# openapi_client.model.project.Project

Проект

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Проект | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avatar_id** | None, str,  | NoneClass, str,  | Идентификатор аватара пользователя. Описание методов работы с аватарами появится позднее. | 
**account_id** | str,  | str,  | Идентификатор пользователя. | 
**name** | str,  | str,  | Удобочитаемое имя проекта. | 
**description** | str,  | str,  | Описание проекта. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого проекта. Автоматически генерируется при создании. | 
**is_default** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выбран ли проект по умолчанию для создания новых сущностей. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

