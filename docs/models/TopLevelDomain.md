# openapi_client.model.top_level_domain.TopLevelDomain

Доменная зона.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Доменная зона. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_registered** | bool,  | BoolClass,  | Это логическое значение, которое показывает, зарегистрирована ли доменная зона. | 
**registrar** | str,  | str,  | Регистратор доменной зоны. | must be one of ["NIC", "PDR", "R01", "timeweb", "TimewebVirtreg", "Webnames", "unknown", ] 
**is_whois_privacy_default_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включено ли по умолчанию скрытие данных администратора для доменной зоны. | 
**is_published** | bool,  | BoolClass,  | Это логическое значение, которое показывает, опубликована ли доменная зона. | 
**early_renew_period** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Количество дней до истечение срока регистрации, когда можно продлять домен. | 
**prolong_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Цена продления домена. | 
**whois_privacy_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Цена услуги скрытия данных администратора для доменной зоны. | 
**is_whois_privacy_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, доступно ли управление скрытием данных администратора для доменной зоны. | 
**grace_period** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество дней, которые действует льготный период когда вы ещё можете продлить домен, после окончания его регистрации | 
**[allowed_buy_periods](#allowed_buy_periods)** | list, tuple,  | tuple,  | Список доступных периодов для регистрации/продления доменов со стоимостью. | 
**transfer** | decimal.Decimal, int, float,  | decimal.Decimal,  | Цена услуги трансфера домена. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Цена регистрации домена | 
**name** | str,  | str,  | Имя доменной зоны. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор доменной зоны. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allowed_buy_periods

Список доступных периодов для регистрации/продления доменов со стоимостью.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список доступных периодов для регистрации/продления доменов со стоимостью. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**period** | str,  | str,  | Период регистрации/продления домена. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Цена регистрации/продления домена. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

