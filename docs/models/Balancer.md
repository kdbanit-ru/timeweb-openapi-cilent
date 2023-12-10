# openapi_client.model.balancer.Balancer

Балансировщик

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Балансировщик | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inter** | decimal.Decimal, int, float,  | decimal.Decimal,  | Интервал проверки. | 
**ip** | None, str,  | NoneClass, str,  | IP-адрес сетевого интерфейса IPv4. | 
**is_sticky** | bool,  | BoolClass,  | Это логическое значение, которое показывает, сохраняется ли сессия. | 
**created_at** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан балансировщик. | value must conform to RFC-3339 date-time
**[rules](#rules)** | list, tuple,  | tuple,  |  | 
**[ips](#ips)** | list, tuple,  | tuple,  | Список IP-адресов, привязанных к балансировщику | 
**timeout** | decimal.Decimal, int, float,  | decimal.Decimal,  | Таймаут ответа балансировщика. | 
**local_ip** | None, str,  | NoneClass, str,  | Локальный IP-адрес сетевого интерфейса IPv4. | 
**path** | str,  | str,  | Адрес балансировщика. | 
**fall** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества ошибок. | 
**port** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порт балансировщика. | 
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор тарифа. | 
**proto** | str,  | str,  | Протокол. | must be one of ["http", "http2", "https", "tcp", ] 
**is_use_proxy** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | 
**name** | str,  | str,  | Удобочитаемое имя, установленное для балансировщика. | 
**is_ssl** | bool,  | BoolClass,  | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | 
**location** | str,  | str,  | Географическое расположение балансировщика | must be one of ["ru-1", "pl-1", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра балансировщика. Автоматически генерируется при создании. | 
**is_keepalive** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | 
**rise** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества успешных ответов. | 
**algo** | str,  | str,  | Алгоритм переключений балансировщика. | must be one of ["roundrobin", "leastconn", ] 
**status** | str,  | str,  | Статус балансировщика. | must be one of ["started", "stoped", "starting", "no_paid", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Rule**](Rule.md) | [**Rule**](Rule.md) | [**Rule**](Rule.md) |  | 

# ips

Список IP-адресов, привязанных к балансировщику

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список IP-адресов, привязанных к балансировщику | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

