from openapi_client.paths.api_v1_auth_access_countries.get import ApiForget
from openapi_client.paths.api_v1_auth_access_countries.post import ApiForpost
from openapi_client.paths.api_v1_auth_access_countries.delete import ApiFordelete


class ApiV1AuthAccessCountries(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
