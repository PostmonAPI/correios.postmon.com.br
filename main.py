# coding: utf-8
from __future__ import absolute_import

from flask import Flask

import postmon_correios


def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    postmon_correios.init_app(app)
    return app
