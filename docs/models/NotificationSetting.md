# openapi_client.model.notification_setting.NotificationSetting

Статус аккаунта

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Статус аккаунта | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[channels](#channels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Каналы отправки уведомления. | 
**type** | [**NotificationSettingType**](NotificationSettingType.md) | [**NotificationSettingType**](NotificationSettingType.md) |  | 
**group** | str,  | str,  | Строка, указывающая название группы уведомления. Может быть «security», «monitoring» или «finances». | must be one of ["security", "monitoring", "finances", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# channels

Каналы отправки уведомления.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Каналы отправки уведомления. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sms** | [**NotificationSettingChannel**](NotificationSettingChannel.md) | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 
**telegram** | [**NotificationSettingChannel**](NotificationSettingChannel.md) | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 
**email** | [**NotificationSettingChannel**](NotificationSettingChannel.md) | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

