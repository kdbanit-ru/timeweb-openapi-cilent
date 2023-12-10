# openapi_client.model.invoice.Invoice

Оплата заявки на продление/регистрацию домена при помощи платежной системы

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Оплата заявки на продление/регистрацию домена при помощи платежной системы | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payment_type** | str,  | str,  | Тип платежной системы. | must be one of ["receipt", "card", "mobile-card", "wm", "webmoney", "yandex", "ya", "invoice", "sofort", "qiwi_wallet", "wechat", ] 
**money_source** | str,  | str,  | Тип создаваемой заявки. | must be one of ["invoice", ] 
**payer_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификационный номер плательщика | 
**person_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

