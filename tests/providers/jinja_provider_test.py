# -*- coding: utf-8 -*-

import unittest
from pylex import Provider
from pylex.providers import JinjaProvider


class JinjaProviderTest(unittest.TestCase):

    def test_assign(self):
        jinja = JinjaProvider()

        self.assertIsInstance(jinja, Provider)
