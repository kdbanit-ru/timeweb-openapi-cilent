from openapi_client.paths.api_v1_dedicated_servers_dedicated_id.get import ApiForget
from openapi_client.paths.api_v1_dedicated_servers_dedicated_id.delete import ApiFordelete
from openapi_client.paths.api_v1_dedicated_servers_dedicated_id.patch import ApiForpatch


class ApiV1DedicatedServersDedicatedId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
