# coding: utf-8
from __future__ import absolute_import

from flask import Flask

from postmon_correios import webservice

app = Flask(__name__)
webservice.init_app(app, url_prefix='/webservice')
