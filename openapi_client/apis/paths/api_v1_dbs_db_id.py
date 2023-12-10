from openapi_client.paths.api_v1_dbs_db_id.get import ApiForget
from openapi_client.paths.api_v1_dbs_db_id.delete import ApiFordelete
from openapi_client.paths.api_v1_dbs_db_id.patch import ApiForpatch


class ApiV1DbsDbId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
