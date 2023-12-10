from openapi_client.paths.api_v1_firewall_groups_group_id.get import ApiForget
from openapi_client.paths.api_v1_firewall_groups_group_id.delete import ApiFordelete
from openapi_client.paths.api_v1_firewall_groups_group_id.patch import ApiForpatch


class ApiV1FirewallGroupsGroupId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
