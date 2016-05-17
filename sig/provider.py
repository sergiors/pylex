# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from sig import Container


class Provider(metaclass=ABCMeta):

    @abstractmethod
    def register(self, container: Container):
        pass
