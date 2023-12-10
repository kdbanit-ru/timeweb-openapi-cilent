# openapi_client.model.rule.Rule

Правило для балансировщика

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Правило для балансировщика | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**balancer_port** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порт балансировщика. | 
**server_port** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порт сервера. | 
**balancer_proto** | str,  | str,  | Протокол балансировщика. | must be one of ["http", "http2", "https", "tcp", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра правила для балансировщика. Автоматически генерируется при создании. | 
**server_proto** | str,  | str,  | Протокол сервера. | must be one of ["http", "http2", "https", "tcp", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

