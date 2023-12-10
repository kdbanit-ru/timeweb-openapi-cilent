# openapi_client.model.mailbox.Mailbox

Почтовый ящик

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Почтовый ящик | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  | Пароль почтового ящика | 
**[auto_reply](#auto_reply)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Автоответчик на входящие письма | 
**[forwarding_outgoing](#forwarding_outgoing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка исходящих писем | 
**mailbox** | str,  | str,  | Название почтового ящика | 
**fqdn** | str,  | str,  | Домен почты | 
**is_webmail** | bool,  | BoolClass,  | Доступен ли Webmail | 
**comment** | str,  | str,  | Комментарий к почтовому ящику | 
**idn_name** | str,  | str,  | IDN домен почтового ящика | 
**[spam_filter](#spam_filter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Спам-фильтр | 
**is_dovecot** | bool,  | BoolClass,  | Есть ли доступ через dovecot | 
**usage_space** | decimal.Decimal, int, float,  | decimal.Decimal,  | Использованное место на почтовом ящике (в Мб) | 
**[forwarding_incoming](#forwarding_incoming)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка входящик писем | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# auto_reply

Автоответчик на входящие письма

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Автоответчик на входящие письма | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_enabled** | bool,  | BoolClass,  | Включен ли автоответчик на входящие письма | 
**subject** | str,  | str,  | Тема сообщения автоответчика на входящие письма | 
**message** | str,  | str,  | Сообщение автоответчика на входящие письма | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# spam_filter

Спам-фильтр

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Спам-фильтр | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_enabled** | bool,  | BoolClass,  | Включен ли спам-фильтр | 
**[white_list](#white_list)** | list, tuple,  | tuple,  | Белый список адресов от которых письма не будут попадать в спам | 
**forward_to** | str,  | str,  | Адрес для пересылки при выбранном действии &#x60;forward&#x60; из параметра &#x60;action&#x60; | 
**action** | str,  | str,  | Что делать с письмами, которые попадают в спам. \\  Параметры: \\  &#x60;move_to_directory&#x60; - переместить в паку спам; \\  &#x60;forward&#x60; - переслать письмо на другой адрес; \\  &#x60;delete&#x60; - удалить письмо; \\  &#x60;tag&#x60; - пометить письмо; | must be one of ["move_to_directory", "forward", "delete", "tag", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# white_list

Белый список адресов от которых письма не будут попадать в спам

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Белый список адресов от которых письма не будут попадать в спам | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# forwarding_incoming

Пересылка входящик писем

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка входящик писем | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_enabled** | bool,  | BoolClass,  | Включена ли пересылка входящик писем | 
**is_delete_messages** | bool,  | BoolClass,  | Удалять ли входящие письма | 
**[incoming_list](#incoming_list)** | list, tuple,  | tuple,  | Список адресов для пересылки | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# incoming_list

Список адресов для пересылки

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Список адресов для пересылки | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# forwarding_outgoing

Пересылка исходящих писем

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Пересылка исходящих писем | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_enabled** | bool,  | BoolClass,  | Включена ли пересылка исходящих писем | 
**outgoing_to** | str,  | str,  | Адрес для пересылки исходящих писем | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

