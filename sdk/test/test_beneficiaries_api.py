# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.347
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.beneficiaries_api import BeneficiariesApi  # noqa: E501
from yapily.rest import ApiException


class TestBeneficiariesApi(unittest.TestCase):
    """BeneficiariesApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.beneficiaries_api.BeneficiariesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_beneficiaries_using_get(self):
        """Test case for get_beneficiaries_using_get

        Get beneficiaries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
