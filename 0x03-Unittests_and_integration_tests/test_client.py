#!/usr/bin/env python3
""" test_client.py """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient(unittest.TestCase) """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, url,  mock_get):
        """ test or """
        mock_get.return_value = {}
        cl = GithubOrgClient(org_name)
        info = cl.org
        self.assertEqual(info, {})
        mock_get.assert_called_once_with(url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        payload = {"repos_url": "https://api.github.com/orgs/python/repos"}
        mock_org.return_value = payload
        cl = GithubOrgClient("python")
        self.assertEqual(cl._public_repos_url, payload["repos_url"])
        mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()
