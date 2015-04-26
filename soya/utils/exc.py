# -*- coding: utf-8 -*-

import httplib


class UpperServiceException(Exception):
    message = 'UPPER SERVICE ERROR'
    code = 1000

    def __init__(self, message=None):
        super(UpperServiceException, self).__init__(message)
        if message is not None:
            self.message = message


class APIError(Exception):
    message = 'API ERROR'
    code = 600
    status_code = httplib.OK

    def __init__(self, message=None):
        super(APIError, self).__init__(message)
        if message is not None:
            self.message = message


class MissingParameter(APIError):
    message = u'缺少参数'
    code = 601


class ParameterFormatError(APIError):
    message = u'参数格式错误'
    code = 602
