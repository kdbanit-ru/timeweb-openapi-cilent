# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api_v1_domains_fqdn_dns_records_record_id import delete  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1DomainsFqdnDnsRecordsRecordId(ApiTestMixin, unittest.TestCase):
    """
    ApiV1DomainsFqdnDnsRecordsRecordId unit test stubs
        Удалить информацию о DNS-записи для домена или поддомена  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
