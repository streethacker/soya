# -*- coding: utf-8 -*-

import unittest
import logging

from test import TestBase
from requests import Session


logger = logging.getLogger(__name__)


class TestAmuse(TestBase):

    def setUp(self):
        self._request = Session()
        self._prefix = 'http://localhost:7300/api/'

    def test_get_hot_movie(self):
        url = self._prefix + \
            'movie/hot?location=北京&is_new=0&is_imax=1&movie_score=8.0'

        response = self._request.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def test_search_cinema(self):
        url = self._prefix + \
            'search/cinema?location=北京&cinema_name=华星&movie_score=8.5'
        response = self._request.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def test_search_movie(self):
        url = self._prefix + \
            'search/movie?location=北京&movie_name=复仇者联盟2&rating=3.5'
        response = self._request.get(url)
        self.assertTrue(response.status_code == 200)

        result = response.json()
        self.assertTrue(result['code'] == 200)

    def tearDown(self):
        self._request.close()
        self._prefix = None


if __name__ == '__main__':
    unittest.main()
