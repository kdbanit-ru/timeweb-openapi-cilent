# openapi_client.model.create_balancer.CreateBalancer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inter** | decimal.Decimal, int, float,  | decimal.Decimal,  | Интервал проверки. | 
**is_sticky** | bool,  | BoolClass,  | Это логическое значение, которое показывает, сохраняется ли сессия. | 
**timeout** | decimal.Decimal, int, float,  | decimal.Decimal,  | Таймаут ответа балансировщика. | 
**path** | str,  | str,  | Адрес балансировщика. | 
**fall** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества ошибок. | 
**port** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порт балансировщика. | 
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Идентификатор тарифа. | 
**proto** | str,  | str,  | Протокол. | must be one of ["http", "http2", "https", "tcp", ] 
**is_use_proxy** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | 
**name** | str,  | str,  | Удобочитаемое имя, установленное для балансировщика. | 
**is_ssl** | bool,  | BoolClass,  | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | 
**is_keepalive** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | 
**rise** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества успешных ответов. | 
**algo** | str,  | str,  | Алгоритм переключений балансировщика. | must be one of ["roundrobin", "leastconn", ] 
**network** | [**Network**](Network.md) | [**Network**](Network.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

