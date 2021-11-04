# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.157.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.embedded_accounts_api import EmbeddedAccountsApi  # noqa: E501
from yapily.rest import ApiException


class TestEmbeddedAccountsApi(unittest.TestCase):
    """EmbeddedAccountsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.embedded_accounts_api.EmbeddedAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_initiate_embedded_account_request_using_post(self):
        """Test case for initiate_embedded_account_request_using_post

        Initiate a new embedded account request for user to authorize  # noqa: E501
        """
        pass

    def test_update_embedded_account_request_using_put(self):
        """Test case for update_embedded_account_request_using_put

        Update an embedded account request with SCA info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
