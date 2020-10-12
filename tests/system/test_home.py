"""
This is a system test for app.py file
"""

from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    """
    This is a test class
    """
    def test_home(self):
        """
        This function will test the home endpoint
        """
        with self.app as c:
            resp = c.get('/')
            print(resp.get_data())
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()),
                             {'message': 'Hello!'})
