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
from yapily.model.virtual_account_business_client import VirtualAccountBusinessClient
from yapily.model.virtual_account_client_type import VirtualAccountClientType
from yapily.model.virtual_account_individual_client import VirtualAccountIndividualClient
globals()['VirtualAccountBusinessClient'] = VirtualAccountBusinessClient
globals()['VirtualAccountClientType'] = VirtualAccountClientType
globals()['VirtualAccountIndividualClient'] = VirtualAccountIndividualClient
from yapily.model.virtual_account_client_request import VirtualAccountClientRequest


class TestVirtualAccountClientRequest(unittest.TestCase):
    """VirtualAccountClientRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVirtualAccountClientRequest(self):
        """Test VirtualAccountClientRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VirtualAccountClientRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
