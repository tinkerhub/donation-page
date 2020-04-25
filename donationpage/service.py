from flask import request, render_template
import json
import requests
import os
from donationpage.payment import razorpay_integration
from donationpage import app
from donationpage.mail_boy import send_mail
@app.route('/health', methods=['GET'])
def health_check():
    """
    To check if the server is up or not
    """
    return "O.K", 200

@app.route('/')
def donation_page():
    return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donation_logic():
    amount = request.form['amount'] + '00'
    amount_int = int(amount)
    payment_type = request.form['type']
    if payment_type == "one_time":
        order_id = razorpay_integration.create_order(amount_int)
        return render_template('order.html', order_id=order_id, amount=amount_int, key=app.config['SECRET_KEY']) 
    elif payment_type == "subscription":
        subscription_id = razorpay_integration.create_subscription(amount_int)
        return render_template('subscription.html', subscription_id=subscription_id, amount=amount_int, key=app.config['SECRET_KEY'])

@app.route('/charge', methods=['POST'])
def app_charge():
    params_dict = dict(request.form.iteritems())
    try:
        razorpay_integration.verify_payment(params_dict)
    except ValueError:
        #should render_template the transaction failed html
        return json.dumps('Signature Validatioon failed')
    payment_id = request.form['razorpay_payment_id']
    data = razorpay_integration.get_payment_details(payment_id)
    amount = int(str(data['amount'])[:-2])
    email = data['email']
    send_mail(email)
    return render_template('thankyou.html', order_id=data['order_id'], amount=amount)

@app.route('/subscription', methods=['POST'])
def app_subscription():
    subscription_id = request.form['razorpay_subscription_id']
    data = razorpay_integration.get_subscription_details(subscription_id)
    customer_data = razorpay_integration.get_customer_details(data['customer_id'])
    email = customer_data['email']
    send_mail(email)
    return render_template('thankyou2.html', subscription_id= subscription_id, months=data['total_count'])