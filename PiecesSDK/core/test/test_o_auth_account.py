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
import datetime

from openapi_client.models.o_auth_account import OAuthAccount  # noqa: E501

class TestOAuthAccount(unittest.TestCase):
    """OAuthAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuthAccount:
        """Test OAuthAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuthAccount`
        """
        model = OAuthAccount()  # noqa: E501
        if include_optional:
            return OAuthAccount(
                client_id = '0',
                email = '0',
                connection = '0',
                username = '0',
                given_name = '0',
                family_name = '0',
                name = '0',
                picture = '0',
                nickname = '0'
            )
        else:
            return OAuthAccount(
                client_id = '0',
                email = '0',
                connection = '0',
                username = '0',
                given_name = '0',
                family_name = '0',
                name = '0',
                picture = '0',
                nickname = '0',
        )
        """

    def testOAuthAccount(self):
        """Test OAuthAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()