# openapi_client.model.update_db.UpdateDb

Дополнительные параметры конфигурации базы данных.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Дополнительные параметры конфигурации базы данных. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  | Пароль для подключения к базе данных. | [optional] 
**name** | str,  | str,  | Название базы данных. | [optional] 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа. | [optional] 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**is_external_ip** | bool,  | BoolClass,  | Использовать или нет внешний ip. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

