# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.266
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.pre_auth_consent_controller_api import PreAuthConsentControllerApi  # noqa: E501
from yapily.rest import ApiException


class TestPreAuthConsentControllerApi(unittest.TestCase):
    """PreAuthConsentControllerApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.pre_auth_consent_controller_api.PreAuthConsentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pre_authorisation_using_post(self):
        """Test case for create_pre_authorisation_using_post

        Initiate request for user to pre authorise  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
