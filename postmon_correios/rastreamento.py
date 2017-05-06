# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template

from .utils import get_objetos
from .webservice import correios

bp = Blueprint('rastreamento', __name__)


@bp.route("/")
def index():
    objetos, _redirect = get_objetos()
    if _redirect:
        return _redirect

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
