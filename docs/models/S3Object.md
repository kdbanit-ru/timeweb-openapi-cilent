# openapi_client.model.s3_object.S3Object

An object consists of data and its descriptive metadata.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object consists of data and its descriptive metadata. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Тип (файл или папка). | must be one of ["file", "directory", ] 
**key** | str,  | str,  | Название файла или папки. | [optional] 
**last_modified** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была сделана последняя модификация файла или папки. | [optional] value must conform to RFC-3339 date-time
**etag** | str,  | str,  | Тег. | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | Размер (в байтах) файла или папки. | [optional] 
**storage_class** | str,  | str,  | Класс хранилища. | [optional] 
**[checksum_algorithm](#checksum_algorithm)** | list, tuple,  | tuple,  | Алгоритм | [optional] 
**[owner](#owner)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Информация о владельце файла или папки. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# checksum_algorithm

Алгоритм

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Алгоритм | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# owner

Информация о владельце файла или папки.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Информация о владельце файла или папки. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Идентификатор владельца файла. | [optional] 
**display_name** | str,  | str,  | Имя владельца файла. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

