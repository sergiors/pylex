# -*- coding: utf-8 -*-

from sig import Container, Provider
from logbook import Logger


class LoggerProvider(Provider):

    def register(self, container: Container):
        container['logger'] = Logger()
