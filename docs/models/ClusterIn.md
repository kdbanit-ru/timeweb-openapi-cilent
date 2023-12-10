# openapi_client.model.cluster_in.ClusterIn

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ingress** | bool,  | BoolClass,  | Логическое значение, которое показывает, использовать ли Ingress в кластере | 
**network_driver** | str,  | str,  | Тип используемого сетевого драйвера в кластере | 
**k8s_version** | str,  | str,  | Версия Kubernetes | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа мастер-ноды | 
**name** | str,  | str,  | Название кластера | 
**ha** | bool,  | BoolClass,  | Описание появится позднее | 
**description** | str,  | str,  | Описание кластера | [optional] 
**[worker_groups](#worker_groups)** | list, tuple,  | tuple,  | Группы воркеров в кластере | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# worker_groups

Группы воркеров в кластере

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Группы воркеров в кластере | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NodeGroupIn**](NodeGroupIn.md) | [**NodeGroupIn**](NodeGroupIn.md) | [**NodeGroupIn**](NodeGroupIn.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

