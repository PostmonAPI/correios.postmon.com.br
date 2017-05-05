# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template, request

from .webservice import correios

bp = Blueprint('rastreamento', __name__)


@bp.route("/")
def index():
    keys = ["P_COD_UNI", "objetos", "objeto"]
    for key in keys:
        objetos = request.args.get(key)
        if objetos is not None:
            break
    response = correios.buscaEventos(objetos)
    objeto = response["objeto"][0]

    if objeto.get("evento"):
        template = 'rastreamento.html'
        status_code = 200
    else:
        template = 'rastreamento_nao_encontrado.html',
        status_code = 404

    return render_template(template, objeto=objeto), status_code


def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)
