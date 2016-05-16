# -*- coding: utf-8 -*-

class Container(dict):
    def __delitem__(self, name):
        if self.has(name):
            dict.__delitem__(self, name)

    def has(self, name):
        return name in self