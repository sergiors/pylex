# -*- coding: utf-8 -*-

import unittest
from sig.container import Container

class ContainerTest(unittest.TestCase):
    def test_assign(self):
        container = Container()
        container['first_name'] = 'Jimi'
        container['last_name'] = 'Hendrix'

        self.assertEqual('Jimi', container['first_name'])
        self.assertEqual(2, len(container))
        self.assertEqual(True, container.has('first_name'))
        self.assertEqual(False, container.has('middle_name'))

    def test_del(self):
        container = Container()
        container['last_name'] = 'Hendrix'
        self.assertEqual(True, container.has('last_name'))
        self.assertEqual('Hendrix', container['last_name'])

        del container['last_name']
        del container['middle_name']
        self.assertEqual(False, container.has('first_name'))
        self.assertEqual(0, len(container))