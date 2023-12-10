import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_v1_account_finances import ApiV1AccountFinances
from openapi_client.apis.paths.api_v1_account_status import ApiV1AccountStatus
from openapi_client.apis.paths.api_v1_account_notification_settings import ApiV1AccountNotificationSettings
from openapi_client.apis.paths.api_v1_images import ApiV1Images
from openapi_client.apis.paths.api_v1_images_image_id import ApiV1ImagesImageId
from openapi_client.apis.paths.api_v1_images_image_id_download_url import ApiV1ImagesImageIdDownloadUrl
from openapi_client.apis.paths.api_v1_images_image_id_download_url_image_url_id import ApiV1ImagesImageIdDownloadUrlImageUrlId
from openapi_client.apis.paths.api_v1_firewall_groups import ApiV1FirewallGroups
from openapi_client.apis.paths.api_v1_firewall_groups_group_id import ApiV1FirewallGroupsGroupId
from openapi_client.apis.paths.api_v1_firewall_groups_group_id_resources import ApiV1FirewallGroupsGroupIdResources
from openapi_client.apis.paths.api_v1_firewall_groups_group_id_resources_resource_id import ApiV1FirewallGroupsGroupIdResourcesResourceId
from openapi_client.apis.paths.api_v1_firewall_groups_group_id_rules import ApiV1FirewallGroupsGroupIdRules
from openapi_client.apis.paths.api_v1_firewall_groups_group_id_rules_rule_id import ApiV1FirewallGroupsGroupIdRulesRuleId
from openapi_client.apis.paths.api_v1_firewall_service_resource_type_resource_id import ApiV1FirewallServiceResourceTypeResourceId
from openapi_client.apis.paths.api_v1_balancers import ApiV1Balancers
from openapi_client.apis.paths.api_v1_balancers_balancer_id import ApiV1BalancersBalancerId
from openapi_client.apis.paths.api_v1_balancers_balancer_id_ips import ApiV1BalancersBalancerIdIps
from openapi_client.apis.paths.api_v1_balancers_balancer_id_rules import ApiV1BalancersBalancerIdRules
from openapi_client.apis.paths.api_v1_balancers_balancer_id_rules_rule_id import ApiV1BalancersBalancerIdRulesRuleId
from openapi_client.apis.paths.api_v1_presets_balancers import ApiV1PresetsBalancers
from openapi_client.apis.paths.api_v1_databases import ApiV1Databases
from openapi_client.apis.paths.api_v1_databases_db_cluster_id import ApiV1DatabasesDbClusterId
from openapi_client.apis.paths.api_v1_databases_db_cluster_id_admins import ApiV1DatabasesDbClusterIdAdmins
from openapi_client.apis.paths.api_v1_databases_db_cluster_id_admins_admin_id import ApiV1DatabasesDbClusterIdAdminsAdminId
from openapi_client.apis.paths.api_v1_databases_db_cluster_id_instances import ApiV1DatabasesDbClusterIdInstances
from openapi_client.apis.paths.api_v1_databases_db_cluster_id_instances_instance_id import ApiV1DatabasesDbClusterIdInstancesInstanceId
from openapi_client.apis.paths.api_v1_dbs import ApiV1Dbs
from openapi_client.apis.paths.api_v1_dbs_db_id import ApiV1DbsDbId
from openapi_client.apis.paths.api_v1_dbs_db_id_auto_backups import ApiV1DbsDbIdAutoBackups
from openapi_client.apis.paths.api_v1_dbs_db_id_backups import ApiV1DbsDbIdBackups
from openapi_client.apis.paths.api_v1_dbs_db_id_backups_backup_id import ApiV1DbsDbIdBackupsBackupId
from openapi_client.apis.paths.api_v1_presets_dbs import ApiV1PresetsDbs
from openapi_client.apis.paths.api_v1_dedicated_servers import ApiV1DedicatedServers
from openapi_client.apis.paths.api_v1_dedicated_servers_dedicated_id import ApiV1DedicatedServersDedicatedId
from openapi_client.apis.paths.api_v1_presets_dedicated_servers import ApiV1PresetsDedicatedServers
from openapi_client.apis.paths.api_v1_presets_dedicated_servers_preset_id_additional_services import ApiV1PresetsDedicatedServersPresetIdAdditionalServices
from openapi_client.apis.paths.api_v1_k8s_clusters import ApiV1K8sClusters
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id import ApiV1K8sClustersClusterId
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_resources import ApiV1K8sClustersClusterIdResources
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_kubeconfig import ApiV1K8sClustersClusterIdKubeconfig
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_groups import ApiV1K8sClustersClusterIdGroups
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_groups_group_id import ApiV1K8sClustersClusterIdGroupsGroupId
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_groups_group_id_nodes import ApiV1K8sClustersClusterIdGroupsGroupIdNodes
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_nodes import ApiV1K8sClustersClusterIdNodes
from openapi_client.apis.paths.api_v1_k8s_clusters_cluster_id_nodes_node_id import ApiV1K8sClustersClusterIdNodesNodeId
from openapi_client.apis.paths.api_v1_k8s_k8s_versions import ApiV1K8sK8sVersions
from openapi_client.apis.paths.api_v1_k8s_network_drivers import ApiV1K8sNetworkDrivers
from openapi_client.apis.paths.api_v1_presets_k8s import ApiV1PresetsK8s
from openapi_client.apis.paths.api_v1_servers import ApiV1Servers
from openapi_client.apis.paths.api_v1_servers_server_id import ApiV1ServersServerId
from openapi_client.apis.paths.api_v1_servers_server_id_action import ApiV1ServersServerIdAction
from openapi_client.apis.paths.api_v1_servers_server_id_clone import ApiV1ServersServerIdClone
from openapi_client.apis.paths.api_v1_servers_server_id_statistics import ApiV1ServersServerIdStatistics
from openapi_client.apis.paths.api_v1_os_servers import ApiV1OsServers
from openapi_client.apis.paths.api_v1_presets_servers import ApiV1PresetsServers
from openapi_client.apis.paths.api_v1_configurator_servers import ApiV1ConfiguratorServers
from openapi_client.apis.paths.api_v1_software_servers import ApiV1SoftwareServers
from openapi_client.apis.paths.api_v1_servers_server_id_boot_mode import ApiV1ServersServerIdBootMode
from openapi_client.apis.paths.api_v1_servers_server_id_local_networks_nat_mode import ApiV1ServersServerIdLocalNetworksNatMode
from openapi_client.apis.paths.api_v1_servers_server_id_ips import ApiV1ServersServerIdIps
from openapi_client.apis.paths.api_v1_servers_server_id_logs import ApiV1ServersServerIdLogs
from openapi_client.apis.paths.api_v1_servers_server_id_disks import ApiV1ServersServerIdDisks
from openapi_client.apis.paths.api_v1_servers_server_id_disks_disk_id import ApiV1ServersServerIdDisksDiskId
from openapi_client.apis.paths.api_v1_servers_server_id_disks_disk_id_auto_backups import ApiV1ServersServerIdDisksDiskIdAutoBackups
from openapi_client.apis.paths.api_v1_servers_server_id_disks_disk_id_backups import ApiV1ServersServerIdDisksDiskIdBackups
from openapi_client.apis.paths.api_v1_servers_server_id_disks_disk_id_backups_backup_id import ApiV1ServersServerIdDisksDiskIdBackupsBackupId
from openapi_client.apis.paths.api_v1_servers_server_id_disks_disk_id_backups_backup_id_action import ApiV1ServersServerIdDisksDiskIdBackupsBackupIdAction
from openapi_client.apis.paths.api_v1_servers_server_id_image_unmount import ApiV1ServersServerIdImageUnmount
from openapi_client.apis.paths.api_v1_projects import ApiV1Projects
from openapi_client.apis.paths.api_v1_projects_project_id import ApiV1ProjectsProjectId
from openapi_client.apis.paths.api_v1_projects_project_id_resources_balancers import ApiV1ProjectsProjectIdResourcesBalancers
from openapi_client.apis.paths.api_v1_projects_project_id_resources_buckets import ApiV1ProjectsProjectIdResourcesBuckets
from openapi_client.apis.paths.api_v1_projects_project_id_resources_clusters import ApiV1ProjectsProjectIdResourcesClusters
from openapi_client.apis.paths.api_v1_projects_project_id_resources_servers import ApiV1ProjectsProjectIdResourcesServers
from openapi_client.apis.paths.api_v1_projects_project_id_resources_databases import ApiV1ProjectsProjectIdResourcesDatabases
from openapi_client.apis.paths.api_v1_projects_project_id_resources_dedicated import ApiV1ProjectsProjectIdResourcesDedicated
from openapi_client.apis.paths.api_v1_projects_project_id_resources import ApiV1ProjectsProjectIdResources
from openapi_client.apis.paths.api_v1_projects_resources_balancers import ApiV1ProjectsResourcesBalancers
from openapi_client.apis.paths.api_v1_projects_resources_servers import ApiV1ProjectsResourcesServers
from openapi_client.apis.paths.api_v1_projects_resources_buckets import ApiV1ProjectsResourcesBuckets
from openapi_client.apis.paths.api_v1_projects_resources_clusters import ApiV1ProjectsResourcesClusters
from openapi_client.apis.paths.api_v1_projects_resources_databases import ApiV1ProjectsResourcesDatabases
from openapi_client.apis.paths.api_v1_projects_resources_dedicated import ApiV1ProjectsResourcesDedicated
from openapi_client.apis.paths.api_v1_projects_project_id_resources_transfer import ApiV1ProjectsProjectIdResourcesTransfer
from openapi_client.apis.paths.api_v1_storages_buckets import ApiV1StoragesBuckets
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id import ApiV1StoragesBucketsBucketId
from openapi_client.apis.paths.api_v1_presets_storages import ApiV1PresetsStorages
from openapi_client.apis.paths.api_v1_storages_users import ApiV1StoragesUsers
from openapi_client.apis.paths.api_v1_storages_users_user_id import ApiV1StoragesUsersUserId
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_transfer_status import ApiV1StoragesBucketsBucketIdTransferStatus
from openapi_client.apis.paths.api_v1_storages_transfer import ApiV1StoragesTransfer
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_subdomains import ApiV1StoragesBucketsBucketIdSubdomains
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_list import ApiV1StoragesBucketsBucketIdObjectManagerList
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_rename import ApiV1StoragesBucketsBucketIdObjectManagerRename
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_remove import ApiV1StoragesBucketsBucketIdObjectManagerRemove
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_copy import ApiV1StoragesBucketsBucketIdObjectManagerCopy
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_upload import ApiV1StoragesBucketsBucketIdObjectManagerUpload
from openapi_client.apis.paths.api_v1_storages_buckets_bucket_id_object_manager_mkdir import ApiV1StoragesBucketsBucketIdObjectManagerMkdir
from openapi_client.apis.paths.api_v1_storages_certificates_generate import ApiV1StoragesCertificatesGenerate
from openapi_client.apis.paths.api_v1_auth_api_keys import ApiV1AuthApiKeys
from openapi_client.apis.paths.api_v1_auth_api_keys_token_id import ApiV1AuthApiKeysTokenId
from openapi_client.apis.paths.api_v1_auth_access import ApiV1AuthAccess
from openapi_client.apis.paths.api_v1_auth_access_countries_enabled import ApiV1AuthAccessCountriesEnabled
from openapi_client.apis.paths.api_v1_auth_access_countries import ApiV1AuthAccessCountries
from openapi_client.apis.paths.api_v1_auth_access_ips_enabled import ApiV1AuthAccessIpsEnabled
from openapi_client.apis.paths.api_v1_auth_access_ips import ApiV1AuthAccessIps
from openapi_client.apis.paths.api_v1_mail import ApiV1Mail
from openapi_client.apis.paths.api_v1_mail_quota import ApiV1MailQuota
from openapi_client.apis.paths.api_v1_mail_domains_domain import ApiV1MailDomainsDomain
from openapi_client.apis.paths.api_v1_mail_domains_domain_info import ApiV1MailDomainsDomainInfo
from openapi_client.apis.paths.api_v1_mail_domains_domain_mailboxes_mailbox import ApiV1MailDomainsDomainMailboxesMailbox
from openapi_client.apis.paths.api_v1_domains import ApiV1Domains
from openapi_client.apis.paths.api_v1_domains_fqdn import ApiV1DomainsFqdn
from openapi_client.apis.paths.api_v1_domains_fqdn_dns_records import ApiV1DomainsFqdnDnsRecords
from openapi_client.apis.paths.api_v1_domains_fqdn_dns_records_record_id import ApiV1DomainsFqdnDnsRecordsRecordId
from openapi_client.apis.paths.api_v1_domains_fqdn_default_dns_records import ApiV1DomainsFqdnDefaultDnsRecords
from openapi_client.apis.paths.api_v1_domains_fqdn_subdomains_subdomain_fqdn import ApiV1DomainsFqdnSubdomainsSubdomainFqdn
from openapi_client.apis.paths.api_v1_domains_fqdn_name_servers import ApiV1DomainsFqdnNameServers
from openapi_client.apis.paths.api_v1_domains_requests import ApiV1DomainsRequests
from openapi_client.apis.paths.api_v1_domains_requests_request_id import ApiV1DomainsRequestsRequestId
from openapi_client.apis.paths.api_v1_tlds import ApiV1Tlds
from openapi_client.apis.paths.api_v1_tlds_tld_id import ApiV1TldsTldId
from openapi_client.apis.paths.api_v1_check_domain_fqdn import ApiV1CheckDomainFqdn
from openapi_client.apis.paths.api_v1_add_domain_fqdn import ApiV1AddDomainFqdn
from openapi_client.apis.paths.api_v2_vpcs import ApiV2Vpcs
from openapi_client.apis.paths.api_v2_vpcs_vpc_id import ApiV2VpcsVpcId
from openapi_client.apis.paths.api_v2_vpcs_vpc_id_services import ApiV2VpcsVpcIdServices
from openapi_client.apis.paths.api_v1_vpcs_vpc_id import ApiV1VpcsVpcId
from openapi_client.apis.paths.api_v1_vpcs_vpc_id_ports import ApiV1VpcsVpcIdPorts
from openapi_client.apis.paths.api_v1_ssh_keys import ApiV1SshKeys
from openapi_client.apis.paths.api_v1_ssh_keys_ssh_key_id import ApiV1SshKeysSshKeyId
from openapi_client.apis.paths.api_v1_servers_server_id_ssh_keys import ApiV1ServersServerIdSshKeys
from openapi_client.apis.paths.api_v1_servers_server_id_ssh_keys_ssh_key_id import ApiV1ServersServerIdSshKeysSshKeyId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_ACCOUNT_FINANCES: ApiV1AccountFinances,
        PathValues.API_V1_ACCOUNT_STATUS: ApiV1AccountStatus,
        PathValues.API_V1_ACCOUNT_NOTIFICATIONSETTINGS: ApiV1AccountNotificationSettings,
        PathValues.API_V1_IMAGES: ApiV1Images,
        PathValues.API_V1_IMAGES_IMAGE_ID: ApiV1ImagesImageId,
        PathValues.API_V1_IMAGES_IMAGE_ID_DOWNLOADURL: ApiV1ImagesImageIdDownloadUrl,
        PathValues.API_V1_IMAGES_IMAGE_ID_DOWNLOADURL_IMAGE_URL_ID: ApiV1ImagesImageIdDownloadUrlImageUrlId,
        PathValues.API_V1_FIREWALL_GROUPS: ApiV1FirewallGroups,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID: ApiV1FirewallGroupsGroupId,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES: ApiV1FirewallGroupsGroupIdResources,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES_RESOURCE_ID: ApiV1FirewallGroupsGroupIdResourcesResourceId,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RULES: ApiV1FirewallGroupsGroupIdRules,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RULES_RULE_ID: ApiV1FirewallGroupsGroupIdRulesRuleId,
        PathValues.API_V1_FIREWALL_SERVICE_RESOURCE_TYPE_RESOURCE_ID: ApiV1FirewallServiceResourceTypeResourceId,
        PathValues.API_V1_BALANCERS: ApiV1Balancers,
        PathValues.API_V1_BALANCERS_BALANCER_ID: ApiV1BalancersBalancerId,
        PathValues.API_V1_BALANCERS_BALANCER_ID_IPS: ApiV1BalancersBalancerIdIps,
        PathValues.API_V1_BALANCERS_BALANCER_ID_RULES: ApiV1BalancersBalancerIdRules,
        PathValues.API_V1_BALANCERS_BALANCER_ID_RULES_RULE_ID: ApiV1BalancersBalancerIdRulesRuleId,
        PathValues.API_V1_PRESETS_BALANCERS: ApiV1PresetsBalancers,
        PathValues.API_V1_DATABASES: ApiV1Databases,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID: ApiV1DatabasesDbClusterId,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_ADMINS: ApiV1DatabasesDbClusterIdAdmins,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_ADMINS_ADMIN_ID: ApiV1DatabasesDbClusterIdAdminsAdminId,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES: ApiV1DatabasesDbClusterIdInstances,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES_INSTANCE_ID: ApiV1DatabasesDbClusterIdInstancesInstanceId,
        PathValues.API_V1_DBS: ApiV1Dbs,
        PathValues.API_V1_DBS_DB_ID: ApiV1DbsDbId,
        PathValues.API_V1_DBS_DB_ID_AUTOBACKUPS: ApiV1DbsDbIdAutoBackups,
        PathValues.API_V1_DBS_DB_ID_BACKUPS: ApiV1DbsDbIdBackups,
        PathValues.API_V1_DBS_DB_ID_BACKUPS_BACKUP_ID: ApiV1DbsDbIdBackupsBackupId,
        PathValues.API_V1_PRESETS_DBS: ApiV1PresetsDbs,
        PathValues.API_V1_DEDICATEDSERVERS: ApiV1DedicatedServers,
        PathValues.API_V1_DEDICATEDSERVERS_DEDICATED_ID: ApiV1DedicatedServersDedicatedId,
        PathValues.API_V1_PRESETS_DEDICATEDSERVERS: ApiV1PresetsDedicatedServers,
        PathValues.API_V1_PRESETS_DEDICATEDSERVERS_PRESET_ID_ADDITIONALSERVICES: ApiV1PresetsDedicatedServersPresetIdAdditionalServices,
        PathValues.API_V1_K8S_CLUSTERS: ApiV1K8sClusters,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID: ApiV1K8sClustersClusterId,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_RESOURCES: ApiV1K8sClustersClusterIdResources,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_KUBECONFIG: ApiV1K8sClustersClusterIdKubeconfig,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS: ApiV1K8sClustersClusterIdGroups,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID: ApiV1K8sClustersClusterIdGroupsGroupId,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID_NODES: ApiV1K8sClustersClusterIdGroupsGroupIdNodes,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES: ApiV1K8sClustersClusterIdNodes,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES_NODE_ID: ApiV1K8sClustersClusterIdNodesNodeId,
        PathValues.API_V1_K8S_K8S_VERSIONS: ApiV1K8sK8sVersions,
        PathValues.API_V1_K8S_NETWORK_DRIVERS: ApiV1K8sNetworkDrivers,
        PathValues.API_V1_PRESETS_K8S: ApiV1PresetsK8s,
        PathValues.API_V1_SERVERS: ApiV1Servers,
        PathValues.API_V1_SERVERS_SERVER_ID: ApiV1ServersServerId,
        PathValues.API_V1_SERVERS_SERVER_ID_ACTION: ApiV1ServersServerIdAction,
        PathValues.API_V1_SERVERS_SERVER_ID_CLONE: ApiV1ServersServerIdClone,
        PathValues.API_V1_SERVERS_SERVER_ID_STATISTICS: ApiV1ServersServerIdStatistics,
        PathValues.API_V1_OS_SERVERS: ApiV1OsServers,
        PathValues.API_V1_PRESETS_SERVERS: ApiV1PresetsServers,
        PathValues.API_V1_CONFIGURATOR_SERVERS: ApiV1ConfiguratorServers,
        PathValues.API_V1_SOFTWARE_SERVERS: ApiV1SoftwareServers,
        PathValues.API_V1_SERVERS_SERVER_ID_BOOTMODE: ApiV1ServersServerIdBootMode,
        PathValues.API_V1_SERVERS_SERVER_ID_LOCALNETWORKS_NATMODE: ApiV1ServersServerIdLocalNetworksNatMode,
        PathValues.API_V1_SERVERS_SERVER_ID_IPS: ApiV1ServersServerIdIps,
        PathValues.API_V1_SERVERS_SERVER_ID_LOGS: ApiV1ServersServerIdLogs,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS: ApiV1ServersServerIdDisks,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID: ApiV1ServersServerIdDisksDiskId,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_AUTOBACKUPS: ApiV1ServersServerIdDisksDiskIdAutoBackups,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS: ApiV1ServersServerIdDisksDiskIdBackups,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID: ApiV1ServersServerIdDisksDiskIdBackupsBackupId,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID_ACTION: ApiV1ServersServerIdDisksDiskIdBackupsBackupIdAction,
        PathValues.API_V1_SERVERS_SERVER_ID_IMAGEUNMOUNT: ApiV1ServersServerIdImageUnmount,
        PathValues.API_V1_PROJECTS: ApiV1Projects,
        PathValues.API_V1_PROJECTS_PROJECT_ID: ApiV1ProjectsProjectId,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_BALANCERS: ApiV1ProjectsProjectIdResourcesBalancers,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_BUCKETS: ApiV1ProjectsProjectIdResourcesBuckets,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_CLUSTERS: ApiV1ProjectsProjectIdResourcesClusters,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_SERVERS: ApiV1ProjectsProjectIdResourcesServers,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_DATABASES: ApiV1ProjectsProjectIdResourcesDatabases,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_DEDICATED: ApiV1ProjectsProjectIdResourcesDedicated,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES: ApiV1ProjectsProjectIdResources,
        PathValues.API_V1_PROJECTS_RESOURCES_BALANCERS: ApiV1ProjectsResourcesBalancers,
        PathValues.API_V1_PROJECTS_RESOURCES_SERVERS: ApiV1ProjectsResourcesServers,
        PathValues.API_V1_PROJECTS_RESOURCES_BUCKETS: ApiV1ProjectsResourcesBuckets,
        PathValues.API_V1_PROJECTS_RESOURCES_CLUSTERS: ApiV1ProjectsResourcesClusters,
        PathValues.API_V1_PROJECTS_RESOURCES_DATABASES: ApiV1ProjectsResourcesDatabases,
        PathValues.API_V1_PROJECTS_RESOURCES_DEDICATED: ApiV1ProjectsResourcesDedicated,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_TRANSFER: ApiV1ProjectsProjectIdResourcesTransfer,
        PathValues.API_V1_STORAGES_BUCKETS: ApiV1StoragesBuckets,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID: ApiV1StoragesBucketsBucketId,
        PathValues.API_V1_PRESETS_STORAGES: ApiV1PresetsStorages,
        PathValues.API_V1_STORAGES_USERS: ApiV1StoragesUsers,
        PathValues.API_V1_STORAGES_USERS_USER_ID: ApiV1StoragesUsersUserId,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_TRANSFERSTATUS: ApiV1StoragesBucketsBucketIdTransferStatus,
        PathValues.API_V1_STORAGES_TRANSFER: ApiV1StoragesTransfer,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_SUBDOMAINS: ApiV1StoragesBucketsBucketIdSubdomains,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_LIST: ApiV1StoragesBucketsBucketIdObjectManagerList,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_RENAME: ApiV1StoragesBucketsBucketIdObjectManagerRename,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_REMOVE: ApiV1StoragesBucketsBucketIdObjectManagerRemove,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_COPY: ApiV1StoragesBucketsBucketIdObjectManagerCopy,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_UPLOAD: ApiV1StoragesBucketsBucketIdObjectManagerUpload,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_MKDIR: ApiV1StoragesBucketsBucketIdObjectManagerMkdir,
        PathValues.API_V1_STORAGES_CERTIFICATES_GENERATE: ApiV1StoragesCertificatesGenerate,
        PathValues.API_V1_AUTH_APIKEYS: ApiV1AuthApiKeys,
        PathValues.API_V1_AUTH_APIKEYS_TOKEN_ID: ApiV1AuthApiKeysTokenId,
        PathValues.API_V1_AUTH_ACCESS: ApiV1AuthAccess,
        PathValues.API_V1_AUTH_ACCESS_COUNTRIES_ENABLED: ApiV1AuthAccessCountriesEnabled,
        PathValues.API_V1_AUTH_ACCESS_COUNTRIES: ApiV1AuthAccessCountries,
        PathValues.API_V1_AUTH_ACCESS_IPS_ENABLED: ApiV1AuthAccessIpsEnabled,
        PathValues.API_V1_AUTH_ACCESS_IPS: ApiV1AuthAccessIps,
        PathValues.API_V1_MAIL: ApiV1Mail,
        PathValues.API_V1_MAIL_QUOTA: ApiV1MailQuota,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN: ApiV1MailDomainsDomain,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN_INFO: ApiV1MailDomainsDomainInfo,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN_MAILBOXES_MAILBOX: ApiV1MailDomainsDomainMailboxesMailbox,
        PathValues.API_V1_DOMAINS: ApiV1Domains,
        PathValues.API_V1_DOMAINS_FQDN: ApiV1DomainsFqdn,
        PathValues.API_V1_DOMAINS_FQDN_DNSRECORDS: ApiV1DomainsFqdnDnsRecords,
        PathValues.API_V1_DOMAINS_FQDN_DNSRECORDS_RECORD_ID: ApiV1DomainsFqdnDnsRecordsRecordId,
        PathValues.API_V1_DOMAINS_FQDN_DEFAULTDNSRECORDS: ApiV1DomainsFqdnDefaultDnsRecords,
        PathValues.API_V1_DOMAINS_FQDN_SUBDOMAINS_SUBDOMAIN_FQDN: ApiV1DomainsFqdnSubdomainsSubdomainFqdn,
        PathValues.API_V1_DOMAINS_FQDN_NAMESERVERS: ApiV1DomainsFqdnNameServers,
        PathValues.API_V1_DOMAINSREQUESTS: ApiV1DomainsRequests,
        PathValues.API_V1_DOMAINSREQUESTS_REQUEST_ID: ApiV1DomainsRequestsRequestId,
        PathValues.API_V1_TLDS: ApiV1Tlds,
        PathValues.API_V1_TLDS_TLD_ID: ApiV1TldsTldId,
        PathValues.API_V1_CHECKDOMAIN_FQDN: ApiV1CheckDomainFqdn,
        PathValues.API_V1_ADDDOMAIN_FQDN: ApiV1AddDomainFqdn,
        PathValues.API_V2_VPCS: ApiV2Vpcs,
        PathValues.API_V2_VPCS_VPC_ID: ApiV2VpcsVpcId,
        PathValues.API_V2_VPCS_VPC_ID_SERVICES: ApiV2VpcsVpcIdServices,
        PathValues.API_V1_VPCS_VPC_ID: ApiV1VpcsVpcId,
        PathValues.API_V1_VPCS_VPC_ID_PORTS: ApiV1VpcsVpcIdPorts,
        PathValues.API_V1_SSHKEYS: ApiV1SshKeys,
        PathValues.API_V1_SSHKEYS_SSH_KEY_ID: ApiV1SshKeysSshKeyId,
        PathValues.API_V1_SERVERS_SERVER_ID_SSHKEYS: ApiV1ServersServerIdSshKeys,
        PathValues.API_V1_SERVERS_SERVER_ID_SSHKEYS_SSH_KEY_ID: ApiV1ServersServerIdSshKeysSshKeyId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_ACCOUNT_FINANCES: ApiV1AccountFinances,
        PathValues.API_V1_ACCOUNT_STATUS: ApiV1AccountStatus,
        PathValues.API_V1_ACCOUNT_NOTIFICATIONSETTINGS: ApiV1AccountNotificationSettings,
        PathValues.API_V1_IMAGES: ApiV1Images,
        PathValues.API_V1_IMAGES_IMAGE_ID: ApiV1ImagesImageId,
        PathValues.API_V1_IMAGES_IMAGE_ID_DOWNLOADURL: ApiV1ImagesImageIdDownloadUrl,
        PathValues.API_V1_IMAGES_IMAGE_ID_DOWNLOADURL_IMAGE_URL_ID: ApiV1ImagesImageIdDownloadUrlImageUrlId,
        PathValues.API_V1_FIREWALL_GROUPS: ApiV1FirewallGroups,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID: ApiV1FirewallGroupsGroupId,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES: ApiV1FirewallGroupsGroupIdResources,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES_RESOURCE_ID: ApiV1FirewallGroupsGroupIdResourcesResourceId,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RULES: ApiV1FirewallGroupsGroupIdRules,
        PathValues.API_V1_FIREWALL_GROUPS_GROUP_ID_RULES_RULE_ID: ApiV1FirewallGroupsGroupIdRulesRuleId,
        PathValues.API_V1_FIREWALL_SERVICE_RESOURCE_TYPE_RESOURCE_ID: ApiV1FirewallServiceResourceTypeResourceId,
        PathValues.API_V1_BALANCERS: ApiV1Balancers,
        PathValues.API_V1_BALANCERS_BALANCER_ID: ApiV1BalancersBalancerId,
        PathValues.API_V1_BALANCERS_BALANCER_ID_IPS: ApiV1BalancersBalancerIdIps,
        PathValues.API_V1_BALANCERS_BALANCER_ID_RULES: ApiV1BalancersBalancerIdRules,
        PathValues.API_V1_BALANCERS_BALANCER_ID_RULES_RULE_ID: ApiV1BalancersBalancerIdRulesRuleId,
        PathValues.API_V1_PRESETS_BALANCERS: ApiV1PresetsBalancers,
        PathValues.API_V1_DATABASES: ApiV1Databases,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID: ApiV1DatabasesDbClusterId,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_ADMINS: ApiV1DatabasesDbClusterIdAdmins,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_ADMINS_ADMIN_ID: ApiV1DatabasesDbClusterIdAdminsAdminId,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES: ApiV1DatabasesDbClusterIdInstances,
        PathValues.API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES_INSTANCE_ID: ApiV1DatabasesDbClusterIdInstancesInstanceId,
        PathValues.API_V1_DBS: ApiV1Dbs,
        PathValues.API_V1_DBS_DB_ID: ApiV1DbsDbId,
        PathValues.API_V1_DBS_DB_ID_AUTOBACKUPS: ApiV1DbsDbIdAutoBackups,
        PathValues.API_V1_DBS_DB_ID_BACKUPS: ApiV1DbsDbIdBackups,
        PathValues.API_V1_DBS_DB_ID_BACKUPS_BACKUP_ID: ApiV1DbsDbIdBackupsBackupId,
        PathValues.API_V1_PRESETS_DBS: ApiV1PresetsDbs,
        PathValues.API_V1_DEDICATEDSERVERS: ApiV1DedicatedServers,
        PathValues.API_V1_DEDICATEDSERVERS_DEDICATED_ID: ApiV1DedicatedServersDedicatedId,
        PathValues.API_V1_PRESETS_DEDICATEDSERVERS: ApiV1PresetsDedicatedServers,
        PathValues.API_V1_PRESETS_DEDICATEDSERVERS_PRESET_ID_ADDITIONALSERVICES: ApiV1PresetsDedicatedServersPresetIdAdditionalServices,
        PathValues.API_V1_K8S_CLUSTERS: ApiV1K8sClusters,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID: ApiV1K8sClustersClusterId,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_RESOURCES: ApiV1K8sClustersClusterIdResources,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_KUBECONFIG: ApiV1K8sClustersClusterIdKubeconfig,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS: ApiV1K8sClustersClusterIdGroups,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID: ApiV1K8sClustersClusterIdGroupsGroupId,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID_NODES: ApiV1K8sClustersClusterIdGroupsGroupIdNodes,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES: ApiV1K8sClustersClusterIdNodes,
        PathValues.API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES_NODE_ID: ApiV1K8sClustersClusterIdNodesNodeId,
        PathValues.API_V1_K8S_K8S_VERSIONS: ApiV1K8sK8sVersions,
        PathValues.API_V1_K8S_NETWORK_DRIVERS: ApiV1K8sNetworkDrivers,
        PathValues.API_V1_PRESETS_K8S: ApiV1PresetsK8s,
        PathValues.API_V1_SERVERS: ApiV1Servers,
        PathValues.API_V1_SERVERS_SERVER_ID: ApiV1ServersServerId,
        PathValues.API_V1_SERVERS_SERVER_ID_ACTION: ApiV1ServersServerIdAction,
        PathValues.API_V1_SERVERS_SERVER_ID_CLONE: ApiV1ServersServerIdClone,
        PathValues.API_V1_SERVERS_SERVER_ID_STATISTICS: ApiV1ServersServerIdStatistics,
        PathValues.API_V1_OS_SERVERS: ApiV1OsServers,
        PathValues.API_V1_PRESETS_SERVERS: ApiV1PresetsServers,
        PathValues.API_V1_CONFIGURATOR_SERVERS: ApiV1ConfiguratorServers,
        PathValues.API_V1_SOFTWARE_SERVERS: ApiV1SoftwareServers,
        PathValues.API_V1_SERVERS_SERVER_ID_BOOTMODE: ApiV1ServersServerIdBootMode,
        PathValues.API_V1_SERVERS_SERVER_ID_LOCALNETWORKS_NATMODE: ApiV1ServersServerIdLocalNetworksNatMode,
        PathValues.API_V1_SERVERS_SERVER_ID_IPS: ApiV1ServersServerIdIps,
        PathValues.API_V1_SERVERS_SERVER_ID_LOGS: ApiV1ServersServerIdLogs,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS: ApiV1ServersServerIdDisks,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID: ApiV1ServersServerIdDisksDiskId,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_AUTOBACKUPS: ApiV1ServersServerIdDisksDiskIdAutoBackups,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS: ApiV1ServersServerIdDisksDiskIdBackups,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID: ApiV1ServersServerIdDisksDiskIdBackupsBackupId,
        PathValues.API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID_ACTION: ApiV1ServersServerIdDisksDiskIdBackupsBackupIdAction,
        PathValues.API_V1_SERVERS_SERVER_ID_IMAGEUNMOUNT: ApiV1ServersServerIdImageUnmount,
        PathValues.API_V1_PROJECTS: ApiV1Projects,
        PathValues.API_V1_PROJECTS_PROJECT_ID: ApiV1ProjectsProjectId,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_BALANCERS: ApiV1ProjectsProjectIdResourcesBalancers,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_BUCKETS: ApiV1ProjectsProjectIdResourcesBuckets,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_CLUSTERS: ApiV1ProjectsProjectIdResourcesClusters,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_SERVERS: ApiV1ProjectsProjectIdResourcesServers,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_DATABASES: ApiV1ProjectsProjectIdResourcesDatabases,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_DEDICATED: ApiV1ProjectsProjectIdResourcesDedicated,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES: ApiV1ProjectsProjectIdResources,
        PathValues.API_V1_PROJECTS_RESOURCES_BALANCERS: ApiV1ProjectsResourcesBalancers,
        PathValues.API_V1_PROJECTS_RESOURCES_SERVERS: ApiV1ProjectsResourcesServers,
        PathValues.API_V1_PROJECTS_RESOURCES_BUCKETS: ApiV1ProjectsResourcesBuckets,
        PathValues.API_V1_PROJECTS_RESOURCES_CLUSTERS: ApiV1ProjectsResourcesClusters,
        PathValues.API_V1_PROJECTS_RESOURCES_DATABASES: ApiV1ProjectsResourcesDatabases,
        PathValues.API_V1_PROJECTS_RESOURCES_DEDICATED: ApiV1ProjectsResourcesDedicated,
        PathValues.API_V1_PROJECTS_PROJECT_ID_RESOURCES_TRANSFER: ApiV1ProjectsProjectIdResourcesTransfer,
        PathValues.API_V1_STORAGES_BUCKETS: ApiV1StoragesBuckets,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID: ApiV1StoragesBucketsBucketId,
        PathValues.API_V1_PRESETS_STORAGES: ApiV1PresetsStorages,
        PathValues.API_V1_STORAGES_USERS: ApiV1StoragesUsers,
        PathValues.API_V1_STORAGES_USERS_USER_ID: ApiV1StoragesUsersUserId,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_TRANSFERSTATUS: ApiV1StoragesBucketsBucketIdTransferStatus,
        PathValues.API_V1_STORAGES_TRANSFER: ApiV1StoragesTransfer,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_SUBDOMAINS: ApiV1StoragesBucketsBucketIdSubdomains,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_LIST: ApiV1StoragesBucketsBucketIdObjectManagerList,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_RENAME: ApiV1StoragesBucketsBucketIdObjectManagerRename,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_REMOVE: ApiV1StoragesBucketsBucketIdObjectManagerRemove,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_COPY: ApiV1StoragesBucketsBucketIdObjectManagerCopy,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_UPLOAD: ApiV1StoragesBucketsBucketIdObjectManagerUpload,
        PathValues.API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_MKDIR: ApiV1StoragesBucketsBucketIdObjectManagerMkdir,
        PathValues.API_V1_STORAGES_CERTIFICATES_GENERATE: ApiV1StoragesCertificatesGenerate,
        PathValues.API_V1_AUTH_APIKEYS: ApiV1AuthApiKeys,
        PathValues.API_V1_AUTH_APIKEYS_TOKEN_ID: ApiV1AuthApiKeysTokenId,
        PathValues.API_V1_AUTH_ACCESS: ApiV1AuthAccess,
        PathValues.API_V1_AUTH_ACCESS_COUNTRIES_ENABLED: ApiV1AuthAccessCountriesEnabled,
        PathValues.API_V1_AUTH_ACCESS_COUNTRIES: ApiV1AuthAccessCountries,
        PathValues.API_V1_AUTH_ACCESS_IPS_ENABLED: ApiV1AuthAccessIpsEnabled,
        PathValues.API_V1_AUTH_ACCESS_IPS: ApiV1AuthAccessIps,
        PathValues.API_V1_MAIL: ApiV1Mail,
        PathValues.API_V1_MAIL_QUOTA: ApiV1MailQuota,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN: ApiV1MailDomainsDomain,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN_INFO: ApiV1MailDomainsDomainInfo,
        PathValues.API_V1_MAIL_DOMAINS_DOMAIN_MAILBOXES_MAILBOX: ApiV1MailDomainsDomainMailboxesMailbox,
        PathValues.API_V1_DOMAINS: ApiV1Domains,
        PathValues.API_V1_DOMAINS_FQDN: ApiV1DomainsFqdn,
        PathValues.API_V1_DOMAINS_FQDN_DNSRECORDS: ApiV1DomainsFqdnDnsRecords,
        PathValues.API_V1_DOMAINS_FQDN_DNSRECORDS_RECORD_ID: ApiV1DomainsFqdnDnsRecordsRecordId,
        PathValues.API_V1_DOMAINS_FQDN_DEFAULTDNSRECORDS: ApiV1DomainsFqdnDefaultDnsRecords,
        PathValues.API_V1_DOMAINS_FQDN_SUBDOMAINS_SUBDOMAIN_FQDN: ApiV1DomainsFqdnSubdomainsSubdomainFqdn,
        PathValues.API_V1_DOMAINS_FQDN_NAMESERVERS: ApiV1DomainsFqdnNameServers,
        PathValues.API_V1_DOMAINSREQUESTS: ApiV1DomainsRequests,
        PathValues.API_V1_DOMAINSREQUESTS_REQUEST_ID: ApiV1DomainsRequestsRequestId,
        PathValues.API_V1_TLDS: ApiV1Tlds,
        PathValues.API_V1_TLDS_TLD_ID: ApiV1TldsTldId,
        PathValues.API_V1_CHECKDOMAIN_FQDN: ApiV1CheckDomainFqdn,
        PathValues.API_V1_ADDDOMAIN_FQDN: ApiV1AddDomainFqdn,
        PathValues.API_V2_VPCS: ApiV2Vpcs,
        PathValues.API_V2_VPCS_VPC_ID: ApiV2VpcsVpcId,
        PathValues.API_V2_VPCS_VPC_ID_SERVICES: ApiV2VpcsVpcIdServices,
        PathValues.API_V1_VPCS_VPC_ID: ApiV1VpcsVpcId,
        PathValues.API_V1_VPCS_VPC_ID_PORTS: ApiV1VpcsVpcIdPorts,
        PathValues.API_V1_SSHKEYS: ApiV1SshKeys,
        PathValues.API_V1_SSHKEYS_SSH_KEY_ID: ApiV1SshKeysSshKeyId,
        PathValues.API_V1_SERVERS_SERVER_ID_SSHKEYS: ApiV1ServersServerIdSshKeys,
        PathValues.API_V1_SERVERS_SERVER_ID_SSHKEYS_SSH_KEY_ID: ApiV1ServersServerIdSshKeysSshKeyId,
    }
)
