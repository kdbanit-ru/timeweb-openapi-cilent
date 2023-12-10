# openapi_client.model.database_cluster.DatabaseCluster

Кластер базы данных

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Кластер базы данных | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) | [**ConfigParameters**](ConfigParameters.md) |  | 
**created_at** | str,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**[networks](#networks)** | list, tuple,  | tuple,  | Список сетей кластера базы данных. | 
**type** | str,  | str,  | Тип кластера базы данных. | must be one of ["mysql", "mysql5", "postgres", "redis", "mongodb", ] 
**port** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Порт | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа. | 
**[disk_stats](#disk_stats)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Статистика использования диска кластера базы данных. | 
**name** | str,  | str,  | Название кластера базы данных. | 
**location** | None, str,  | NoneClass, str,  | Локация сервера. | must be one of ["ru-1", "ru-2", "pl-1", "kz-1", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**is_enabled_public_network** | bool,  | BoolClass,  | Доступность публичного IP-адреса | 
**hash_type** | None, str,  | NoneClass, str,  | Тип хеширования кластера базы данных (mysql5 | mysql | postgres). | must be one of ["caching_sha2", "mysql_native", None, ] 
**status** | str,  | str,  | Текущий статус кластера базы данных. | must be one of ["started", "starting", "stopped", "no_paid", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# networks

Список сетей кластера базы данных.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список сетей кластера базы данных. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# disk_stats

Статистика использования диска кластера базы данных.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Статистика использования диска кластера базы данных. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) диска кластера базы данных. | 
**used** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) использованного пространства диска кластера базы данных. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

