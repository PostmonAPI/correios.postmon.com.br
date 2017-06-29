# coding: utf-8
from __future__ import absolute_import

from flask import current_app
from werkzeug.local import LocalProxy
from zeep import Client as Zeep
from zeep.cache import InMemoryCache
from zeep.helpers import serialize_object
from zeep.transports import Transport

correios_client = LocalProxy(lambda: current_app.extensions["correios"])


class Client(object):
    wsdl = 'http://webservice.correios.com.br/service/rastro/Rastro.wsdl'
    auth = {
        "usuario": "ECT",
        "senha": "SRO",
    }

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.client = Zeep(
            wsdl=self.wsdl,
            transport=Transport(cache=InMemoryCache()),
        )
        app.extensions["correios"] = self

    def buscaEventos(self, objetos, tipo="L", resultado="T", lingua="101"):
        data = {
            "objetos": objetos,
            "tipo": tipo,
            "resultado": resultado,
            "lingua": lingua,
        }
        data.update(self.auth)
        response = self.client.service.buscaEventos(**data)
        return serialize_object(response)

    def buscaEventosLista(self, objetos,
                          tipo="L", resultado="T", lingua="101"):
        data = {
            "objetos": objetos,
            "tipo": tipo,
            "resultado": resultado,
            "lingua": lingua,
        }
        data.update(self.auth)
        response = self.client.buscaEventosLista(**data)
        return serialize_object(response)
