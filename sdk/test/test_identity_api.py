# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.245
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.identity_api import IdentityApi  # noqa: E501
from yapily.rest import ApiException


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.identity_api.IdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_identity_using_get(self):
        """Test case for get_identity_using_get

        Get identity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
