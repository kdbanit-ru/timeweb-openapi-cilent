# openapi_client.model.vds.Vds

Сервер

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Сервер | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[image](#image)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Образ сервера. | 
**[disks](#disks)** | list, tuple,  | tuple,  | Список дисков сервера. | 
**[os](#os)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Операционная система сервера. | 
**[software](#software)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | ПО из маркетплейса. | 
**qemu_agent** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора сервера. | 
**created_at** | str,  | str,  | Дата создания сервера в формате ISO8061. | 
**cloud_init** | None, str,  | NoneClass, str,  | Cloud-init скрипт. | 
**[networks](#networks)** | list, tuple,  | tuple,  | Список сетей диска. | 
**start_at** | None, str, datetime,  | NoneClass, str,  | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был запущен сервер. | value must conform to RFC-3339 date-time
**avatar_id** | None, str,  | NoneClass, str,  | Уникальный идентификатор аватара сервера. Описание методов работы с аватарами появится позднее. | 
**vnc_pass** | str,  | str,  | Пароль от VNC. | 
**preset_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор тарифа сервера. | 
**boot_mode** | str,  | str,  | Режим загрузки ОС сервера. | must be one of ["std", "single", "cd", ] 
**name** | str,  | str,  | Удобочитаемое имя, установленное для выделенного сервера. | 
**comment** | str,  | str,  | Комментарий к выделенному серверу. | 
**configurator_id** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Уникальный идентификатор конфигуратора сервера. | 
**location** | str,  | str,  | Локация сервера. | must be one of ["ru-1", "ru-2", "pl-1", "kz-1", ] 
**cpu_frequency** | str,  | str,  | Частота ядер процессора сервера. | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор для каждого экземпляра сервера. Автоматически генерируется при создании. | 
**is_ddos_guard** | bool,  | BoolClass,  | Это логическое значение, которое показывает, включена ли защита от DDOS у данного сервера. | 
**root_pass** | None, str,  | NoneClass, str,  | Пароль root сервера или пароль Администратора для серверов Windows. | 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер (в Мб) ОЗУ сервера. | 
**status** | str,  | str,  | Статус сервера. | must be one of ["installing", "software_install", "reinstalling", "on", "off", "turning_on", "turning_off", "hard_turning_off", "rebooting", "hard_rebooting", "removing", "removed", "cloning", "transfer", "blocked", "configuring", "no_paid", "permanent_blocked", ] 
**is_qemu_agent** | bool,  | BoolClass,  | Включен ли QEMU-agent на сервере. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# os

Операционная система сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Операционная система сервера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Тип операционной системы. | must be one of ["bitrix", "brainycp", "centos", "debian", "fedora", "freebsd", "gentoo", "routeros", "ubuntu", "windows", ] 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор операционной системы. | 
**version** | None, str,  | NoneClass, str,  | Версия операционной системы. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# software

ПО из маркетплейса.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | ПО из маркетплейса. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор ПО из маркетплейса. | [optional] 
**name** | str,  | str,  | Название ПО из маркетплейса. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# disks

Список дисков сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список дисков сервера. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# image

Образ сервера.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Образ сервера. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Название образа сервера. | 
**is_custom** | bool,  | BoolClass,  | Является ли образ кастомным. | 
**id** | str,  | str,  | Уникальный идентификатор образа сервера. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# networks

Список сетей диска.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список сетей диска. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

