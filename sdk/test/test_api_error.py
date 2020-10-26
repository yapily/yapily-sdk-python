# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.264
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_error import ApiError  # noqa: E501
from yapily.rest import ApiException

class TestApiError(unittest.TestCase):
    """ApiError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_error.ApiError()  # noqa: E501
        if include_optional :
            return ApiError(
                code = 56, 
                institution_error = yapily.models.institution_error.InstitutionError(
                    error_message = '0', 
                    http_status_code = 56, ), 
                message = '0', 
                source = '0', 
                status = '400', 
                tracing_id = '0'
            )
        else :
            return ApiError(
        )

    def testApiError(self):
        """Test ApiError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
