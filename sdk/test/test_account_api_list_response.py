"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.15.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import yapily
from yapily.model.account import Account
from yapily.model.filtered_client_payload_list_account import FilteredClientPayloadListAccount
from yapily.model.raw_response import RawResponse
from yapily.model.response_forwarded_data import ResponseForwardedData
from yapily.model.response_list_meta import ResponseListMeta
globals()['Account'] = Account
globals()['FilteredClientPayloadListAccount'] = FilteredClientPayloadListAccount
globals()['RawResponse'] = RawResponse
globals()['ResponseForwardedData'] = ResponseForwardedData
globals()['ResponseListMeta'] = ResponseListMeta
from yapily.model.account_api_list_response import AccountApiListResponse


class TestAccountApiListResponse(unittest.TestCase):
    """AccountApiListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountApiListResponse(self):
        """Test AccountApiListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountApiListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
