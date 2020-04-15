from flask import Flask, request, render_template, session
import json
import requests
import razorpay
import os

KEY = os.environ['KEY']
SECRET = os.environ['SECRET']
client = razorpay.Client(auth=("<APP_ID>", "<APP_SECRET>"))
app = Flask(__name__)
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
    amount = request.form['amount']
    payment_type = request.form['type']
    if payment_type == "one_time":
        session['amount'] = amount + '00'
        amount = int(session['amount'])
        order_id = create_order(amount)
        return render_template('order.html', order_id=order_id, amount=session['amount'], key=key) 
    elif payment_type == "subscription":
        plans = client.plan.all()
        subscription_id = create_subscription(amount, plans)
        return render_template('subscription.html', subscription_id=subscription_id, amount=session['amount'], key=key)

def create_order(amount):
    data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'test receipt',
        'payment_capture': 1,
        'notes': {
            'key': 'value'
        }
    }
    order = client.order.create(data)
    order_id = order['id']
    return order_id

def get_plan(amount, plans):
    items = plans['items']
    for item in items:
        amount = item['item']['amount']
        if amount == target_amount:
            return item['id']
        else:
            return create_plan(amount)

def create_plan(amount):
    data = {
        "period": "monthly",
        "interval": 1,
        "item": {
            "name": "TinkeHub monthly plan - "+ str(amount),
            "amount": amount,
            "currency": "INR",
            "description": "This plan takes " + str(amount) + "monthly."
        },
        "notes": {
            'key': 'value'
        } 
    }
    plan = client.plan.create(data)
    return plan['id']

def create_subscription(amount, plans):
    plan_id = get_plan(amount, plans)
    data = {
        "plan_id":plan_id,
        "total_count":12,
        "quantity": 1,
        "customer_notify":1,
        "notes":{
            'key': 'value'
        }
    }
    subscription = client.subscription.create(data)
    subscription_id = subscription['id']
    return subscription_id


@app.route('/charge', methods=['POST'])
def app_charge():
    params_dict = dict(request.form.iteritems())
    try:
        client.utility.verify_payment_signature(params_dict)
    except ValueError:
        #should render_template the transaction failed html
        return json.dumps('Signature Validatioon failed')
    payment_id = request.form['razorpay_payment_id']
    session.pop('amount', 0)
    #should render_template thank you for your support html
    return json.dumps(client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()