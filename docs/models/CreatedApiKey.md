# openapi_client.model.created_api_key.CreatedApiKey

Токен.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Токен. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Имя токена. | 
**created_at** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан токен. | value must conform to RFC-3339 date-time
**expired_at** | None, str, datetime,  | NoneClass, str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда истекает токен. | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  | Уникальный идентификатор токена. | value must be a uuid
**token** | str,  | str,  | Созданный токен, будет показан только один раз, его необходимо сохранить. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

