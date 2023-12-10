from openapi_client.paths.api_v1_servers_server_id.get import ApiForget
from openapi_client.paths.api_v1_servers_server_id.delete import ApiFordelete
from openapi_client.paths.api_v1_servers_server_id.patch import ApiForpatch


class ApiV1ServersServerId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
