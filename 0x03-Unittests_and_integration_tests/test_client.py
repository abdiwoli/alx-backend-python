#!/usr/bin/env python3
""" test_client.py """
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


class MockResponse:
    """ moc response class """
    def __init__(self, json_data):
        """ init method """
        self.json_data = json_data

    def json(self):
        """ return json """
        return self.json_data


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


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ test integrations """

    def setUpClass(self):
        """ setup method """
        self.get_patcher = patch('requests.get')
        self.mock_get = cls.get_patcher.start()
        self.mock_get.side_effect = [
            MockResponse(self.org_payload),
            MockResponse(self.repos_payload)
        ]

        def tearDownClass(self):
            """ tear down method """
            self.get_patcher.stop()

        def test_public_repos(cls):
            """ test public """
            client = GithubOrgClient(org_name="google")
            repos = client.public_repos()
            cls.assertEqual(repos, cls.expected_repos)

        def test_public_repos_with_license(cls):
            """ tets public """
            client = GithubOrgClient(org_name="google")
            repos = client.public_repos(license="apache-2.0")
            cls.assertEqual(repos, cls.apache2_repos)


if __name__ == '__main__':
    unittest.main()
