from openapi_client.paths.api_v1_domains_fqdn.get import ApiForget
from openapi_client.paths.api_v1_domains_fqdn.delete import ApiFordelete
from openapi_client.paths.api_v1_domains_fqdn.patch import ApiForpatch


class ApiV1DomainsFqdn(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
