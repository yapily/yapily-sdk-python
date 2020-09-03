# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.234
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.bulk_payment_request import BulkPaymentRequest  # noqa: E501
from yapily.rest import ApiException

class TestBulkPaymentRequest(unittest.TestCase):
    """BulkPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.bulk_payment_request.BulkPaymentRequest()  # noqa: E501
        if include_optional :
            return BulkPaymentRequest(
                execution_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                originator_identification_number = '0', 
                payments = [
                    yapily.models.payment_request.PaymentRequest(
                        payment_idempotency_id = '0', 
                        payer = yapily.models.payer.Payer(
                            name = '0', 
                            address = yapily.models.address.Address(
                                address_lines = [
                                    '0'
                                    ], 
                                street_name = '0', 
                                building_number = '0', 
                                post_code = '0', 
                                town_name = '0', 
                                county = [
                                    '0'
                                    ], 
                                address_type = 'BUSINESS', 
                                country = '0', 
                                department = '0', 
                                sub_department = '0', ), 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '0', )
                                ], ), 
                        amount = yapily.models.amount.Amount(
                            amount = 1.337, 
                            currency = '0', ), 
                        reference = '0', 
                        context_type = 'BILL', 
                        type = 'DOMESTIC_PAYMENT', 
                        payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        payee = yapily.models.payee.Payee(
                            name = '0', 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '0', )
                                ], 
                            merchant_id = '0', 
                            merchant_category_code = '0', ), 
                        periodic_payment = yapily.models.periodic_payment_request.PeriodicPaymentRequest(
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
                                currency = '0', ), ), 
                        international_payment = yapily.models.international_payment_request.InternationalPaymentRequest(
                            currency_of_transfer = '0', 
                            exchange_rate_information = yapily.models.exchange_rate_information.ExchangeRateInformation(
                                foreign_exchange_contract_reference = '0', 
                                rate = 1.337, 
                                rate_type = 'ACTUAL', 
                                unit_currency = '0', ), 
                            purpose = '0', 
                            priority = 'NORMAL', 
                            charge_bearer = 'DEBT', ), )
                    ]
            )
        else :
            return BulkPaymentRequest(
                payments = [
                    yapily.models.payment_request.PaymentRequest(
                        payment_idempotency_id = '0', 
                        payer = yapily.models.payer.Payer(
                            name = '0', 
                            address = yapily.models.address.Address(
                                address_lines = [
                                    '0'
                                    ], 
                                street_name = '0', 
                                building_number = '0', 
                                post_code = '0', 
                                town_name = '0', 
                                county = [
                                    '0'
                                    ], 
                                address_type = 'BUSINESS', 
                                country = '0', 
                                department = '0', 
                                sub_department = '0', ), 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '0', )
                                ], ), 
                        amount = yapily.models.amount.Amount(
                            amount = 1.337, 
                            currency = '0', ), 
                        reference = '0', 
                        context_type = 'BILL', 
                        type = 'DOMESTIC_PAYMENT', 
                        payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        payee = yapily.models.payee.Payee(
                            name = '0', 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '0', )
                                ], 
                            merchant_id = '0', 
                            merchant_category_code = '0', ), 
                        periodic_payment = yapily.models.periodic_payment_request.PeriodicPaymentRequest(
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
                                currency = '0', ), ), 
                        international_payment = yapily.models.international_payment_request.InternationalPaymentRequest(
                            currency_of_transfer = '0', 
                            exchange_rate_information = yapily.models.exchange_rate_information.ExchangeRateInformation(
                                foreign_exchange_contract_reference = '0', 
                                rate = 1.337, 
                                rate_type = 'ACTUAL', 
                                unit_currency = '0', ), 
                            purpose = '0', 
                            priority = 'NORMAL', 
                            charge_bearer = 'DEBT', ), )
                    ],
        )

    def testBulkPaymentRequest(self):
        """Test BulkPaymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
