# -*- coding: utf-8 -*-

import logging
import unittest

from test import TestBase
from requests import Session


logger = logging.getLogger(__name__)


class TestGeocoding(TestBase):

    def setUp(self):
        self._session = Session()
        self._prefix = 'http://localhost:7300/api/'

    def test_geocoding(self):
        url = self._prefix + 'geocoding?cityname=上海&keyword=近铁城市广场'
        response = self._session.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def test_reverse_geocoding(self):
        url = self._prefix + 'geocoding/reverse?longitude=121.38149998807&latitude=31.233189678235'  # noqa
        response = self._session.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def tearDown(self):
        self._session.close()
        self._prefix = None


if __name__ == '__main__':
    unittest.main()
