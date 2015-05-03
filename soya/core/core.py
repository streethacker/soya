# -*- coding: utf-8 -*-

import httplib
import requests

import logging

from requests import Session
from contextlib import closing
from soya.utils import SingletonMixin

from soya.utils.exc import (
    UpperServiceException,
)

from soya.settings import (
    API_KEY,
    API_URI,
    API_VERSION,
    OUTPUT_JSON_FORMATTER,
)


logger = logging.getLogger(__name__)


class SoyaToolkit(Session, SingletonMixin):

    def __init__(self, *args, **kwargs):
        super(SoyaToolkit, self).__init__(*args, **kwargs)

        self._api_key = API_KEY
        self._api_uri = API_URI
        self._api_version = API_VERSION
        self._json_output = OUTPUT_JSON_FORMATTER

    def __before_request_hook(self, spec, **kwargs):

        query_str = "&".join([u"{}={}".format(key, val)
                             for key, val in kwargs.iteritems()])

        if self._json_output:
            query_str = query_str + "&" + u"{}={}".format('output', 'json')

        self._req_url = u"{}/{}/{}?ak={}&{}".format(
            self._api_uri,
            self._api_version,
            spec,
            self._api_key,
            query_str.lstrip('&')
        )

        return super(SoyaToolkit, self).get

    def __after_request_hook(self, response):
        if response.status_code != httplib.OK:
            raise UpperServiceException(
                u'错误的状态返回: {}'.format(response.status_code)
            )

        self._resp_headers = response.headers
        self._resp_cookies = response.cookies

        try:
            self._resp_json = response.json()
        except ValueError as e:
            logger.exception(e)
            raise UpperServiceException(
                u'无效的JSON返回值: {}'.format(e.message)
            )

        self.__verify_response_json()
        self.__generate_result()

    def __verify_response_json(self):
        error = self._resp_json.get('error')
        message = self._resp_json.get('status') or 'UNKNOWN ERROR'

        if error:
            raise UpperServiceException(
                u'无效的JSON返回值: {}'.format(message)
            )

    def __generate_result(self):

        if self._resp_json.get('result'):
            self._resp_result = self._resp_json.get('result')
        elif self._resp_json.get('results'):
            self._resp_result = self._resp_json.get('results')
        else:
            self._resp_result = self._resp_json

    def get(self, spec, **kwargs):
        query_func = self.__before_request_hook(spec, **kwargs)

        try:
            with closing(query_func(self._req_url)) as r:
                self.__after_request_hook(r)
        except requests.exceptions.ConnectionError as e:
            logger.exception(e)
            raise UpperServiceException(
                u'无法连接到服务: {}'.format(e.message)
            )
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            raise UpperServiceException(
                u'无效的HTTP响应: {}'.format(e.message)
            )
        except requests.exceptions.Timeout as e:
            logger.exception(e)
            raise UpperServiceException(
                u'HTTP请求超时: {}'.format(e.message)
            )

        return self

    def jsonify(self):
        return self._resp_json

    def get_headers(self):
        return self._resp_headers

    def get_cookies(self):
        return self._resp_cookies

    def get_request_url(self):
        return self._req_url

    @property
    def result(self):
        return self._resp_result

    @classmethod
    def query(clazz, spec, **kwargs):
        return SoyaToolkit().get(spec, **kwargs)
