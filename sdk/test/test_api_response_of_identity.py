# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.120.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_of_identity import ApiResponseOfIdentity  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfIdentity(unittest.TestCase):
    """ApiResponseOfIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfIdentity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_identity.ApiResponseOfIdentity()  # noqa: E501
        if include_optional :
            return ApiResponseOfIdentity(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = yapily.models.identity.Identity(
                    id = '0', 
                    first_name = '0', 
                    last_name = '0', 
                    full_name = '0', 
                    gender = '0', 
                    birthdate = '0', 
                    email = '0', 
                    phone = '0', 
                    addresses = [
                        yapily.models.identity_address.IdentityAddress(
                            address_lines = [
                                '0'
                                ], 
                            city = '0', 
                            postal_code = '0', 
                            country = '0', 
                            street_name = '0', 
                            building_number = '0', 
                            type = 'BUSINESS', 
                            county = '0', )
                        ], ), 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiResponseOfIdentity(
        )

    def testApiResponseOfIdentity(self):
        """Test ApiResponseOfIdentity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
