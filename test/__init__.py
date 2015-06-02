# -*- coding: utf-8 -*-

import os
import unittest

from unittest import TestLoader, TextTestRunner
from settings import TEST_SETTINGS

import logging


logger = logging.getLogger(__name__)


class TestBase(unittest.TestCase):
    pass


def clear():
    command = "find . -name '*.pyc' | xargs rm -rf"

    try:
        os.system(command)
    except OSError as e:
        logger.exception(e)
        raise


def run_test():
    test_loader = TestLoader()
    test_suite = test_loader.discover(**TEST_SETTINGS)

    runner = TextTestRunner()
    runner.run(test_suite)

    clear()


if __name__ == '__main__':
    run_test()
