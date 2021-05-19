# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.345
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.transfer_request import TransferRequest  # noqa: E501
from yapily.rest import ApiException

class TestTransferRequest(unittest.TestCase):
    """TransferRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransferRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.transfer_request.TransferRequest()  # noqa: E501
        if include_optional :
            return TransferRequest(
                account_id = '0', 
                amount = 1.337, 
                currency = '0', 
                reference = '0', 
                transfer_reference_id = '0'
            )
        else :
            return TransferRequest(
        )

    def testTransferRequest(self):
        """Test TransferRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
