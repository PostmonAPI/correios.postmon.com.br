# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template
from flask import jsonify,request

from .correios import correios_client
from .utils import get_objetos

bp = Blueprint('rastreamento', __name__)


@bp.route("/")
def index():
    objetos, _redirect = get_objetos()
    if _redirect:
        return _redirect

    response = correios_client.buscaEventos(objetos)
    objeto = response["objeto"][0]

    if objeto.get("evento"):
        template = 'rastreamento.html'
        status_code = 200
    else:
        template = 'rastreamento_nao_encontrado.html',
        status_code = 404

    return render_template(template, objeto=objeto), status_code

@bp.route("/objeto/<codigo>")
def getObjeto(codigo):
    codigoObjeto = codigo 
    objetos, _redirect = get_objetos()
    if _redirect:
        return _redirect

    response = correios_client.buscaEventos(codigoObjeto)
    objeto = response["objeto"][0]
    objetoVO = {}
    if objeto.get("evento"):
        status_code = 200
    else:
        status_code = 404
    return jsonify(objeto), status_code
    #return render_template(template, objeto=objeto), status_code

@bp.route('/objetos', methods=['POST'])
def getObjetos():
    data = request.get_json()
    objetos = []
    for item in data:
        print item['codigo']
        response = correios_client.buscaEventos(item['codigo'])
        objeto = response["objeto"][0]
        objetos.append(objeto)
    return jsonify(objetos)

def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)
