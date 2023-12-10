# openapi_client.model.database_admin.DatabaseAdmin

Пользователь базы данных

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Пользователь базы данных | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  | Пароль пользователя базы данных | 
**[instances](#instances)** | list, tuple,  | tuple,  |  | 
**host** | None, str,  | NoneClass, str,  | Хост пользователя | 
**created_at** | str,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**description** | str,  | str,  | Описанеие пользователя базы данных | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра пользователя базы данных. Автоматически генерируется при создании. | 
**login** | str,  | str,  | Имя пользователя базы данных | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[privileges](#privileges)** | list, tuple,  | tuple,  | Список привилегий пользователя базы данных | 
**instance_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор базы данных | 
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

