# openapi_client.model.node_group_out.NodeGroupOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа мастер-ноды | 
**name** | str,  | str,  | Название группы | 
**created_at** | str, datetime,  | str,  | Дата и время создания группы в формате ISO8601 | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Уникальный идентификатор группы | 
**node_count** | decimal.Decimal, int,  | decimal.Decimal,  | Количество нод в группе | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

