# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.349
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.embedded_payments_api import EmbeddedPaymentsApi  # noqa: E501
from yapily.rest import ApiException


class TestEmbeddedPaymentsApi(unittest.TestCase):
    """EmbeddedPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.embedded_payments_api.EmbeddedPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_embedded_payment_authorisation_using_post(self):
        """Test case for create_embedded_payment_authorisation_using_post

        Initiate an embedded payment for user to authorise  # noqa: E501
        """
        pass

    def test_update_embedded_payment_authorisation_using_put(self):
        """Test case for update_embedded_payment_authorisation_using_put

        Update an embedded payment initiation with SCA info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
