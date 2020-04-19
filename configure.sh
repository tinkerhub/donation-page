python3 setup.py install
export RAZORPAY_KEY_TESTING=<KEY>
export RAZORPAY_SECRET_TESTING=<SECRET>
export APP_SETTINGS=backend.coig.TestingConfig
export FLASK_APP=backend/run.py
flask run