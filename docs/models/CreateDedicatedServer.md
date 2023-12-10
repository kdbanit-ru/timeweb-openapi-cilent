# openapi_client.model.create_dedicated_server.CreateDedicatedServer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор тарифа выделенного сервера. | 
**name** | str,  | str,  | Удобочитаемое имя выделенного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | 
**payment_period** | str,  | str,  | Период оплаты. | must be one of ["P1M", "P3M", "P6M", "P1Y", ] 
**location** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**plan_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор списка дополнительных услуг выделенного сервера. | 
**os_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор операционной системы, которая будет установлена на выделенный сервер. | [optional] 
**cp_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор панели управления, которая будет установлена на выделенный сервер. | [optional] 
**bandwidth_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор интернет-канала, который будет установлен на выделенный сервер. | [optional] 
**network_drive_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор сетевого диска, который будет установлен на выделенный сервер. | [optional] 
**additional_ip_addr_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор дополнительного IP-адреса, который будет установлен на выделенный сервер. | [optional] 
**comment** | str,  | str,  | Комментарий к выделенному серверу. Максимальная длина — 255 символов. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

