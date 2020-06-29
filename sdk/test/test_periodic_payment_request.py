# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.201
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.periodic_payment_request import PeriodicPaymentRequest  # noqa: E501
from yapily.rest import ApiException

class TestPeriodicPaymentRequest(unittest.TestCase):
    """PeriodicPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PeriodicPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.periodic_payment_request.PeriodicPaymentRequest()  # noqa: E501
        if include_optional :
            return PeriodicPaymentRequest(
                frequency = yapily.models.frequency_request.FrequencyRequest(
                    type = 'DAILY', 
                    interval_week = 56, 
                    interval_month = 56, 
                    execution_day = 56, ), 
                number_of_payments = 56, 
                next_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                next_payment_amount = yapily.models.amount.Amount(
                    amount = 1.337, 
                    currency = '0', ), 
                final_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                final_payment_amount = yapily.models.amount.Amount(
                    amount = 1.337, 
                    currency = '0', )
            )
        else :
            return PeriodicPaymentRequest(
                frequency = yapily.models.frequency_request.FrequencyRequest(
                    type = 'DAILY', 
                    interval_week = 56, 
                    interval_month = 56, 
                    execution_day = 56, ),
        )

    def testPeriodicPaymentRequest(self):
        """Test PeriodicPaymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
