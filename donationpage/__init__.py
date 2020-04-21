from flask import Flask
import os
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
from donationpage.payment import *
from donationpage.config import *
from donationpage.service import *