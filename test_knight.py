""" Module for api test"""

import json
import unittest
from app import create_app


class KnightTestCase(unittest.TestCase):
    """Knight shortest path testcases"""
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_api(self):
        """Method for testing correct response and path."""
        res = self.client.get('/apiv1/shortestpath?start=b6&end=e1')
        result = json.loads(res.data.decode())
        self.assertEqual(result['status'], "success")
        self.assertEqual(result['path']['1'], "b6")
        self.assertEqual(result['path']['4'], "e1")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()