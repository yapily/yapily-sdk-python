# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.138.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.application_users_api import ApplicationUsersApi  # noqa: E501
from yapily.rest import ApiException


class TestApplicationUsersApi(unittest.TestCase):
    """ApplicationUsersApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.application_users_api.ApplicationUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_using_post(self):
        """Test case for add_user_using_post

        Add an application user  # noqa: E501
        """
        pass

    def test_delete_user_using_delete(self):
        """Test case for delete_user_using_delete

        Delete an application user and sub-resources (including consent resources on institution APIs if they exist)  # noqa: E501
        """
        pass

    def test_get_delete_users_job_using_get(self):
        """Test case for get_delete_users_job_using_get

        Get details of a user deletion job  # noqa: E501
        """
        pass

    def test_get_delete_users_jobs_using_get(self):
        """Test case for get_delete_users_jobs_using_get

        Get details of all user deletion jobs  # noqa: E501
        """
        pass

    def test_get_user_using_get(self):
        """Test case for get_user_using_get

        Get an application user  # noqa: E501
        """
        pass

    def test_get_users_using_get(self):
        """Test case for get_users_using_get

        Get application users  # noqa: E501
        """
        pass

    def test_start_delete_users_job_using_post(self):
        """Test case for start_delete_users_job_using_post

        Start a job to delete application users by specifying their identifiers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
