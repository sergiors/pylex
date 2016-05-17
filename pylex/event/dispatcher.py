# -*- coding: utf-8 -*-

from . import Subscriber


class Dispatcher:

    __listeners = {}

    def add_subscriber(self, subscriber: Subscriber) -> None:
        pass
