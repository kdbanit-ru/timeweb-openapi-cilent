# openapi_client.model.presets_dbs.PresetsDbs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра тарифа базы данных. | [optional] 
**description** | str,  | str,  | Описание тарифа. | [optional] 
**description_short** | str,  | str,  | Краткое описание тарифа. | [optional] 
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Описание процессора тарифа. | [optional] 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Описание ОЗУ тарифа. | [optional] 
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Описание диска тарифа. | [optional] 
**type** | str,  | str,  | Тип тарифа базы данных | [optional] must be one of ["mysql", "mysql5", "postgres", "redis", "mongodb", ] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость тарифа базы данных | [optional] 
**location** | str,  | str,  | Географическое расположение тарифа. | [optional] must be one of ["ru-1", "pl-1", "kz-1", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

