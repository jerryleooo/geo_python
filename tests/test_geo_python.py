#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_geo_python
----------------------------------

Tests for `geo_python` module.
"""


import unittest

from geo_python.geo_python import Point


class TestGeoPython(unittest.TestCase):

    class TestPoint(Point):
        __key__ = 'test_point'

    def setUp(self):
        self.TestPoint.redis_store.flushall()

    def tearDown(self):
        self.TestPoint.redis_store.flushall()

    def test_add_point(self):
        point = self.TestPoint.add(120, 40, 'test point')
        self.assertEqual(point.longitude, 120)
        self.assertEqual(point.latitude, 40)
        self.assertEqual(point.member, 'test point')

    def test_geo_hash(self):
        pass

    def test_get_pos(self):
        pass

    def test_get_dist(self):
        pass

    def test_get_radius(self):
        pass

    def test_get_radius_by_member(self):
        pass
