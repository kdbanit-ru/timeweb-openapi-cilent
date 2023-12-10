# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_ACCOUNT_FINANCES = "/api/v1/account/finances"
    API_V1_ACCOUNT_STATUS = "/api/v1/account/status"
    API_V1_ACCOUNT_NOTIFICATIONSETTINGS = "/api/v1/account/notification-settings"
    API_V1_IMAGES = "/api/v1/images"
    API_V1_IMAGES_IMAGE_ID = "/api/v1/images/{image_id}"
    API_V1_IMAGES_IMAGE_ID_DOWNLOADURL = "/api/v1/images/{image_id}/download-url"
    API_V1_IMAGES_IMAGE_ID_DOWNLOADURL_IMAGE_URL_ID = "/api/v1/images/{image_id}/download-url/{image_url_id}"
    API_V1_FIREWALL_GROUPS = "/api/v1/firewall/groups"
    API_V1_FIREWALL_GROUPS_GROUP_ID = "/api/v1/firewall/groups/{group_id}"
    API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES = "/api/v1/firewall/groups/{group_id}/resources"
    API_V1_FIREWALL_GROUPS_GROUP_ID_RESOURCES_RESOURCE_ID = "/api/v1/firewall/groups/{group_id}/resources/{resource_id}"
    API_V1_FIREWALL_GROUPS_GROUP_ID_RULES = "/api/v1/firewall/groups/{group_id}/rules"
    API_V1_FIREWALL_GROUPS_GROUP_ID_RULES_RULE_ID = "/api/v1/firewall/groups/{group_id}/rules/{rule_id}"
    API_V1_FIREWALL_SERVICE_RESOURCE_TYPE_RESOURCE_ID = "/api/v1/firewall/service/{resource_type}/{resource_id}"
    API_V1_BALANCERS = "/api/v1/balancers"
    API_V1_BALANCERS_BALANCER_ID = "/api/v1/balancers/{balancer_id}"
    API_V1_BALANCERS_BALANCER_ID_IPS = "/api/v1/balancers/{balancer_id}/ips"
    API_V1_BALANCERS_BALANCER_ID_RULES = "/api/v1/balancers/{balancer_id}/rules"
    API_V1_BALANCERS_BALANCER_ID_RULES_RULE_ID = "/api/v1/balancers/{balancer_id}/rules/{rule_id}"
    API_V1_PRESETS_BALANCERS = "/api/v1/presets/balancers"
    API_V1_DATABASES = "/api/v1/databases"
    API_V1_DATABASES_DB_CLUSTER_ID = "/api/v1/databases/{db_cluster_id}"
    API_V1_DATABASES_DB_CLUSTER_ID_ADMINS = "/api/v1/databases/{db_cluster_id}/admins"
    API_V1_DATABASES_DB_CLUSTER_ID_ADMINS_ADMIN_ID = "/api/v1/databases/{db_cluster_id}/admins/{admin_id}"
    API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES = "/api/v1/databases/{db_cluster_id}/instances"
    API_V1_DATABASES_DB_CLUSTER_ID_INSTANCES_INSTANCE_ID = "/api/v1/databases/{db_cluster_id}/instances/{instance_id}"
    API_V1_DBS = "/api/v1/dbs"
    API_V1_DBS_DB_ID = "/api/v1/dbs/{db_id}"
    API_V1_DBS_DB_ID_AUTOBACKUPS = "/api/v1/dbs/{db_id}/auto-backups"
    API_V1_DBS_DB_ID_BACKUPS = "/api/v1/dbs/{db_id}/backups"
    API_V1_DBS_DB_ID_BACKUPS_BACKUP_ID = "/api/v1/dbs/{db_id}/backups/{backup_id}"
    API_V1_PRESETS_DBS = "/api/v1/presets/dbs"
    API_V1_DEDICATEDSERVERS = "/api/v1/dedicated-servers"
    API_V1_DEDICATEDSERVERS_DEDICATED_ID = "/api/v1/dedicated-servers/{dedicated_id}"
    API_V1_PRESETS_DEDICATEDSERVERS = "/api/v1/presets/dedicated-servers"
    API_V1_PRESETS_DEDICATEDSERVERS_PRESET_ID_ADDITIONALSERVICES = "/api/v1/presets/dedicated-servers/{preset_id}/additional-services"
    API_V1_K8S_CLUSTERS = "/api/v1/k8s/clusters"
    API_V1_K8S_CLUSTERS_CLUSTER_ID = "/api/v1/k8s/clusters/{cluster_id}"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_RESOURCES = "/api/v1/k8s/clusters/{cluster_id}/resources"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_KUBECONFIG = "/api/v1/k8s/clusters/{cluster_id}/kubeconfig"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS = "/api/v1/k8s/clusters/{cluster_id}/groups"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID = "/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_GROUPS_GROUP_ID_NODES = "/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES = "/api/v1/k8s/clusters/{cluster_id}/nodes"
    API_V1_K8S_CLUSTERS_CLUSTER_ID_NODES_NODE_ID = "/api/v1/k8s/clusters/{cluster_id}/nodes/{node_id}"
    API_V1_K8S_K8S_VERSIONS = "/api/v1/k8s/k8s_versions"
    API_V1_K8S_NETWORK_DRIVERS = "/api/v1/k8s/network_drivers"
    API_V1_PRESETS_K8S = "/api/v1/presets/k8s"
    API_V1_SERVERS = "/api/v1/servers"
    API_V1_SERVERS_SERVER_ID = "/api/v1/servers/{server_id}"
    API_V1_SERVERS_SERVER_ID_ACTION = "/api/v1/servers/{server_id}/action"
    API_V1_SERVERS_SERVER_ID_CLONE = "/api/v1/servers/{server_id}/clone"
    API_V1_SERVERS_SERVER_ID_STATISTICS = "/api/v1/servers/{server_id}/statistics"
    API_V1_OS_SERVERS = "/api/v1/os/servers"
    API_V1_PRESETS_SERVERS = "/api/v1/presets/servers"
    API_V1_CONFIGURATOR_SERVERS = "/api/v1/configurator/servers"
    API_V1_SOFTWARE_SERVERS = "/api/v1/software/servers"
    API_V1_SERVERS_SERVER_ID_BOOTMODE = "/api/v1/servers/{server_id}/boot-mode"
    API_V1_SERVERS_SERVER_ID_LOCALNETWORKS_NATMODE = "/api/v1/servers/{server_id}/local-networks/nat-mode"
    API_V1_SERVERS_SERVER_ID_IPS = "/api/v1/servers/{server_id}/ips"
    API_V1_SERVERS_SERVER_ID_LOGS = "/api/v1/servers/{server_id}/logs"
    API_V1_SERVERS_SERVER_ID_DISKS = "/api/v1/servers/{server_id}/disks"
    API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID = "/api/v1/servers/{server_id}/disks/{disk_id}"
    API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_AUTOBACKUPS = "/api/v1/servers/{server_id}/disks/{disk_id}/auto-backups"
    API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS = "/api/v1/servers/{server_id}/disks/{disk_id}/backups"
    API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID = "/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}"
    API_V1_SERVERS_SERVER_ID_DISKS_DISK_ID_BACKUPS_BACKUP_ID_ACTION = "/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action"
    API_V1_SERVERS_SERVER_ID_IMAGEUNMOUNT = "/api/v1/servers/{server_id}/image-unmount"
    API_V1_PROJECTS = "/api/v1/projects"
    API_V1_PROJECTS_PROJECT_ID = "/api/v1/projects/{project_id}"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_BALANCERS = "/api/v1/projects/{project_id}/resources/balancers"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_BUCKETS = "/api/v1/projects/{project_id}/resources/buckets"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_CLUSTERS = "/api/v1/projects/{project_id}/resources/clusters"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_SERVERS = "/api/v1/projects/{project_id}/resources/servers"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_DATABASES = "/api/v1/projects/{project_id}/resources/databases"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_DEDICATED = "/api/v1/projects/{project_id}/resources/dedicated"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES = "/api/v1/projects/{project_id}/resources"
    API_V1_PROJECTS_RESOURCES_BALANCERS = "/api/v1/projects/resources/balancers"
    API_V1_PROJECTS_RESOURCES_SERVERS = "/api/v1/projects/resources/servers"
    API_V1_PROJECTS_RESOURCES_BUCKETS = "/api/v1/projects/resources/buckets"
    API_V1_PROJECTS_RESOURCES_CLUSTERS = "/api/v1/projects/resources/clusters"
    API_V1_PROJECTS_RESOURCES_DATABASES = "/api/v1/projects/resources/databases"
    API_V1_PROJECTS_RESOURCES_DEDICATED = "/api/v1/projects/resources/dedicated"
    API_V1_PROJECTS_PROJECT_ID_RESOURCES_TRANSFER = "/api/v1/projects/{project_id}/resources/transfer"
    API_V1_STORAGES_BUCKETS = "/api/v1/storages/buckets"
    API_V1_STORAGES_BUCKETS_BUCKET_ID = "/api/v1/storages/buckets/{bucket_id}"
    API_V1_PRESETS_STORAGES = "/api/v1/presets/storages"
    API_V1_STORAGES_USERS = "/api/v1/storages/users"
    API_V1_STORAGES_USERS_USER_ID = "/api/v1/storages/users/{user_id}"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_TRANSFERSTATUS = "/api/v1/storages/buckets/{bucket_id}/transfer-status"
    API_V1_STORAGES_TRANSFER = "/api/v1/storages/transfer"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_SUBDOMAINS = "/api/v1/storages/buckets/{bucket_id}/subdomains"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_LIST = "/api/v1/storages/buckets/{bucket_id}/object-manager/list"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_RENAME = "/api/v1/storages/buckets/{bucket_id}/object-manager/rename"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_REMOVE = "/api/v1/storages/buckets/{bucket_id}/object-manager/remove"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_COPY = "/api/v1/storages/buckets/{bucket_id}/object-manager/copy"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_UPLOAD = "/api/v1/storages/buckets/{bucket_id}/object-manager/upload"
    API_V1_STORAGES_BUCKETS_BUCKET_ID_OBJECTMANAGER_MKDIR = "/api/v1/storages/buckets/{bucket_id}/object-manager/mkdir"
    API_V1_STORAGES_CERTIFICATES_GENERATE = "/api/v1/storages/certificates/generate"
    API_V1_AUTH_APIKEYS = "/api/v1/auth/api-keys"
    API_V1_AUTH_APIKEYS_TOKEN_ID = "/api/v1/auth/api-keys/{token_id}"
    API_V1_AUTH_ACCESS = "/api/v1/auth/access"
    API_V1_AUTH_ACCESS_COUNTRIES_ENABLED = "/api/v1/auth/access/countries/enabled"
    API_V1_AUTH_ACCESS_COUNTRIES = "/api/v1/auth/access/countries"
    API_V1_AUTH_ACCESS_IPS_ENABLED = "/api/v1/auth/access/ips/enabled"
    API_V1_AUTH_ACCESS_IPS = "/api/v1/auth/access/ips"
    API_V1_MAIL = "/api/v1/mail"
    API_V1_MAIL_QUOTA = "/api/v1/mail/quota"
    API_V1_MAIL_DOMAINS_DOMAIN = "/api/v1/mail/domains/{domain}"
    API_V1_MAIL_DOMAINS_DOMAIN_INFO = "/api/v1/mail/domains/{domain}/info"
    API_V1_MAIL_DOMAINS_DOMAIN_MAILBOXES_MAILBOX = "/api/v1/mail/domains/{domain}/mailboxes/{mailbox}"
    API_V1_DOMAINS = "/api/v1/domains"
    API_V1_DOMAINS_FQDN = "/api/v1/domains/{fqdn}"
    API_V1_DOMAINS_FQDN_DNSRECORDS = "/api/v1/domains/{fqdn}/dns-records"
    API_V1_DOMAINS_FQDN_DNSRECORDS_RECORD_ID = "/api/v1/domains/{fqdn}/dns-records/{record_id}"
    API_V1_DOMAINS_FQDN_DEFAULTDNSRECORDS = "/api/v1/domains/{fqdn}/default-dns-records"
    API_V1_DOMAINS_FQDN_SUBDOMAINS_SUBDOMAIN_FQDN = "/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}"
    API_V1_DOMAINS_FQDN_NAMESERVERS = "/api/v1/domains/{fqdn}/name-servers"
    API_V1_DOMAINSREQUESTS = "/api/v1/domains-requests"
    API_V1_DOMAINSREQUESTS_REQUEST_ID = "/api/v1/domains-requests/{request_id}"
    API_V1_TLDS = "/api/v1/tlds"
    API_V1_TLDS_TLD_ID = "/api/v1/tlds/{tld_id}"
    API_V1_CHECKDOMAIN_FQDN = "/api/v1/check-domain/{fqdn}"
    API_V1_ADDDOMAIN_FQDN = "/api/v1/add-domain/{fqdn}"
    API_V2_VPCS = "/api/v2/vpcs"
    API_V2_VPCS_VPC_ID = "/api/v2/vpcs/{vpc_id}"
    API_V2_VPCS_VPC_ID_SERVICES = "/api/v2/vpcs/{vpc_id}/services"
    API_V1_VPCS_VPC_ID = "/api/v1/vpcs/{vpc_id}"
    API_V1_VPCS_VPC_ID_PORTS = "/api/v1/vpcs/{vpc_id}/ports"
    API_V1_SSHKEYS = "/api/v1/ssh-keys"
    API_V1_SSHKEYS_SSH_KEY_ID = "/api/v1/ssh-keys/{ssh_key_id}"
    API_V1_SERVERS_SERVER_ID_SSHKEYS = "/api/v1/servers/{server_id}/ssh-keys"
    API_V1_SERVERS_SERVER_ID_SSHKEYS_SSH_KEY_ID = "/api/v1/servers/{server_id}/ssh-keys/{ssh_key_id}"
