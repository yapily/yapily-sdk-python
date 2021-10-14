# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.127.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_of_ssa_result import ApiResponseOfSSAResult  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfSSAResult(unittest.TestCase):
    """ApiResponseOfSSAResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfSSAResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_ssa_result.ApiResponseOfSSAResult()  # noqa: E501
        if include_optional :
            return ApiResponseOfSSAResult(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = yapily.models.ssa_result.SSAResult(
                    application_id = '0', 
                    institution_id = '0', 
                    ssa_jwt = '0', ), 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiResponseOfSSAResult(
        )

    def testApiResponseOfSSAResult(self):
        """Test ApiResponseOfSSAResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
