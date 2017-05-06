# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, current_app

bp = Blueprint('base', __name__)


@bp.route('/crossdomain.xml')
def crossdomain():
    response = current_app.send_static_file('crossdomain.xml')
    return response


def init_app(app):
    app.register_blueprint(bp)
