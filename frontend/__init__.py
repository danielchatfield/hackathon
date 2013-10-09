"""
Frontend app

"""
import libs
from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder="assets")

import frontend.views