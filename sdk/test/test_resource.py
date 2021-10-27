# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.154.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.resource import Resource  # noqa: E501
from yapily.rest import ApiException

class TestResource(unittest.TestCase):
    """Resource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Resource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.resource.Resource()  # noqa: E501
        if include_optional :
            return Resource(
                description = '0', 
                file = yapily.models.file.File(
                    absolute = True, 
                    absolute_file = yapily.models.file.File(
                        absolute = True, 
                        absolute_path = '0', 
                        canonical_file = yapily.models.file.File(
                            absolute = True, 
                            absolute_path = '0', 
                            canonical_path = '0', 
                            directory = True, 
                            file = True, 
                            free_space = 56, 
                            hidden = True, 
                            name = '0', 
                            parent = '0', 
                            parent_file = yapily.models.file.File(
                                absolute = True, 
                                absolute_path = '0', 
                                canonical_path = '0', 
                                directory = True, 
                                file = True, 
                                free_space = 56, 
                                hidden = True, 
                                name = '0', 
                                parent = '0', 
                                path = '0', 
                                total_space = 56, 
                                usable_space = 56, ), 
                            path = '0', 
                            total_space = 56, 
                            usable_space = 56, ), 
                        canonical_path = '0', 
                        directory = True, 
                        file = True, 
                        free_space = 56, 
                        hidden = True, 
                        name = '0', 
                        parent = '0', 
                        parent_file = yapily.models.file.File(
                            absolute = True, 
                            absolute_path = '0', 
                            canonical_path = '0', 
                            directory = True, 
                            file = True, 
                            free_space = 56, 
                            hidden = True, 
                            name = '0', 
                            parent = '0', 
                            path = '0', 
                            total_space = 56, 
                            usable_space = 56, ), 
                        path = '0', 
                        total_space = 56, 
                        usable_space = 56, ), 
                    absolute_path = '0', 
                    canonical_file = yapily.models.file.File(
                        absolute = True, 
                        absolute_path = '0', 
                        canonical_path = '0', 
                        directory = True, 
                        file = True, 
                        free_space = 56, 
                        hidden = True, 
                        name = '0', 
                        parent = '0', 
                        path = '0', 
                        total_space = 56, 
                        usable_space = 56, ), 
                    canonical_path = '0', 
                    directory = True, 
                    file = True, 
                    free_space = 56, 
                    hidden = True, 
                    name = '0', 
                    parent = '0', 
                    parent_file = yapily.models.file.File(
                        absolute = True, 
                        absolute_path = '0', 
                        canonical_path = '0', 
                        directory = True, 
                        file = True, 
                        free_space = 56, 
                        hidden = True, 
                        name = '0', 
                        parent = '0', 
                        path = '0', 
                        total_space = 56, 
                        usable_space = 56, ), 
                    path = '0', 
                    total_space = 56, 
                    usable_space = 56, ), 
                filename = '0', 
                input_stream = None, 
                open = True, 
                readable = True, 
                uri = yapily.models.uri.URI(
                    absolute = True, 
                    authority = '0', 
                    fragment = '0', 
                    host = '0', 
                    opaque = True, 
                    path = '0', 
                    port = 56, 
                    query = '0', 
                    raw_authority = '0', 
                    raw_fragment = '0', 
                    raw_path = '0', 
                    raw_query = '0', 
                    raw_scheme_specific_part = '0', 
                    raw_user_info = '0', 
                    scheme = '0', 
                    scheme_specific_part = '0', 
                    user_info = '0', ), 
                url = yapily.models.url.URL(
                    authority = '0', 
                    content = yapily.models.content.content(), 
                    default_port = 56, 
                    file = '0', 
                    host = '0', 
                    path = '0', 
                    port = 56, 
                    protocol = '0', 
                    query = '0', 
                    ref = '0', 
                    user_info = '0', )
            )
        else :
            return Resource(
        )

    def testResource(self):
        """Test Resource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
