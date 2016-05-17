# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from pylex import Container


class Provider(metaclass=ABCMeta):

    @abstractmethod
    def register(self, container: Container) -> None:
        pass
