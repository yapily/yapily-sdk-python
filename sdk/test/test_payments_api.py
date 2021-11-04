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
from yapily.api.payments_api import PaymentsApi  # noqa: E501
from yapily.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.payments_api.PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bulk_payment_authorisation_using_post(self):
        """Test case for create_bulk_payment_authorisation_using_post

        Initiate bulk payment for user to authorise  # noqa: E501
        """
        pass

    def test_create_bulk_payment_using_post(self):
        """Test case for create_bulk_payment_using_post

        Create bulk payment  # noqa: E501
        """
        pass

    def test_create_payment_authorisation_using_post(self):
        """Test case for create_payment_authorisation_using_post

        Initiate a payment for user to authorise  # noqa: E501
        """
        pass

    def test_create_payment_authorisation_with_sort_code_using_post(self):
        """Test case for create_payment_authorisation_with_sort_code_using_post

        Initiate a new single payment for user to authorise  # noqa: E501
        """
        pass

    def test_create_payment_using_post(self):
        """Test case for create_payment_using_post

        Create a payment  # noqa: E501
        """
        pass

    def test_create_payment_with_sort_code_using_post(self):
        """Test case for create_payment_with_sort_code_using_post

        Create a new single payment  # noqa: E501
        """
        pass

    def test_get_payment_status_using_get(self):
        """Test case for get_payment_status_using_get

        Get status of a payment  # noqa: E501
        """
        pass

    def test_get_payments_using_get(self):
        """Test case for get_payments_using_get

        Get payments details  # noqa: E501
        """
        pass

    def test_update_payment_authorisation_using_put(self):
        """Test case for update_payment_authorisation_using_put

        Update pre authorize consent for user to authorise payment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
