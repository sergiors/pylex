# -*- coding: utf-8 -*-

from pylex import Container, Provider, Bootable
from pylex.http import Request, Response


class HttpProvider(Provider, Bootable):

    def register(self, container: Container) -> None:
        container['request'] = Request()
        container['response'] = Response()

    def boot(self, container: Container) -> None:
        pass
