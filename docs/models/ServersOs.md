# openapi_client.model.servers_os.ServersOs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор операционной системы. | [optional] 
**family** | str,  | str,  | Семейство операционной системы. | [optional] 
**name** | str,  | str,  | Название операционной системы. | [optional] 
**version** | str,  | str,  | Версия операционной системы. | [optional] 
**version_codename** | str,  | str,  | Кодовое имя версии операционной системы. | [optional] 
**description** | str,  | str,  | Описание операционной системы. | [optional] 
**[requirements](#requirements)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Требования к облачному серверу для установки операционной системы. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requirements

Требования к облачному серверу для установки операционной системы.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Требования к облачному серверу для установки операционной системы. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cpu_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальной значение процессора. | [optional] 
**disk_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение диска. | [optional] 
**ram_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение оперативной памяти. | [optional] 
**bandwidth_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Минимальное значение пропускной способности. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

