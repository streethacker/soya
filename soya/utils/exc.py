# -*- coding: utf-8 -*-


class UpperServiceError(Exception):
    code = 1000


class APIError(Exception):
    code = 600


class MissingParameter(APIError):
    code = 601


class ParameterFormatError(APIError):
    code = 602
