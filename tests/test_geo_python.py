#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_geo_python
----------------------------------

Tests for `geo_python` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from geo_python import geo_python
from geo_python import cli



class TestGeo_python(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'geo_python.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
