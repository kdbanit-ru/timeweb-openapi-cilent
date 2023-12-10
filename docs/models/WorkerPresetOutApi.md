# openapi_client.model.worker_preset_out_api.WorkerPresetOutApi

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description_short** | str,  | str,  | Краткое описание тарифа | 
**disk** | decimal.Decimal, int,  | decimal.Decimal,  | Количество пространства на ноде | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость | 
**cpu** | decimal.Decimal, int,  | decimal.Decimal,  | Количество ядер ноды | 
**description** | str,  | str,  | Описание тарифа | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Уникальный идентификатор тарифа | 
**network** | decimal.Decimal, int,  | decimal.Decimal,  | Пропускная способность ноды | 
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | Количество памяти ноды | 
**type** | str,  | str,  | Тип тарифа | [optional] must be one of ["worker", ] if omitted the server will use the default value of "worker"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

