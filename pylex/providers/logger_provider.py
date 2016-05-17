# -*- coding: utf-8 -*-

from logbook import Logger
from pylex import Container, Provider


class LoggerProvider(Provider):

    def register(self, container: Container) -> None:
        container['logger'] = Logger()
