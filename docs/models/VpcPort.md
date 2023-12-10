# openapi_client.model.vpc_port.VpcPort

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ipv4** | str,  | str,  | Внутренний адрес. | 
**[service](#service)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Сервис, к которому привязан порт. | 
**id** | str,  | str,  | Идентификатор порта. | 
**nat_mode** | str,  | str,  | Тип преобразования сетевых адресов. | must be one of ["dnat_and_snat", "snat", "no_nat", ] 
**mac** | str,  | str,  | MAC адрес. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service

Сервис, к которому привязан порт.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Сервис, к которому привязан порт. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Название сервиса. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор сервиса. | 
**type** | str,  | str,  | Тип сервиса. | must be one of ["server", "balancer", "dbaas", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

