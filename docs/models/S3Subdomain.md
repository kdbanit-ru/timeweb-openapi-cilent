# openapi_client.model.s3_subdomain.S3Subdomain

Поддомен.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Поддомен. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cert_released** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был выдан SSL сертификат. | value must conform to RFC-3339 date-time
**tries** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество попыток перевыпустить SSL сертификат. | 
**subdomain** | str,  | str,  | Поддомен. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор поддомена. | 
**status** | str,  | str,  | Поддомен. | must be one of ["ssl_released", "ssl_not_requested", "ssl_re_release_error", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

