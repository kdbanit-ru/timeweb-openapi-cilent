# openapi_client.model.server_backup.ServerBackup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер бэкапа (в Мб). | 
**name** | str,  | str,  | Название бэкапа. | 
**created_at** | str,  | str,  | Дата создания бэкапа. | 
**progress** | decimal.Decimal, int, float,  | decimal.Decimal,  | Прогресс создания бэкапа. Значение будет меняться в статусе бэкапа &#x60;create&#x60; от 0 до 99, для остальных статусов всегда будет возвращаться 0. | 
**comment** | None, str,  | NoneClass, str,  | Комментарий к бэкапу. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор бэкапа сервера. | 
**type** | str,  | str,  | Тип бэкапа. | must be one of ["manual", "auto", ] 
**status** | str,  | str,  | Статус бэкапа. | must be one of ["precreate", "delete", "shutdown", "recover", "create", "fail", "done", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

