# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_subscribed_events(self) -> dict:
        pass
