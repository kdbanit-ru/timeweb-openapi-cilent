# openapi_client.model.update_mailbox.UpdateMailbox

Изменение почтового ящика

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Изменение почтового ящика | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[auto_reply](#auto_reply)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Автоответчик на входящие письма | [optional] 
**[spam_filter](#spam_filter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Спам-фильтр | [optional] 
**[forwarding_incoming](#forwarding_incoming)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка входящик писем. | [optional] 
**[forwarding_outgoing](#forwarding_outgoing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка исходящих писем | [optional] 
**comment** | str,  | str,  | Комментарий к почтовому ящику | [optional] 
**password** | str,  | str,  | Пароль почтового ящика | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# auto_reply

Автоответчик на входящие письма

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Автоответчик на входящие письма | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AutoReplyIsDisabled](AutoReplyIsDisabled.md) | [**AutoReplyIsDisabled**](AutoReplyIsDisabled.md) | [**AutoReplyIsDisabled**](AutoReplyIsDisabled.md) |  | 
[AutoReplyIsEnabled](AutoReplyIsEnabled.md) | [**AutoReplyIsEnabled**](AutoReplyIsEnabled.md) | [**AutoReplyIsEnabled**](AutoReplyIsEnabled.md) |  | 

# spam_filter

Спам-фильтр

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Спам-фильтр | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SpamFilterIsDisabled](SpamFilterIsDisabled.md) | [**SpamFilterIsDisabled**](SpamFilterIsDisabled.md) | [**SpamFilterIsDisabled**](SpamFilterIsDisabled.md) |  | 
[SpamFilterIsEnabled](SpamFilterIsEnabled.md) | [**SpamFilterIsEnabled**](SpamFilterIsEnabled.md) | [**SpamFilterIsEnabled**](SpamFilterIsEnabled.md) |  | 

# forwarding_incoming

Пересылка входящик писем.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка входящик писем. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ForwardingIncomingIsDisabled](ForwardingIncomingIsDisabled.md) | [**ForwardingIncomingIsDisabled**](ForwardingIncomingIsDisabled.md) | [**ForwardingIncomingIsDisabled**](ForwardingIncomingIsDisabled.md) |  | 
[ForwardingIncomingIsEnabled](ForwardingIncomingIsEnabled.md) | [**ForwardingIncomingIsEnabled**](ForwardingIncomingIsEnabled.md) | [**ForwardingIncomingIsEnabled**](ForwardingIncomingIsEnabled.md) |  | 

# forwarding_outgoing

Пересылка исходящих писем

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка исходящих писем | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ForwardingOutgoingIsDisabled](ForwardingOutgoingIsDisabled.md) | [**ForwardingOutgoingIsDisabled**](ForwardingOutgoingIsDisabled.md) | [**ForwardingOutgoingIsDisabled**](ForwardingOutgoingIsDisabled.md) |  | 
[ForwardingOutgoingIsEnabled](ForwardingOutgoingIsEnabled.md) | [**ForwardingOutgoingIsEnabled**](ForwardingOutgoingIsEnabled.md) | [**ForwardingOutgoingIsEnabled**](ForwardingOutgoingIsEnabled.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

