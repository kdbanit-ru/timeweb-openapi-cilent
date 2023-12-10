# openapi_client.model.dedicated_server.DedicatedServer

Выделенный сервер

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Выделенный сервер | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cpu_description** | str,  | str,  | Описание параметров процессора выделенного сервера. | 
**autoinstall_ready** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество готовых к автоматической выдаче серверов. Если значение равно 0, сервер будет установлен через инженеров. | 
**ip** | None, str,  | NoneClass, str,  | IP-адрес сетевого интерфейса IPv4. | 
**os_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор операционной системы, установленной на выделенный сервер. | 
**created_at** | str, datetime,  | str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан выделенный сервер. | value must conform to RFC-3339 date-time
**cp_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор панели управления, установленной на выделенный сервер. | 
**bandwidth_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор интернет-канала, установленного на выделенный сервер. | 
**ipmi_login** | None, str,  | NoneClass, str,  | Логин, используемый для входа в IPMI-консоль. | 
**[additional_ip_addr_id](#additional_ip_addr_id)** | list, tuple, None,  | tuple, NoneClass,  | Массив уникальных идентификаторов дополнительных IP-адресов, подключенных к выделенному серверу. | 
**ram_description** | str,  | str,  | Описание ОЗУ выделенного сервера. | 
**vnc_pass** | None, str,  | NoneClass, str,  | Пароль для подключения к VNC-консоли выделенного сервера. | 
**hdd_description** | str,  | str,  | Описание параметров жёсткого диска выделенного сервера. | 
**ipmi_password** | None, str,  | NoneClass, str,  | Пароль, используемый для входа в IPMI-консоль. | 
**[network_drive_id](#network_drive_id)** | list, tuple, None,  | tuple, NoneClass,  | Массив уникальных идентификаторов сетевых дисков, подключенных к выделенному серверу. | 
**ipv6** | None, str,  | NoneClass, str,  | IP-адрес сетевого интерфейса IPv6. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Стоимость выделенного сервера. | 
**name** | str,  | str,  | Удобочитаемое имя, установленное для выделенного сервера. | 
**comment** | str,  | str,  | Комментарий к выделенному серверу. | 
**location** | str,  | str,  | Локация сервера. | must be one of ["ru-1", "pl-1", "kz-1", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра выделенного сервера. Автоматически генерируется при создании. | 
**ipmi_ip** | None, str,  | NoneClass, str,  | IP-адрес сетевого интерфейса IPMI. | 
**plan_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор списка дополнительных услуг выделенного сервера. | 
**node_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Внутренний дополнительный идентификатор сервера. | 
**status** | str,  | str,  | Строка состояния, указывающая состояние выделенного сервера. Может быть «installing», «installed», «on» или «off». | must be one of ["installing", "installed", "on", "off", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# network_drive_id

Массив уникальных идентификаторов сетевых дисков, подключенных к выделенному серверу.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Массив уникальных идентификаторов сетевых дисков, подключенных к выделенному серверу. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# additional_ip_addr_id

Массив уникальных идентификаторов дополнительных IP-адресов, подключенных к выделенному серверу.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Массив уникальных идентификаторов дополнительных IP-адресов, подключенных к выделенному серверу. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

