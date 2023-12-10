# openapi_client.model.use.Use

Оплата заявки на продление/регистрацию домена с баланса аккаунта

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Оплата заявки на продление/регистрацию домена с баланса аккаунта | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**money_source** | str,  | str,  | Тип создаваемой заявки. | must be one of ["use", ] 
**person_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

