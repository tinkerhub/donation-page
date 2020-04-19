from flask import Flask
import os
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
from backend.service import *
from backend.payment import *
from backend.config import *
