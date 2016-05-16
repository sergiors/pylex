# -*- coding: utf-8 -*-

import unittest
from sig.container import Container

class ContainerTest(unittest.TestCase):
    def test_register(self):
        container = Container()
        container.first_name = 'Sérgio'
        container.last_name = 'Sérgio'


        self.assertEqual('Sérgio', container.first_name)
        self.assertEqual(2, len(container))
        self.assertEqual(True, container.has('first_name'))
        self.assertEqual(False, container.has('middle_name'))

        del container.middle_name