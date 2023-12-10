# openapi_client.model.finances.Finances

Платежная информация

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Платежная информация | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**monthly_cost** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость услуг на аккаунте в месяц. | 
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Баланс аккаунта. | 
**monthly_fee** | decimal.Decimal, int, float,  | decimal.Decimal,  | Абонентская плата в месяц (с учетом скидок). | 
**total_paid** | decimal.Decimal, int, float,  | decimal.Decimal,  | Общая сумма платежей на аккаунте. | 
**hourly_cost** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость услуг на аккаунте в час. | 
**currency** | str,  | str,  | Валюта, которая используется на аккаунте. | 
**hourly_fee** | decimal.Decimal, int, float,  | decimal.Decimal,  | Абонентская плата в час (с учетом скидок). | 
**hours_left** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Сколько часов работы услуг оплачено на аккаунте. | 
**discount_percent** | decimal.Decimal, int, float,  | decimal.Decimal,  | Процент скидки для аккаунта. | 
**autopay_card_info** | None, str,  | NoneClass, str,  | Информация о карте, используемой для автоплатежей. | 
**discount_end_date_at** | None, str,  | NoneClass, str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда заканчивается скидка для аккаунта. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

