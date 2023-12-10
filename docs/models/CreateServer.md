# openapi_client.model.create_server.CreateServer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bandwidth** | decimal.Decimal, int, float,  | decimal.Decimal,  | Пропускная способность тарифа. Доступные значения от 100 до 1000 с шагом 100. | 
**name** | str,  | str,  | Имя облачного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | 
**is_ddos_guard** | bool,  | BoolClass,  | Защита от DDoS. Серверу выдается защищенный IP-адрес с защитой уровня L3 / L4. Для включения защиты уровня L7 необходимо создать тикет в техническую поддержку. | 
**[configuration](#configuration)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Параметры конфигурации сервера. Нельзя передавать вместе с &#x60;preset_id&#x60;. | [optional] 
**os_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор операционной системы, которая будет установлена на облачный сервер. Нельзя передавать вместе с &#x60;image_id&#x60;. | [optional] 
**image_id** | str, uuid.UUID,  | str,  | Уникальный идентификатор образа, который будет установлен на облачный сервер. Нельзя передавать вместе с &#x60;os_id&#x60;. | [optional] value must be a uuid
**software_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор программного обеспечения сервера. | [optional] 
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор тарифа сервера. Нельзя передавать вместе с ключом &#x60;configurator&#x60;. | [optional] 
**avatar_id** | str,  | str,  | Уникальный идентификатор аватара сервера. Описание методов работы с аватарами появится позднее. | [optional] 
**comment** | str,  | str,  | Комментарий к облачному серверу. Максимальная длина — 255 символов. | [optional] 
**[ssh_keys_ids](#ssh_keys_ids)** | list, tuple,  | tuple,  | Список SSH-ключей. | [optional] 
**is_local_network** | bool,  | BoolClass,  | Локальная сеть. | [optional] 
**network** | [**Network**](Network.md) | [**Network**](Network.md) |  | [optional] 
**cloud_init** | str,  | str,  | Cloud-init скрипт | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# configuration

Параметры конфигурации сервера. Нельзя передавать вместе с `preset_id`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Параметры конфигурации сервера. Нельзя передавать вместе с &#x60;preset_id&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер диска в МБ. | 
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора. | 
**configurator_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор конфигуратора сервера. | 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер ОЗУ сервера в МБ. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssh_keys_ids

Список SSH-ключей.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список SSH-ключей. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

