# -*- coding: utf-8 -*-

import unittest
from sig import Application
from sig.providers import HttpProvider
from sig.http import Request, Response


class ApplicationTest(unittest.TestCase):

    def register_test(self):
        app = Application()
        app.register(HttpProvider())

        self.assertTrue(app.has('request'))
        self.assertTrue(app.has('response'))
        self.assertIsInstance(app['request'], Request)
        self.assertIsInstance(app['response'], Response)
