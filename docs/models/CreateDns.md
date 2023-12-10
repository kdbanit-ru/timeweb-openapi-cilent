# openapi_client.model.create_dns.CreateDns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Тип DNS-записи. | must be one of ["TXT", "SRV", "CNAME", "AAAA", "MX", "A", ] 
**value** | str,  | str,  | Значение DNS-записи. | 
**priority** | decimal.Decimal, int, float,  | decimal.Decimal,  | Приоритет DNS-записи. | [optional] 
**subdomain** | str,  | str,  | Полное имя поддомена. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

