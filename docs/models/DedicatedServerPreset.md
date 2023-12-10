# openapi_client.model.dedicated_server_preset.DedicatedServerPreset

Выделенный сервер

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Выделенный сервер | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[disk](#disk)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию о диске выделенного сервера. | 
**[memory](#memory)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию об ОЗУ выделенного сервера. | 
**[cpu](#cpu)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию о процессоре выделенного сервера. | 
**description** | str,  | str,  | Описание характеристик тарифа выделенного сервера. | 
**is_ipmi_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, доступен ли IPMI у данного тарифа. | 
**location** | str,  | str,  | Локация. | must be one of ["ru-1", "ru-2", "kz-1", "pl-1", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор тарифа выделенного сервера. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость тарифа выделенного сервера | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cpu

Объект, содержащий информацию о процессоре выделенного сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию о процессоре выделенного сервера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description_short** | str,  | str,  | Краткое описание характеристик процессора выделенного сервера. | 
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора выделенного сервера. | 
**description** | str,  | str,  | Описание характеристик процессора выделенного сервера. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# disk

Объект, содержащий информацию о диске выделенного сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию о диске выделенного сервера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество дисков выделенного сервера. | 
**description** | str,  | str,  | Описание характеристик диска выделенного сервера. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# memory

Объект, содержащий информацию об ОЗУ выделенного сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Объект, содержащий информацию об ОЗУ выделенного сервера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Мб) ОЗУ выделенного сервера. | 
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ОЗУ выделенного сервера. | 
**description** | str,  | str,  | Описание характеристик ОЗУ выделенного сервера. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

