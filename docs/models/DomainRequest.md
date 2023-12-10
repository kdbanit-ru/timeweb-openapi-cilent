# openapi_client.model.domain_request.DomainRequest

Заявка на продление/регистрацию/трансфер домена.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Заявка на продление/регистрацию/трансфер домена. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | Дата создания заявки. | value must conform to RFC-3339 date-time
**[prime](#prime)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | 
**fqdn** | str,  | str,  | Полное имя домена. | 
**message** | None, str,  | NoneClass, str,  | Информационное сообщение о заявке. | 
**type** | str,  | str,  | Тип заявки. | must be one of ["request", "prolong", "transfer", ] 
**is_antispam_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает включена ли услуга \&quot;Антиспам\&quot; для домена | 
**is_whois_privacy_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Опция недоступна для доменов в зонах .ru и .рф. | 
**auth_code** | None, str,  | NoneClass, str,  | Код авторизации для переноса домена. | 
**error_code_transfer** | None, str,  | NoneClass, str,  | Код ошибки трансфера домена. | 
**is_autoprolong_enabled** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включено ли автопродление домена. | 
**account_id** | str,  | str,  | Идентификатор пользователя | 
**money_source** | None, str,  | NoneClass, str,  | Источник (способ) оплаты заявки. | must be one of ["use", "bonus", "invoice", ] 
**group_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор группы доменных зон. | 
**domain_bundle_id** | None, str,  | NoneClass, str,  | Идентификационный номер бандла, в который входит данная заявка (null - если заявка не входит ни в один бандл). | 
**soon_expire** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество дней до конца регистрации домена, за которые мы уведомим о необходимости продления. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор заявки. | 
**sort_order** | decimal.Decimal, int, float,  | decimal.Decimal,  | Это значение используется для сортировки доменных зон в панели управления. | 
**person_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификационный номер персоны для заявки на регистрацию. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# prime

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DomainPrimeType](DomainPrimeType.md) | [**DomainPrimeType**](DomainPrimeType.md) | [**DomainPrimeType**](DomainPrimeType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

