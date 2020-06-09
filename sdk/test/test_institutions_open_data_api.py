# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.193
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.institutions_open_data_api import InstitutionsOpenDataApi  # noqa: E501
from yapily.rest import ApiException


class TestInstitutionsOpenDataApi(unittest.TestCase):
    """InstitutionsOpenDataApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.institutions_open_data_api.InstitutionsOpenDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_atm_data_using_get(self):
        """Test case for get_atm_data_using_get

        Retrieves data about all ATMs of the selected institution  # noqa: E501
        """
        pass

    def test_get_personal_current_accounts_using_get(self):
        """Test case for get_personal_current_accounts_using_get

        Retrieves details of personal current accounts for an institution  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
