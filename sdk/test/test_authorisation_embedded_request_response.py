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
from yapily.models.authorisation_embedded_request_response import AuthorisationEmbeddedRequestResponse  # noqa: E501
from yapily.rest import ApiException

class TestAuthorisationEmbeddedRequestResponse(unittest.TestCase):
    """AuthorisationEmbeddedRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthorisationEmbeddedRequestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.authorisation_embedded_request_response.AuthorisationEmbeddedRequestResponse()  # noqa: E501
        if include_optional :
            return AuthorisationEmbeddedRequestResponse(
                id = '0', 
                user_uuid = '0', 
                application_user_id = '0', 
                reference_id = '0', 
                institution_id = '0', 
                status = 'AWAITING_AUTHORIZATION', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                transaction_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                transaction_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_to_expire_in_millis = 56, 
                time_to_expire = '0', 
                feature_scope = [
                    'INITIATE_PRE_AUTHORISATION'
                    ], 
                authorisation_url = '0', 
                consent_token = '0', 
                qr_code_url = '0', 
                sca_methods = [
                    yapily.models.sca_method.ScaMethod(
                        id = '0', 
                        type = 'SMS_OTP', 
                        description = '0', )
                    ], 
                state = '0', 
                selected_sca_method = yapily.models.sca_method.ScaMethod(
                    id = '0', 
                    type = 'SMS_OTP', 
                    description = '0', ), 
                authorized_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                institution_consent_id = '0'
            )
        else :
            return AuthorisationEmbeddedRequestResponse(
        )

    def testAuthorisationEmbeddedRequestResponse(self):
        """Test AuthorisationEmbeddedRequestResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
