python3 setup.py install
export RAZORPAY_KEY_TESTING="your key"
export RAZORPAY_SECRET_TESTING="your secret key"
export APP_SETTINGS=backend.coig.TestingConfig
export FLASK_APP=backend/run.py
flask run