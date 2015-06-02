# -*- coding: utf-8 -*-

import unittest
import logging

from test import TestBase
from requests import Session


logger = logging.getLogger(__name__)


class TestAssist(TestBase):

    def setUp(self):
        self._request = Session()
        self._prefix = 'http://localhost:7300/api/'

    def test_get_weater(self):
        url = self._prefix + 'weather?location=北京&current_only=1&origin=0'
        response = self._request.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def test_get_traffic(self):
        url = self._prefix +\
            'traffic?location=北京&start_time=2015-04-01&end_time=2015-05-05'
        response = self._request.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def tearDown(self):
        self._request.close()
        self._prefix = None


if __name__ == '__main__':
    unittest.main()
