"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import yapily
from yapily.model.non_sweeping_authorisation_response import NonSweepingAuthorisationResponse
from yapily.model.response_forwarded_data import ResponseForwardedData
from yapily.model.response_meta import ResponseMeta
globals()['NonSweepingAuthorisationResponse'] = NonSweepingAuthorisationResponse
globals()['ResponseForwardedData'] = ResponseForwardedData
globals()['ResponseMeta'] = ResponseMeta
from yapily.model.api_response_of_non_sweeping_authorisation_response import ApiResponseOfNonSweepingAuthorisationResponse


class TestApiResponseOfNonSweepingAuthorisationResponse(unittest.TestCase):
    """ApiResponseOfNonSweepingAuthorisationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiResponseOfNonSweepingAuthorisationResponse(self):
        """Test ApiResponseOfNonSweepingAuthorisationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiResponseOfNonSweepingAuthorisationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
