# -*- coding: utf-8 -*-

from logbook import Logger
from sig import Container, Provider


class LoggerProvider(Provider):

    def register(self, container: Container) -> None:
        container['logger'] = Logger()
