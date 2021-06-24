# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.359
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_list_response_of_institution import ApiListResponseOfInstitution  # noqa: E501
from yapily.rest import ApiException

class TestApiListResponseOfInstitution(unittest.TestCase):
    """ApiListResponseOfInstitution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiListResponseOfInstitution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_list_response_of_institution.ApiListResponseOfInstitution()  # noqa: E501
        if include_optional :
            return ApiListResponseOfInstitution(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '0', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        next = yapily.models.next.Next(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, ), 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            offset = 56, 
                            sort = 'date', ), 
                        total_count = 56, ), ), 
                data = [
                    yapily.models.institution.Institution(
                        id = '0', 
                        name = '0', 
                        full_name = '0', 
                        countries = [
                            yapily.models.country.Country(
                                country_code2 = '0', 
                                display_name = '0', )
                            ], 
                        environment_type = 'SANDBOX', 
                        credentials_type = 'OAUTH1', 
                        media = [
                            yapily.models.media.Media(
                                source = '0', 
                                type = '0', )
                            ], 
                        features = [
                            'INITIATE_PRE_AUTHORISATION'
                            ], 
                        monitoring = {
                            'key' : yapily.models.monitoring_feature_status.MonitoringFeatureStatus(
                                last_tested = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                span = '0', 
                                status = 'Up', )
                            }, )
                    ], 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiListResponseOfInstitution(
        )

    def testApiListResponseOfInstitution(self):
        """Test ApiListResponseOfInstitution"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
