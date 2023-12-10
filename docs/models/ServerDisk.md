# openapi_client.model.server_disk.ServerDisk

Диск сервера

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Диск сервера | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_mounted** | bool,  | BoolClass,  | Является ли диск примонтированным. | 
**is_system** | bool,  | BoolClass,  | Является ли диск системным. | 
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер диска (в Мб). | 
**system_name** | str,  | str,  | Системное название диска. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор диска. | 
**used** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество использованной памяти диска (в Мб). | 
**type** | str,  | str,  | Тип диска. | 
**status** | str,  | str,  | Статус диска. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

