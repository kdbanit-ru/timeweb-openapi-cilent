# openapi_client.model.create_admin.CreateAdmin

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[privileges](#privileges)** | list, tuple,  | tuple,  | Список привилегий пользователя базы данных | 
**password** | str,  | str,  | Пароль пользователя базы данных | 
**login** | str,  | str,  | Имя пользователя базы данных | 
**host** | str,  | str,  | Хост пользователя | [optional] 
**instance_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор инстанса базы данных для приминения привилегий. В данных момент поле доступно только для кластеров MySQL. Если поле не передано, то привилегии будут применены ко всем инстансам | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

