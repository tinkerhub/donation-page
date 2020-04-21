import razorpay
from donationpage import app

class razorpay_integration(object):
    """
    Code for razorpay integration lies here
    """
    client = razorpay.Client(auth=(app.config['SECRET_KEY'], app.config['RAZORPAY_SECRET']))

    @classmethod
    def create_order(cls, amount):
        data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'test receipt',
            'payment_capture': 1,
            'notes': {
                'key': 'value'
            }
        }
        order = cls.client.order.create(data)
        order_id = order['id']
        return order_id

    @classmethod
    def get_plan(cls, target_amount, plans):
        items = plans['items']
        for item in items:
            amount = item['item']['amount']
            if amount == target_amount:
                return item['id']
            else:
                return cls.create_plan(target_amount)

    @classmethod
    def create_plan(cls, amount):
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
        plan = cls.client.plan.create(data)
        return plan['id']

    @classmethod
    def create_subscription(cls, amount):
        plans = cls.client.plan.all()
        plan_id = cls.get_plan(amount, plans)
        data = {
            "plan_id":plan_id,
            "total_count":12,
            "quantity": 1,
            "customer_notify":1,
            "notes":{
                'key': 'value'
            }
        }
        subscription = cls.client.subscription.create(data)
        subscription_id = subscription['id']
        return subscription_id

    @classmethod
    def verify_payment(cls, params_dict):
        cls.client.utility.verify_payment_signature(params_dict)

    @classmethod
    def get_payment_details(cls, payment_id):
        return client.payment.fetch(payment_id)



   

