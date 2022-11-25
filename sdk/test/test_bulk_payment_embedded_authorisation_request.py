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
from yapily.model.bulk_payment_request import BulkPaymentRequest
from yapily.model.redirect_request import RedirectRequest
from yapily.model.sca_method import ScaMethod
from yapily.model.user_credentials import UserCredentials
globals()['BulkPaymentRequest'] = BulkPaymentRequest
globals()['RedirectRequest'] = RedirectRequest
globals()['ScaMethod'] = ScaMethod
globals()['UserCredentials'] = UserCredentials
from yapily.model.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest


class TestBulkPaymentEmbeddedAuthorisationRequest(unittest.TestCase):
    """BulkPaymentEmbeddedAuthorisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBulkPaymentEmbeddedAuthorisationRequest(self):
        """Test BulkPaymentEmbeddedAuthorisationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BulkPaymentEmbeddedAuthorisationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
