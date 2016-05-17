# -*- coding: utf-8 -*-

import unittest
from sig import Provider
from sig.providers import JinjaProvider


class JinjaProviderTest(unittest.TestCase):

    def test_assign(self):
        jinja = JinjaProvider()

        self.assertIsInstance(jinja, Provider)
