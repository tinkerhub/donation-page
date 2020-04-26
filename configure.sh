python3 setup.py install
export RAZORPAY_KEY_TESTING=<KEY>
export RAZORPAY_SECRET_TESTING=<SECRET>
export APP_SETTINGS=donationpage.config.TestingConfig
export FLASK_APP=donationpage/run.py
export MAILGUN_API_KEY=<PRIVATE_KEY>
flask run
