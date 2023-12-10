# openapi_client.model.bucket.Bucket

Хранилище S3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Хранилище S3 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**secret_key** | str,  | str,  | Секретный ключ доступа от хранилища. | 
**hostname** | str,  | str,  | Адрес хранилища для подключения. | 
**preset_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Идентификатор тарифа хранилища. | 
**access_key** | str,  | str,  | Ключ доступа от хранилища. | 
**[disk_stats](#disk_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Статистика использования диска хранилища. | 
**name** | str,  | str,  | Удобочитаемое имя, установленное для хранилища. | 
**location** | str,  | str,  | Регион хранилища. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра хранилища. Автоматически генерируется при создании. | 
**type** | str,  | str,  | Тип хранилища. | must be one of ["private", "public", ] 
**object_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество файлов в хранилище. | 
**status** | str,  | str,  | Статус хранилища. | must be one of ["no_paid", "created", "transfer", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# disk_stats

Статистика использования диска хранилища.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Статистика использования диска хранилища. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) диска хранилища. | 
**used** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) использованного пространства диска хранилища. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

