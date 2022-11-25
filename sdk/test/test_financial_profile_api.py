"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.15.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import yapily
from yapily.api.financial_profile_api import FinancialProfileApi  # noqa: E501


class TestFinancialProfileApi(unittest.TestCase):
    """FinancialProfileApi unit test stubs"""

    def setUp(self):
        self.api = FinancialProfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_profile_consent(self):
        """Test case for create_profile_consent

        Create Profile Consent  # noqa: E501
        """
        pass

    def test_delete_profile_consent(self):
        """Test case for delete_profile_consent

        Delete Profile Consent  # noqa: E501
        """
        pass

    def test_get_balance_prediction(self):
        """Test case for get_balance_prediction

        Get Predicted Balances  # noqa: E501
        """
        pass

    def test_get_profile_consent(self):
        """Test case for get_profile_consent

        Get Profile Consent  # noqa: E501
        """
        pass

    def test_get_user_profile(self):
        """Test case for get_user_profile

        Get User Profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
