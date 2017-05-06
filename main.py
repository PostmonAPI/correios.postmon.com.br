# coding: utf-8
from __future__ import absolute_import

from flask import Flask

import postmon_correios

app = Flask(__name__)
postmon_correios.init_app(app)
