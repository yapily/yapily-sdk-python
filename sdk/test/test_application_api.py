"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.15.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import yapily
from yapily.api.application_api import ApplicationApi  # noqa: E501


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_application_me(self):
        """Test case for get_application_me

        Get Application Self  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
