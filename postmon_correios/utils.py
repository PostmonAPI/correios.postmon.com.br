# coding: utf-8
from __future__ import absolute_import

from flask import redirect, request, url_for


def clean_objetos(objetos):
    objetos = objetos.replace(" ", "")
    return objetos


def get_objetos(keys=["P_COD_UNI", "objetos", "objeto"]):
    for key in keys:
        objetos = request.args.get(key)
        if objetos is None:
            continue

        cleaned_objetos = clean_objetos(objetos)

        if cleaned_objetos == objetos:
            _redirect = None
        else:
            url = url_for(request.endpoint, **{key: cleaned_objetos})
            _redirect = redirect(url)

        return objetos, _redirect

    return None, None
