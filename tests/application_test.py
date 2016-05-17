# -*- coding: utf-8 -*-

import unittest
from pylex import Application
from pylex.providers import HttpProvider
from pylex.http import Request, Response


class ApplicationTest(unittest.TestCase):

    def init_test(self):
        app = Application()

        self.assertEqual('utf-8', app['charset'])
        self.assertEqual(False, app['debug'])

    def register_test(self):
        app = Application()
        app.register(HttpProvider())

        self.assertTrue(app.has('request'))
        self.assertTrue(app.has('response'))
        self.assertIsInstance(app['request'], Request)
        self.assertIsInstance(app['response'], Response)
