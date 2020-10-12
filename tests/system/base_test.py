"""
This file contain a master class for tests from
file test_home.py
"""

from unittest import TestCase
from app import app


class BaseTest(TestCase):
    """
    This class will setup all common parameters for the tests.
    By creating a master class for the test, the maintenance of
    the code is much easier later on.
    """
    def setUp(self):
        """

        """
        app.testing = True
        self.app = app.test_client()
