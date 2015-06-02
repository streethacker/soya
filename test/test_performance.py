# -*- coding: utf-8 -*-

import time
import StringIO
import logging

from requests import Session


logger = logging.getLogger(__name__)


TARGET_DICT = {
    'geocoding': 'geocoding?cityname=上海&keyword=近铁城市广场',

    'reverse_geocoding':
    'geocoding/reverse?longitude=121.38149998807&latitude=31.233189678235',

    'get_weather': 'weather?location=北京&current_only=1&origin=0',

    'get_traffic':
    'traffic?location=北京&start_time=2015-04-01&end_time=2015-05-05',

    'get_hot_movie':
    'movie/hot?location=北京&is_new=0&is_imax=1&movie_score=8.0',

    'search_cinema':
    'search/cinema?location=北京&cinema_name=华星&movie_score=8.5',

    'search_movie':
    'search/movie?location=北京&movie_name=复仇者联盟2&rating=3.5',
}


def test_performance():
    buffer_ = StringIO.StringIO()
    request = Session()
    prefix = 'http://localhost:7300/api/'

    for func_name, target in TARGET_DICT.iteritems():
        start = time.time()
        request.get(prefix + target)
        delta = time.time() - start

        print >> buffer_, '{}|{}'.format(func_name, float(delta)*100)

    with open('./profile.txt', 'wb') as prof:
        prof.write(buffer_.getvalue())

if __name__ == '__main__':
    test_performance()
