python3 setup.py install
export RAZORPAY_KEY_TESTING=$1
export RAZORPAY_SECRET_TESTING=$2
export APP_SETTINGS=backend.config.TestingConfig
export FLASK_APP=backend/run.py
flask run
