# openapi_client.model.forwarding_incoming_is_disabled.ForwardingIncomingIsDisabled

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_enabled** | bool,  | BoolClass,  | Включена ли пересылка входящик писем | 
**is_delete_messages** | bool,  | BoolClass,  | Удалять ли входящие письма | [optional] 
**[incoming_list](#incoming_list)** | list, tuple,  | tuple,  | Список адресов для пересылки. Не должен быть пустым при передачи параметра &#x60;is_enabled&#x60;: &#x60;true&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# incoming_list

Список адресов для пересылки. Не должен быть пустым при передачи параметра `is_enabled`: `true`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список адресов для пересылки. Не должен быть пустым при передачи параметра &#x60;is_enabled&#x60;: &#x60;true&#x60; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

