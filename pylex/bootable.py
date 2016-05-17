# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from . import Container


class Bootable(metaclass=ABCMeta):

    @abstractmethod
    def boot(self, container: Container) -> None:
        pass
