# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template, request

bp = Blueprint('websro', __name__)


from .webservice import correios


@bp.route("/")
def index():
    keys = ["P_COD_UNI", "objetos", "objeto"]
    for key in keys:
        objetos = request.args.get(key)
        if objetos is not None:
            break
    response = correios.buscaEventos(objetos)
    return render_template('websro.html', objeto=response["objeto"][0])


def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)