# openapi_client.model.update_server.UpdateServer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[configurator](#configurator)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Параметры конфигурации сервера. Нельзя передавать вместе с &#x60;preset_id&#x60;. | [optional] 
**os_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор операционной системы, которая будет установлена на облачный сервер. | [optional] 
**software_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор программного обеспечения сервера. | [optional] 
**preset_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор тарифа сервера. Нельзя передавать вместе с ключом &#x60;configurator&#x60;. | [optional] 
**bandwidth** | decimal.Decimal, int, float,  | decimal.Decimal,  | Пропускная способность тарифа. Доступные значения от 100 до 1000 с шагом 100. | [optional] 
**name** | str,  | str,  | Имя облачного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | [optional] 
**avatar_id** | str,  | str,  | Уникальный идентификатор аватара сервера. Описание методов работы с аватарами появится позднее. | [optional] 
**comment** | str,  | str,  | Комментарий к облачному серверу. Максимальная длина — 255 символов. | [optional] 
**image_id** | str, uuid.UUID,  | str,  | Уникальный идентификатор образа, который будет установлен на облачный сервер. Нельзя передавать вместе с &#x60;os_id&#x60;. | [optional] value must be a uuid
**cloud_init** | str,  | str,  | Cloud-init скрипт | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# configurator

Параметры конфигурации сервера. Нельзя передавать вместе с `preset_id`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Параметры конфигурации сервера. Нельзя передавать вместе с &#x60;preset_id&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configurator_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Уникальный идентификатор конфигуратора сервера. | [optional] 
**disk** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер диска в МБ. | [optional] 
**cpu** | decimal.Decimal, int, float,  | decimal.Decimal,  | Количество ядер процессора. | [optional] 
**ram** | decimal.Decimal, int, float,  | decimal.Decimal,  | Размер ОЗУ сервера в МБ. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

