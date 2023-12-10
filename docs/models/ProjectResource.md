# openapi_client.model.project_resource.ProjectResource

Ресурс проекта

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Ресурс проекта | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан ресурс. | 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | 
**resource_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор ресурса проекта (сервера, хранилища, кластера, балансировщика, базы данных или выделенного сервера). | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого ресурса проекта. Автоматически генерируется при создании. | 
**type** | str,  | str,  | Тип ресурса проекта | must be one of ["server", "balancer", "database", "kubernetes", "storage", "dedicated", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

