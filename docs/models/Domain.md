# openapi_client.model.domain.Domain

Домен

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Домен | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_status** | None, str,  | NoneClass, str,  | Статус заявки на продление/регистрацию/трансфер домена. | must be one of ["prolongation_fail", "prolongation_request", "registration_fail", "registration_request", "transfer_fail", "transfer_request", "awaiting_person", ] 
**days_left** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество дней, оставшихся до конца срока регистрации домена. | 
**fqdn** | str,  | str,  | Полное имя домена. | 
**is_whois_privacy_enabled** | None, bool,  | NoneClass, BoolClass,  | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Если приходит null, значит для данной зоны эта услуга не доступна. | 
**paid_till** | None, str,  | NoneClass, str,  | До какого числа оплачен домен. | 
**[allowed_buy_periods](#allowed_buy_periods)** | list, tuple,  | tuple,  | Допустимые периоды продления домена. | 
**linked_ip** | None, str,  | NoneClass, str,  | Привязанный к домену IP-адрес. | 
**[subdomains](#subdomains)** | list, tuple,  | tuple,  | Список поддоменов. | 
**is_autoprolong_enabled** | None, bool,  | NoneClass, BoolClass,  | Это логическое значение, которое показывает, включено ли автопродление домена. | 
**is_premium** | bool,  | BoolClass,  | Это логическое значение, которое показывает, является ли домен премиальным. | 
**domain_status** | str,  | str,  | Статус домена. | must be one of ["awaiting_payment", "expired", "final_expired", "free", "no_paid", "ns_based", "paid", "soon_expire", "today_expired", ] 
**is_prolong_allowed** | bool,  | BoolClass,  | Это логическое значение, которое показывает, можно ли сейчас продлить домен. | 
**provider** | None, str,  | NoneClass, str,  | Идентификатор регистратора домена. | 
**premium_prolong_cost** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Стоимость премиального домена. | 
**expiration** | str,  | str,  | Дата окончания срока регистрации домена, для доменов без срока окончания регистрации будет приходить 0000-00-00. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор домена. | 
**is_technical** | bool,  | BoolClass,  | Это логическое значение, которое показывает, является ли домен техническим. | 
**tld_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Идентификатор доменной зоны. | 
**person_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Идентификатор администратора, на которого зарегистрирован домен. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allowed_buy_periods

Допустимые периоды продления домена.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Допустимые периоды продления домена. | 

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
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость домена за указанный период. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subdomains

Список поддоменов.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список поддоменов. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Subdomain**](Subdomain.md) | [**Subdomain**](Subdomain.md) | [**Subdomain**](Subdomain.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

