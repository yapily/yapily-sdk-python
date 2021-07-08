# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.363
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.ssa_result import SSAResult  # noqa: E501
from yapily.rest import ApiException

class TestSSAResult(unittest.TestCase):
    """SSAResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SSAResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.ssa_result.SSAResult()  # noqa: E501
        if include_optional :
            return SSAResult(
                application_id = '0', 
                institution_id = '0', 
                ssa_jwt = '0'
            )
        else :
            return SSAResult(
        )

    def testSSAResult(self):
        """Test SSAResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
