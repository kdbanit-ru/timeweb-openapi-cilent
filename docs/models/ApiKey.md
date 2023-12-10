# openapi_client.model.api_key.ApiKey

Токен.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Токен. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_able_to_delete** | bool,  | BoolClass,  | Это логическое значение, которое показывает, можно ли удалять управляемые сервисы при помощи данного токена без подтверждения через Телеграм, когда это подтверждение включено. | 
**name** | str,  | str,  | Имя токена. | 
**created_at** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан токен. | value must conform to RFC-3339 date-time
**expired_at** | None, str, datetime,  | NoneClass, str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда истекает токен. | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  | Уникальный идентификатор токена. | value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

