# openapi_client.model.image_out_api.ImageOutAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[os](#os)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Операционная система образа | 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | Размер в мегабайтах | 
**name** | str,  | str,  | Имя образа | 
**created_at** | str, datetime,  | str,  | Дата и время создания | value must conform to RFC-3339 date-time
**description** | str,  | str,  | Описание образа | 
**is_custom** | bool,  | BoolClass,  | Признак указывающий на то является ли образ кастомным | 
**progress** | decimal.Decimal, int,  | decimal.Decimal,  | Процент создания образа | 
**id** | str,  | str,  | Идентификатор образа | 
**deleted_at** | str, datetime,  | str,  | Дата и время удаления | value must conform to RFC-3339 date-time
**disk_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор связанного с образом диска | 
**[status](#status)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Статус образа | 
**location** | str,  | str,  | Локация, в которой создан образ | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# status

Статус образа

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Статус образа | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ImageStatus](ImageStatus.md) | [**ImageStatus**](ImageStatus.md) | [**ImageStatus**](ImageStatus.md) |  | 

# os

Операционная система образа

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Операционная система образа | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[OS](OS.md) | [**OS**](OS.md) | [**OS**](OS.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

