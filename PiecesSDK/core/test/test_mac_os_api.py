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

from openapi_client.api.mac_os_api import MacOSApi  # noqa: E501


class TestMacOSApi(unittest.TestCase):
    """MacOSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MacOSApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_assets_create_new_asset_from_macos(self) -> None:
        """Test case for assets_create_new_asset_from_macos

        /macos/assets/create [Post]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()