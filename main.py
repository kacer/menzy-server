# -*- coding: utf-8 -*-

from flask import Flask
from menzy.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/')
