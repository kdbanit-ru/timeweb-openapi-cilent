# openapi_client.model.status.Status

Статус аккаунта

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Статус аккаунта | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_blocked** | bool,  | BoolClass,  | Это логическое значение, которое показывает, заблокирован ли аккаунт. | 
**[company_info](#company_info)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Информация о компании. | 
**is_permanent_blocked** | bool,  | BoolClass,  | Это логическое значение, которое показывает, заблокирован ли аккаунт навсегда. | 
**is_send_bill_letters** | bool,  | BoolClass,  | Это логическое значение, которое показывает, требуется ли отправлять счета на почту. | 
**last_password_changed_at** | str,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда последний раз изменялся пароль. | 
**ym_client_id** | None, str,  | NoneClass, str,  | Идентификатор аккаунта для яндекс метрики. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# company_info

Информация о компании.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Информация о компании. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Название компании. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор компании. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

