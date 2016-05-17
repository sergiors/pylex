# -*- coding: utf-8 -*-

from pylex import Container, Provider
from pylex.http import Request, Response


class HttpProvider(Provider):

    def register(self, container: Container):
        container['request'] = Request()
        container['response'] = Response()
