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
        self.TestPoint.redis_store.delete(self.TestPoint.__key__)

    def tearDown(self):
        self.TestPoint.redis_store.delete(self.TestPoint.__key__)

    def test_create_point(self):
        point = self.TestPoint.create(120, 40, 'test point')
        self.assertEqual(point.longitude, 120)
        self.assertEqual(point.latitude, 40)
        self.assertEqual(point.member, 'test point')

    def test_geo_hash(self):
        point = self.TestPoint.create(120, 40, 'test point')
        self.assertEqual(point.geo_hash(), "wxj7d9v2fs0")

    def test_delete_pos(self):
        point = self.TestPoint.create(120, 40, 'test point')
        point.delete()
        query_result = self.TestPoint.redis_store.georadius(self.TestPoint.__key__, 120, 40, 10000)
        assert not query_result

    def test_update_point(self):
        test_point_2 = 'test point 2'
        point = self.TestPoint.create(120, 40, 'test point')
        point.update(member=test_point_2)
        self.assertEqual(point.member, test_point_2)

    def test_query_by_pos(self):
        point = self.TestPoint.create(120, 40, 'test point')
        self.assertIn(point.member, [p.member for p in self.TestPoint.query_by_pos(120, 40, 10000)])

    def test_query_by_member(self):
        point = self.TestPoint.create(120, 40, 'test point')
        self.assertIn(point.member, [p.member for p in self.TestPoint.query_by_member(point.member)])

    def test_dist(self):
        point1 = self.TestPoint.create(120, 40, 'test point 1')
        point2 = self.TestPoint.create(119, 40, 'test point 2')
        self.assertEqual(int(self.TestPoint.dist(point1, point2)), 85204)

