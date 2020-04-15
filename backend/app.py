from flask import Flask, request, render_template, session
import json
import requests
import razorpay
import os

#KEY = rzp_live_XmAm96CIbEaD8l
#SECRET = os.environ['SECRET']
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
        data = {
            'amount': int(session['amount']),
            'currency': 'INR',
            'receipt': 'test receipt',
            'payment_capture': 1,
            'notes': {
                'key': 'value'
            }
        }
        order = client.order.create(data)
        order_id = order['id']
        return render_template('app.html', order_id=order_id, amount=session['amount']) 
    elif payment_type == "subscription":
        plans = client.plan.all()
        return "Work in progress"

def explore_plans(amount, plans):
    pass


@app.route('/charge', methods=['POST'])
def app_charge():
    params_dict = dict(request.form.iteritems())
    try:
        client.utility.verify_payment_signature(params_dict)
    except ValueError:
        return json.dumps('Signature Validatioon failed')
    payment_id = request.form['razorpay_payment_id']
    session.pop('amount', 0)
    return json.dumps(client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()