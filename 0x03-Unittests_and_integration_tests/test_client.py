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
        """ test public """
        payload = {"repos_url": "https://api.github.com/orgs/python/repos"}
        mock_org.return_value = payload
        cl = GithubOrgClient("python")
        self.assertEqual(cl._public_repos_url, payload["repos_url"])
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """ Test public repos """
        repos_payload = [
            {"name": "python"},
            {"name": "java"},
            {"name": "c"}
        ]
        mock_get.return_value = repos_payload
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as repos_url:
            repos_url.return_value = "https://api.github.com/orgs/test/repos"
            cl = GithubOrgClient("test")
            result = cl.public_repos()
            expected_repos = ["python", "java", "c"]
            self.assertEqual(result, expected_repos)
            repos_url.assert_called_once()
            url = "https://api.github.com/orgs/test/repos"
            mock_get.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, ex_result):
        """ check license """
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, ex_result)


if __name__ == '__main__':
    unittest.main()
