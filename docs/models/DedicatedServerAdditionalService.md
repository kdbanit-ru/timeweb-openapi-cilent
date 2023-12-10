# openapi_client.model.dedicated_server_additional_service.DedicatedServerAdditionalService

Дополнительная услуга для выделенного сервера

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Дополнительная услуга для выделенного сервера | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**short_description** | str,  | str,  | Краткое описание дополнительной услуги выделенного сервера. | 
**period** | str,  | str,  | Период оплаты. | must be one of ["P1D", "P1M", "P3M", "P6M", "P1Y", "forever", ] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость (в рублях) дополнительной услуги для выделенного сервера. | 
**name** | str,  | str,  | Уникально имя дополнительной услуги выделенного сервера. | 
**description** | str,  | str,  | Описание дополнительной услуги выделенного сервера. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор дополнительной услуги для выделенного сервера. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

