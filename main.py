# coding: utf-8
from __future__ import absolute_import

from flask import Flask

from postmon_correios import rastreamento, webservice, websro

app = Flask(__name__)
webservice.init_app(app, url_prefix='/webservice')
websro.init_app(app, url_prefix='/websro')
rastreamento.init_app(app, url_prefix='/rastreamento')
