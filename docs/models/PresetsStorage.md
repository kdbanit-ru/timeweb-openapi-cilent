# openapi_client.model.presets_storage.PresetsStorage

Тариф

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Тариф | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description_short** | str,  | str,  | Краткое описание тарифа. | 
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Описание диска хранилища. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость тарифа хранилища. | 
**description** | str,  | str,  | Описание тарифа. | 
**location** | str,  | str,  | Географическое расположение тарифа. | must be one of ["ru-1", "pl-1", "kz-1", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра тарифа хранилища. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

