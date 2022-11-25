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
from yapily.model.links import Links
from yapily.model.response_forwarded_data import ResponseForwardedData
from yapily.model.response_list_meta import ResponseListMeta
from yapily.model.virtual_account_payment import VirtualAccountPayment
globals()['Links'] = Links
globals()['ResponseForwardedData'] = ResponseForwardedData
globals()['ResponseListMeta'] = ResponseListMeta
globals()['VirtualAccountPayment'] = VirtualAccountPayment
from yapily.model.api_list_response_of_virtual_account_payment import ApiListResponseOfVirtualAccountPayment


class TestApiListResponseOfVirtualAccountPayment(unittest.TestCase):
    """ApiListResponseOfVirtualAccountPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiListResponseOfVirtualAccountPayment(self):
        """Test ApiListResponseOfVirtualAccountPayment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiListResponseOfVirtualAccountPayment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
