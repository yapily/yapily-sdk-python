# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.299
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.statements_api import StatementsApi  # noqa: E501
from yapily.rest import ApiException


class TestStatementsApi(unittest.TestCase):
    """StatementsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.statements_api.StatementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statement_file_using_get(self):
        """Test case for get_statement_file_using_get

        Get account statement file  # noqa: E501
        """
        pass

    def test_get_statement_using_get(self):
        """Test case for get_statement_using_get

        Get account statement  # noqa: E501
        """
        pass

    def test_get_statements_using_get(self):
        """Test case for get_statements_using_get

        Get account statements  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
