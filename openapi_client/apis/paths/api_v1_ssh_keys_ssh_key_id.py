from openapi_client.paths.api_v1_ssh_keys_ssh_key_id.get import ApiForget
from openapi_client.paths.api_v1_ssh_keys_ssh_key_id.delete import ApiFordelete
from openapi_client.paths.api_v1_ssh_keys_ssh_key_id.patch import ApiForpatch


class ApiV1SshKeysSshKeyId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
