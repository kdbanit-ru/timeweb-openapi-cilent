# openapi_client.model.domain_prolong.DomainProlong

Заявка на продление домена

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Заявка на продление домена | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fqdn** | str,  | str,  | Полное имя домена. | 
**action** | str,  | str,  | Тип создаваемой заявки. | must be one of ["prolong", ] 
**is_antispam_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает включена ли услуга \&quot;Антиспам\&quot; для домена | [optional] 
**is_autoprolong_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включено ли автопродление домена. | [optional] 
**is_whois_privacy_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Опция недоступна для доменов в зонах .ru и .рф. | [optional] 
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | [optional] 
**person_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**prime** | [**DomainPrimeType**](DomainPrimeType.md) | [**DomainPrimeType**](DomainPrimeType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

