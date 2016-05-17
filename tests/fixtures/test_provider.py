# -*- codig: utf-8 -*-

from sig.container import Container
from sig.provider import Provider

class TestProvider(Provider):
    def register(self, container: Container):
        container['test'] = lambda x: x * 2



