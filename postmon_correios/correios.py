# coding: utf-8
from __future__ import absolute_import

from flask import current_app, request
from werkzeug.local import LocalProxy
from zeep import Client as Zeep
from zeep.cache import InMemoryCache
from zeep.helpers import serialize_object
from zeep.transports import Transport

correios_client = LocalProxy(lambda: current_app.extensions["correios"])


class Client(object):
    wsdl = 'http://webservice.correios.com.br/service/rastro/Rastro.wsdl'

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    @property
    def service(self):
        if not hasattr(self, "_service"):
            client = Zeep(
                wsdl=self.wsdl,
                transport=Transport(cache=InMemoryCache()))
            self._service = client.service
        return self._service

    def init_app(self, app):
        app.extensions["correios"] = self

    def buscaEventos(self, objetos, tipo="L", resultado="T", lingua="101"):
        data = {
            "objetos": objetos,
            "tipo": tipo,
            "resultado": resultado,
            "lingua": lingua,
            # auth
            "usuario": request.headers.get('x-correios-usuario', "ECT"),
            "senha": request.headers.get('x-correios-senha', "SRO"),
        }

        response = self.service.buscaEventos(**data)
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
        response = self.service.buscaEventosLista(**data)
        return serialize_object(response)
