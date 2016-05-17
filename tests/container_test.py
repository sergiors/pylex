# -*- coding: utf-8 -*-

import unittest
from sig import Container
from tests.fixtures.test_provider import TestProvider


class ContainerTest(unittest.TestCase):

    def test_assign(self):
        container = Container()
        container['first_name'] = 'Jimi'
        container['last_name'] = 'Hendrix'

        self.assertEqual(container['first_name'], 'Jimi')
        self.assertEqual(len(container), 2)
        self.assertTrue(container.has('first_name'))
        self.assertFalse(container.has('middle_name'))

    def test_del(self):
        container = Container()
        container['last_name'] = 'Hendrix'
        self.assertTrue(container.has('last_name'))
        self.assertEqual(container['last_name'], 'Hendrix')

        del container['last_name']
        del container['middle_name']
        self.assertFalse(container.has('first_name'))
        self.assertEqual(len(container), 0)

    def test_register(self):
        container = Container()
        container.register(TestProvider())

        self.assertEqual(container['test'](2), 4)
