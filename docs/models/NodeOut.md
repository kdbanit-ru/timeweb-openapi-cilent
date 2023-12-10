# openapi_client.model.node_out.NodeOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disk** | decimal.Decimal, int,  | decimal.Decimal,  | Количество пространства | 
**group_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор группы нод | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа ноды | 
**cpu** | decimal.Decimal, int,  | decimal.Decimal,  | Количество ядер | 
**created_at** | str, datetime,  | str,  | Дата и время создания ноды в формате ISO8601 | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Уникальный идентификатор ноды | 
**type** | str,  | str,  | Тип ноды | 
**network** | decimal.Decimal, int,  | decimal.Decimal,  | Пропускная способность сети | 
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | Количество памяти | 
**status** | str,  | str,  | Статус | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

