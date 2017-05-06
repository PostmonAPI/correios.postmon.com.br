# coding: utf-8
from __future__ import absolute_import

from . import base, rastreamento, webservice, websro


def init_app(app):
    base.init_app(app)
    webservice.init_app(app, url_prefix='/webservice')
    websro.init_app(app, url_prefix='/websro')
    rastreamento.init_app(app, url_prefix='/rastreamento')
