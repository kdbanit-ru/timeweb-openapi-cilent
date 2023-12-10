# openapi_client.model.servers_preset.ServersPreset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bandwidth** | decimal.Decimal, int, float,  | decimal.Decimal,  | Пропускная способность тарифа. | 
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора. | 
**description** | str,  | str,  | Описание тарифа. | 
**[tags](#tags)** | list, tuple,  | tuple,  | Список тегов тарифа. | 
**description_short** | str,  | str,  | Короткое описание тарифа. | 
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер диска (в Мб). | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость в рублях. | 
**disk_type** | str,  | str,  | Тип диска. | must be one of ["ssd", "nvme", "hdd", ] 
**location** | str,  | str,  | Локация сервера. | must be one of ["ru-1", "pl-1", "kz-1", ] 
**cpu_frequency** | str,  | str,  | Частота процессора. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор тарифа сервера. | 
**is_allowed_local_network** | bool,  | BoolClass,  | Есть возможность подключения локальной сети | 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество (в Мб) оперативной памяти. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Список тегов тарифа.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список тегов тарифа. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

