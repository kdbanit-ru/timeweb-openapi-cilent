from openapi_client.paths.api_v1_images_image_id.get import ApiForget
from openapi_client.paths.api_v1_images_image_id.post import ApiForpost
from openapi_client.paths.api_v1_images_image_id.delete import ApiFordelete
from openapi_client.paths.api_v1_images_image_id.patch import ApiForpatch


class ApiV1ImagesImageId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
