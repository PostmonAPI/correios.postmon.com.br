# coding: utf-8
from __future__ import absolute_import

from . import correios, rastreamento, webservice, websro


def init_app(app):
    correios_client = correios.Client()
    correios_client.init_app(app)

    webservice.init_app(app, url_prefix='/webservice')
    websro.init_app(app, url_prefix='/websro')
    rastreamento.init_app(app, url_prefix='/rastreamento')
