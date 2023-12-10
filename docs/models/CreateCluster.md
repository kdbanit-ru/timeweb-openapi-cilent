# openapi_client.model.create_cluster.CreateCluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа. | 
**name** | str,  | str,  | Название кластера базы данных. | 
**type** | str,  | str,  | Тип базы данных. | must be one of ["mysql", "mysql5", "postgres", "redis", "mongodb", ] 
**[admin](#admin)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[instance](#instance)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | База данных | [optional] 
**hash_type** | str,  | str,  | Тип хеширования базы данных (mysql5 | mysql | postgres). | [optional] must be one of ["caching_sha2", "mysql_native", ] 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**network** | [**Network**](Network.md) | [**Network**](Network.md) |  | [optional] 
**description** | str,  | str,  | Описание кластера базы данных | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# admin

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**login** | str,  | str,  | Имя пользователя базы данных | [optional] 
**password** | str,  | str,  | Пароль пользователя базы данных | [optional] 
**host** | str,  | str,  | Хост пользователя | [optional] 
**[privileges](#privileges)** | list, tuple,  | tuple,  | Список привилегий пользователя базы данных | [optional] 
**description** | str,  | str,  | Описание пользователя базы данных | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# privileges

Список привилегий пользователя базы данных

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список привилегий пользователя базы данных | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ALTER", "CREATE_VIEW", "CREATE", "DELETE", "DROP", "EVENT", "INDEX", "INSERT", "LOCK_TABLES", "REFERENCES", "SELECT", "SHOW_VIEW", "TRUNCATE", "UPDATE", "READ", "WRITE", "CONNECTION", "FAST", "readWrite", "ALTER_ROUTINE", "CREATE_ROUTINE", "TRANSACTION", ] 

# instance

База данных

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | База данных | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Название базы данных | [optional] 
**description** | str,  | str,  | Описание базы данных | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

