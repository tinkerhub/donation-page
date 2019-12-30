from flask import Flask, request, render_template, session
import json
import requests
import razorpay
import os

KEY = os.environ['KEY']
SECRET = os.environ['SECRET']
client = razorpay.Client(auth=(KEY, SECRET))
app = Flask(__name__)
@app.route('/health', methods=['GET'])
def health_check():
    """
    To check if the server is up or not
    """
    return "O.K", 200

@app.route('/', methods=['POST'])
def donation_logic():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        if 'payment_type' in data:
            if data['payment_type'] == "one_time":
                session['amount'] = data['amount'] + '00'
                return render_template('app.html', amount=session['amount'])
            elif data['payment_type'] == "subscription":
                pass


@app.route('/charge', methods=['POST'])
def app_charge():
    amount = int(session['amount'])
    payment_id = request.form['razorpay_payment_id']
    client.payment.capture(payment_id, amount)
    session.pop('amount', 0)
    return json.dumps(client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.run()