python3 setup.py install
export RAZORPAY_KEY_TESTING=$1
export RAZORPAY_SECRET_TESTING=$2
export APP_SETTINGS=donationpage.config.TestingConfig
export FLASK_APP=donationpage/run.py
flask run
