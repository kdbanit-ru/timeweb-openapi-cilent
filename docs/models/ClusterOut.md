# openapi_client.model.cluster_out.ClusterOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ingress** | bool,  | BoolClass,  | Логическое значение, показывающее, включен ли Ingress | 
**network_driver** | str,  | str,  | Используемый сетевой драйвер | 
**k8s_version** | str,  | str,  | Версия Kubernetes | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа мастер-ноды | 
**name** | str,  | str,  | Название | 
**created_at** | str, datetime,  | str,  | Дата и время создания кластера в формате ISO8601 | value must conform to RFC-3339 date-time
**description** | str,  | str,  | Описание | 
**ha** | bool,  | BoolClass,  | Описание появится позже | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Уникальный идентификатор кластера | 
**status** | str,  | str,  | Статус | 
**cpu** | decimal.Decimal, int,  | decimal.Decimal,  | Общее количество ядер | [optional] if omitted the server will use the default value of 0
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | Общее количество памяти | [optional] if omitted the server will use the default value of 0
**disk** | decimal.Decimal, int,  | decimal.Decimal,  | Общее дисковое пространство | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

