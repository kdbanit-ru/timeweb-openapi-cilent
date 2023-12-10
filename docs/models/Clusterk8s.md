# openapi_client.model.clusterk8s.Clusterk8s

Кластер

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Кластер | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора кластера. | 
**created_at** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан кластер. | value must conform to RFC-3339 date-time
**description** | str,  | str,  | Описание кластера. | 
**ingress** | bool,  | BoolClass,  | Описание появится позднее. | 
**network_driver** | str,  | str,  | Описание появится позднее. | 
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Гб) диска кластера. | 
**k8s_version** | str,  | str,  | Версия k8s. | 
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Тип сервиса кластера. | 
**name** | str,  | str,  | Удобочитаемое имя, установленное для кластера. | 
**ha** | bool,  | BoolClass,  | Описание появится позднее. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра крастера. Автоматически генерируется при создании. | 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество (в Мб) оперативной памяти кластера. | 
**status** | str,  | str,  | Статус кластера. | must be one of ["installing", "provisioning", "active", "unpaid", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

