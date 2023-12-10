# openapi_client.model.image_url_auth.ImageUrlAuth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Токен доступа к API облачного хранилища | 
**refresh_token** | str,  | str,  | Токен обновления доступов к API | [optional] 
**expiry** | str, datetime,  | str,  | Время истечения работы токена доступа | [optional] value must conform to RFC-3339 date-time
**token_type** | str,  | str,  | Тип токена доступа | [optional] if omitted the server will use the default value of "Bearer"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

