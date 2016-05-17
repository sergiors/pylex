# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from . import Container


class Provider(metaclass=ABCMeta):

    @abstractmethod
    def register(self, container: Container) -> None:
        pass
