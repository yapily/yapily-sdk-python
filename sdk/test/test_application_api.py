# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.167.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.application_api import ApplicationApi  # noqa: E501
from yapily.rest import ApiException


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.application_api.ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_application_me_using_get(self):
        """Test case for get_application_me_using_get

        Returns the details of the application that owns the request credentials  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
