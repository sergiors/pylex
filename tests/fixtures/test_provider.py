# -*- codig: utf-8 -*-

from pylex import Container, Provider


class TestProvider(Provider):

    def register(self, container: Container) -> None:
        container['test.y'] = 0
        container['test'] = lambda x: x * container['test.y']
