from flask import Flask, request, render_template, session
import json
import requests
import os
from donationpage.payment import razorpay_integration
from donationpage import app

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
    data = json.dumps(razorpay_integration.get_payment_details(payment_id))
    return render_template('thankyou.html', email=data['email'], order_id=data['order_id'], amount=int(str(data['amount'])[:-1]))

