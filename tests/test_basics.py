# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import os
import unittest

class BasicTestCase(unittest.TestCase):

    def test_python_version(self):
        """Application runs under Python 2.7, not 2.6.
        Test for 2.7.6 or greater (as long as it's 2.7)."""
        assert 2 == sys.version_info.major
        assert 7 == sys.version_info.minor
        assert 6 <= sys.version_info.micro
