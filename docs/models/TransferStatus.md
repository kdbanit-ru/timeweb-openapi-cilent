# openapi_client.model.transfer_status.TransferStatus

Статус трансфера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Статус трансфера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tries** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество попыток. | 
**uploaded_count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество перемещенных объектов. | 
**total_count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Общее количество затронутых объектов. | 
**total_size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Общий размер затронутых объектов. | 
**uploaded_size** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер перемещенных объектов. | 
**[errors](#errors)** | list, tuple,  | tuple,  |  | 
**status** | str,  | str,  | Общий статус трансфера. | must be one of ["started", "suspended", "failed", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**try** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество попыток. | 
**value** | str,  | str,  | Текст ошибки. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

