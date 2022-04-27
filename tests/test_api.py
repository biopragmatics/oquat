# -*- coding: utf-8 -*-

"""Test API functions."""

import unittest

from oquat.robot import robot_parse_json_remote


class TestAPI(unittest.TestCase):
    """Trivially test a version."""

    def test_parse_owl(self):
        """Test parsing a remote JSON graph."""
        uri = "http://purl.obolibrary.org/obo/pato.owl"
        result = robot_parse_json_remote(uri)
        self.assertIsNotNone(result)
