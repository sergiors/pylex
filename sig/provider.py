# -*- coding: utf-8 -*-

import abc
from abc import ABCMeta, abstractmethod
from sig.container import Container

class Provider(metaclass=ABCMeta):
    @abstractmethod
    def register(self, container: Container):
        pass
