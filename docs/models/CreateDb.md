# openapi_client.model.create_db.CreateDb

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  | Пароль для подключения к базе данных. | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа. | 
**name** | str,  | str,  | Название базы данных. | 
**type** | str,  | str,  | Тип базы данных. | must be one of ["mysql", "mysql5", "postgres", "redis", "mongodb", ] 
**login** | str,  | str,  | Логин для подключения к базе данных. | [optional] 
**hash_type** | str,  | str,  | Тип хеширования базы данных (mysql5 | mysql | postgres). | [optional] must be one of ["caching_sha2", "mysql_native", ] 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**network** | [**Network**](Network.md) | [**Network**](Network.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

