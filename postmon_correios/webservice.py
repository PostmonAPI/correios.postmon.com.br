# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, jsonify, request

from .correios import Client as CorreiosClient

correios = CorreiosClient()

bp = Blueprint('webservice', __name__)


def _filter_data(data, keys):
    _map = {}
    for key in keys:
        value = request.args.get(key)
        if value:
            _map[key] = value

    return _map


@bp.route("/buscaEventos/")
def buscaEventos():
    values = request.values
    data = _filter_data(
        values,
        ["objetos", "tipo", "resultado", "lingua"])
    data.setdefault("objetos", None)
    response = correios.buscaEventos(**data)
    return jsonify(response)


@bp.route("/buscaEventosLista/")
def buscaEventosLista():
    values = request.values
    data = _filter_data(
        values,
        ["tipo", "resultado", "lingua"])
    data["objetos"] = request.args.getlist("objetos")
    response = correios.buscaEventosLista(**data)
    return jsonify(response)


def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)
