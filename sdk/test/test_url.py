# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.268
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.url import URL  # noqa: E501
from yapily.rest import ApiException

class TestURL(unittest.TestCase):
    """URL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test URL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.url.URL()  # noqa: E501
        if include_optional :
            return URL(
                authority = '0', 
                content = None, 
                default_port = 56, 
                file = '0', 
                host = '0', 
                path = '0', 
                port = 56, 
                protocol = '0', 
                query = '0', 
                ref = '0', 
                user_info = '0'
            )
        else :
            return URL(
        )

    def testURL(self):
        """Test URL"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
