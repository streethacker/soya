# -*- coding: utf-8 -*-

import httplib
import requests

import logging

from requests import (
    Session,
)

from contextlib import (
    closing,
)

from soya.utils import (
    SingletonMixin,
)

from soya.utils.exc import (
    UpperServiceError,
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

    def get(self, spec, **kwargs):
        self.__before_request_hook(spec, **kwargs)

        query_func = super(SoyaToolkit, self).get

        try:
            with closing(query_func(self._req_url)) as r:
                if r.status_code != httplib.OK:
                    raise UpperServiceError(
                        u'上层API服务无法访问:{}'.format(r.status_code))

                self._resp_headers = r.headers
                self._resp_cookies = r.cookies

                try:
                    self._resp_json = r.json()
                except ValueError as e:
                    logger.exception(e)
                    self._resp_json = {}
        except requests.exceptions.ConnectionError as e:
            logger.exception(e)
            raise UpperServiceError(u'无法连接上层API服务')
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            raise UpperServiceError(u'无效的HTTP响应')
        except requests.exceptions.Timeout as e:
            logger.exception(e)
            raise UpperServiceError(u'HTTP请求超时')

        return self

    def jsonify(self):
        return self._resp_json

    def get_headers(self):
        return self._resp_headers

    def get_cookies(self):
        return self._resp_cookies

    def get_request_url(self):
        return self._req_url

    @classmethod
    def query(clazz, spec, **kwargs):
        return SoyaToolkit().get(spec, **kwargs)
