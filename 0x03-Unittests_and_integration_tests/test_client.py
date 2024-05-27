#!/usr/bin/env python3
""" test_client.py """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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


if __name__ == '__main__':
    unittest.main()
