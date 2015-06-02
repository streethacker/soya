# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class SingletonMixin(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(SingletonMixin, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
