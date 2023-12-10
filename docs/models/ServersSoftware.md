# openapi_client.model.servers_software.ServersSoftware

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор ПО из маркетплейса. | [optional] 
**name** | str,  | str,  | Имя ПО из маркетплейса. | [optional] 
**[os_ids](#os_ids)** | list, tuple,  | tuple,  | Список id операционных систем, на которых доступна установка ПО. | [optional] 
**description** | str,  | str,  | Описание ПО из маркетплейса. | [optional] 
**installations** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество установок ПО. | [optional] 
**[requirements](#requirements)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Требования к облачному серверу для установки ПО. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# os_ids

Список id операционных систем, на которых доступна установка ПО.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список id операционных систем, на которых доступна установка ПО. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# requirements

Требования к облачному серверу для установки ПО.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Требования к облачному серверу для установки ПО. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cpu_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальной значение процессора. | [optional] 
**disk_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение диска. | [optional] 
**ram_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение оперативной памяти. | [optional] 
**bandwidth_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение пропускной способности. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

