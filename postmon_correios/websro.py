# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template, request

bp = Blueprint('websro', __name__)


from .webservice import correios


@bp.route("/")
def index():
    objetos = request.args.get("P_COD_UNI")
    if objetos is None:
        objetos = request.args.get("objetos")
    response = correios.buscaEventos(objetos)
    return render_template('websro.html', objeto=response["objeto"][0])


def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)
