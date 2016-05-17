# -*- coding: utf-8 -*-

from sig import Container, Provider
from sig.http import Request, Response


class HttpProvider(Provider):

    def register(self, container: Container):
        container['request'] = Request()
        container['response'] = Response()
