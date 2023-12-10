# openapi_client.model.db.Db

База данных

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | База данных | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) | [**ConfigParameters**](ConfigParameters.md) |  | 
**ip** | None, str,  | NoneClass, str,  | IP-адрес сетевого интерфейса IPv4. | 
**created_at** | str,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**is_only_local_ip_access** | bool,  | BoolClass,  | Это логическое значение, которое показывает, доступна ли база данных только по локальному IP адресу. | 
**login** | str,  | str,  | Логин для подключения к базе данных. | 
**type** | str,  | str,  | Тип базы данных. | must be one of ["mysql", "mysql5", "postgres", "redis", "mongodb", ] 
**local_ip** | None, str,  | NoneClass, str,  | IP-адрес локального сетевого интерфейса IPv4. | 
**password** | str,  | str,  | Пароль для подключения к базе данных. | 
**account_id** | str,  | str,  | Идентификатор пользователя. | 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Порт | 
**preset_id** | decimal.Decimal, int,  | decimal.Decimal,  | Идентификатор тарифа. | 
**[disk_stats](#disk_stats)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Статистика использования диска базы данных. | 
**host** | None, str,  | NoneClass, str,  | Хост. | 
**name** | str,  | str,  | Название базы данных. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**hash_type** | None, str,  | NoneClass, str,  | Тип хеширования базы данных (mysql5 | mysql | postgres). | must be one of ["caching_sha2", "mysql_native", None, ] 
**status** | str,  | str,  | Текущий статус базы данных. | must be one of ["started", "starting", "stoped", "no_paid", ] 
**location** | str,  | str,  | Локация сервера. | [optional] must be one of ["ru-1", "ru-2", "pl-1", "kz-1", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# disk_stats

Статистика использования диска базы данных.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Статистика использования диска базы данных. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) диска базы данных. | 
**used** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Кб) использованного пространства диска базы данных. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

