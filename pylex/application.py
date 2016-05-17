# -*- coding: utf-8 -*-

from pylex import Container, Bootable


class Application(Container):

    __providers = []
    __booted = False

    def __init__(self, values={}) -> None:
        self['debug'] = False
        self['charset'] = 'utf-8'

        for k, v in values.items():
            self[k] = v

    def register(self, provider, values={}):
        self.__providers.append(provider)
        Container.register(self, provider, values)

        return self

    def boot(self):
        if self.__booted:
            return

        self.__booted = True

        for provider in self.__providers:
            if isinstance(provider, Bootable):
                provider.boot(self)

