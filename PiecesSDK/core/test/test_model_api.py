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

from openapi_client.api.model_api import ModelApi  # noqa: E501


class TestModelApi(unittest.TestCase):
    """ModelApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModelApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_model_specific_model_download(self) -> None:
        """Test case for model_specific_model_download

        /model/{model}/download [POST]  # noqa: E501
        """
        pass

    def test_model_specific_model_download_cancel(self) -> None:
        """Test case for model_specific_model_download_cancel

        /model/{model}/download/cancel [POST]  # noqa: E501
        """
        pass

    def test_model_specific_model_download_progress(self) -> None:
        """Test case for model_specific_model_download_progress

        /model/{model}/download/progress [WS]  # noqa: E501
        """
        pass

    def test_model_specific_model_load(self) -> None:
        """Test case for model_specific_model_load

        /model/{model}/load [POST]  # noqa: E501
        """
        pass

    def test_model_specific_model_unload(self) -> None:
        """Test case for model_specific_model_unload

        /model/{model}/unload [POST]  # noqa: E501
        """
        pass

    def test_model_update(self) -> None:
        """Test case for model_update

        /model/update [POST]  # noqa: E501
        """
        pass

    def test_models_specific_model_snapshot(self) -> None:
        """Test case for models_specific_model_snapshot

        /model/{model} [GET]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()