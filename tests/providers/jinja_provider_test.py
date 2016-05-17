# -*- coding: utf-8 -*-

import unittest
from sig.container import Container
from sig.provider import Provider
from sig.providers.jinja_provider import JinjaProvider

class JinjaProviderTest(unittest.TestCase):
    def test_assign(self):
        jinja = JinjaProvider()

        self.assertIsInstance(jinja, Provider)
