# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.307
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.iso_bank_transaction_code import IsoBankTransactionCode  # noqa: E501
from yapily.rest import ApiException

class TestIsoBankTransactionCode(unittest.TestCase):
    """IsoBankTransactionCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IsoBankTransactionCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.iso_bank_transaction_code.IsoBankTransactionCode()  # noqa: E501
        if include_optional :
            return IsoBankTransactionCode(
                domain_code = yapily.models.iso_code_details.IsoCodeDetails(
                    code = '0', 
                    name = '0', ), 
                family_code = yapily.models.iso_code_details.IsoCodeDetails(
                    code = '0', 
                    name = '0', ), 
                sub_family_code = yapily.models.iso_code_details.IsoCodeDetails(
                    code = '0', 
                    name = '0', )
            )
        else :
            return IsoBankTransactionCode(
        )

    def testIsoBankTransactionCode(self):
        """Test IsoBankTransactionCode"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
