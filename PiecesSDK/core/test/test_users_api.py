# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_authenticate_from_oauth_token(self) -> None:
        """Test case for authenticate_from_oauth_token

        /users/authenticate/from_token [POST]  # noqa: E501
        """
        pass

    def test_users_disconnect_user(self) -> None:
        """Test case for users_disconnect_user

        /users/{user}/disconnect [POST]  # noqa: E501
        """
        pass

    def test_users_snapshot(self) -> None:
        """Test case for users_snapshot

        /users [GET]  # noqa: E501
        """
        pass

    def test_users_specific_user_snapshot(self) -> None:
        """Test case for users_specific_user_snapshot

        /users/{user} [GET] Scoped to Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()