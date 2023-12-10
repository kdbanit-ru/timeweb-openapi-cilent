from openapi_client.paths.api_v1_k8s_clusters_cluster_id.get import ApiForget
from openapi_client.paths.api_v1_k8s_clusters_cluster_id.delete import ApiFordelete
from openapi_client.paths.api_v1_k8s_clusters_cluster_id.patch import ApiForpatch


class ApiV1K8sClustersClusterId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
