# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.203
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.iso_code_details import IsoCodeDetails  # noqa: E501
from yapily.rest import ApiException

class TestIsoCodeDetails(unittest.TestCase):
    """IsoCodeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IsoCodeDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.iso_code_details.IsoCodeDetails()  # noqa: E501
        if include_optional :
            return IsoCodeDetails(
                code = '0', 
                name = '0'
            )
        else :
            return IsoCodeDetails(
        )

    def testIsoCodeDetails(self):
        """Test IsoCodeDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
