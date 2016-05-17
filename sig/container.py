# -*- coding: utf-8 -*-


class Container(dict):

    def __delitem__(self, name):
        if self.has(name):
            dict.__delitem__(self, name)

    def has(self, name) -> bool:
        return name in self

    def register(self, provider, values={}) -> None:
        provider.register(self)

        for k, v in values.items():
            self[k] = v

