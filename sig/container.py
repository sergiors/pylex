# -*- coding: utf-8 -*-

class Container:
    __values = {}

    def __getattr__(self, name):
        if self.has(name):
            return self.__values[name]

        return False

    def __setattr__(self, name, value):
        self.__values[name] = value

    def __delattr__(self, name):
        if self.has(name):
            del self.__values[name]

    def __len__(self):
        return len(self.__values)

    def has(self, name):
        return name in self.__values