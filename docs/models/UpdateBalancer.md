# openapi_client.model.update_balancer.UpdateBalancer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Удобочитаемое имя, установленное для балансировщика. | [optional] 
**algo** | str,  | str,  | Алгоритм переключений балансировщика. | [optional] must be one of ["roundrobin", "leastconn", ] 
**is_sticky** | bool,  | BoolClass,  | Это логическое значение, которое показывает, сохраняется ли сессия. | [optional] 
**is_use_proxy** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | [optional] 
**is_ssl** | bool,  | BoolClass,  | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | [optional] 
**is_keepalive** | bool,  | BoolClass,  | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | [optional] 
**proto** | str,  | str,  | Протокол. | [optional] must be one of ["http", "http2", "https", "tcp", ] 
**port** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порт балансировщика. | [optional] 
**path** | str,  | str,  | Адрес балансировщика. | [optional] 
**inter** | decimal.Decimal, int, float,  | decimal.Decimal,  | Интервал проверки. | [optional] 
**timeout** | decimal.Decimal, int, float,  | decimal.Decimal,  | Таймаут ответа балансировщика. | [optional] 
**fall** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества ошибок. | [optional] 
**rise** | decimal.Decimal, int, float,  | decimal.Decimal,  | Порог количества успешных ответов. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

