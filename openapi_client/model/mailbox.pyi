# coding: utf-8

"""
    Документация публичного API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@timeweb.cloud
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class Mailbox(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Почтовый ящик
    """


    class MetaOapg:
        required = {
            "password",
            "auto_reply",
            "forwarding_outgoing",
            "mailbox",
            "fqdn",
            "is_webmail",
            "comment",
            "idn_name",
            "spam_filter",
            "is_dovecot",
            "usage_space",
            "forwarding_incoming",
        }
        
        class properties:
            
            
            class auto_reply(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "is_enabled",
                        "subject",
                        "message",
                    }
                    
                    class properties:
                        is_enabled = schemas.BoolSchema
                        message = schemas.StrSchema
                        subject = schemas.StrSchema
                        __annotations__ = {
                            "is_enabled": is_enabled,
                            "message": message,
                            "subject": subject,
                        }
                
                is_enabled: MetaOapg.properties.is_enabled
                subject: MetaOapg.properties.subject
                message: MetaOapg.properties.message
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_enabled", "message", "subject", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_enabled", "message", "subject", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
                    subject: typing.Union[MetaOapg.properties.subject, str, ],
                    message: typing.Union[MetaOapg.properties.message, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'auto_reply':
                    return super().__new__(
                        cls,
                        *_args,
                        is_enabled=is_enabled,
                        subject=subject,
                        message=message,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class spam_filter(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "is_enabled",
                        "white_list",
                        "forward_to",
                        "action",
                    }
                    
                    class properties:
                        is_enabled = schemas.BoolSchema
                        
                        
                        class action(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def MOVE_TO_DIRECTORY(cls):
                                return cls("move_to_directory")
                            
                            @schemas.classproperty
                            def FORWARD(cls):
                                return cls("forward")
                            
                            @schemas.classproperty
                            def DELETE(cls):
                                return cls("delete")
                            
                            @schemas.classproperty
                            def TAG(cls):
                                return cls("tag")
                        forward_to = schemas.StrSchema
                        
                        
                        class white_list(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'white_list':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "is_enabled": is_enabled,
                            "action": action,
                            "forward_to": forward_to,
                            "white_list": white_list,
                        }
                
                is_enabled: MetaOapg.properties.is_enabled
                white_list: MetaOapg.properties.white_list
                forward_to: MetaOapg.properties.forward_to
                action: MetaOapg.properties.action
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["forward_to"]) -> MetaOapg.properties.forward_to: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["white_list"]) -> MetaOapg.properties.white_list: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_enabled", "action", "forward_to", "white_list", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["forward_to"]) -> MetaOapg.properties.forward_to: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["white_list"]) -> MetaOapg.properties.white_list: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_enabled", "action", "forward_to", "white_list", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
                    white_list: typing.Union[MetaOapg.properties.white_list, list, tuple, ],
                    forward_to: typing.Union[MetaOapg.properties.forward_to, str, ],
                    action: typing.Union[MetaOapg.properties.action, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'spam_filter':
                    return super().__new__(
                        cls,
                        *_args,
                        is_enabled=is_enabled,
                        white_list=white_list,
                        forward_to=forward_to,
                        action=action,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class forwarding_incoming(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "is_enabled",
                        "is_delete_messages",
                        "incoming_list",
                    }
                    
                    class properties:
                        is_enabled = schemas.BoolSchema
                        is_delete_messages = schemas.BoolSchema
                        
                        
                        class incoming_list(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'incoming_list':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "is_enabled": is_enabled,
                            "is_delete_messages": is_delete_messages,
                            "incoming_list": incoming_list,
                        }
                
                is_enabled: MetaOapg.properties.is_enabled
                is_delete_messages: MetaOapg.properties.is_delete_messages
                incoming_list: MetaOapg.properties.incoming_list
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_delete_messages"]) -> MetaOapg.properties.is_delete_messages: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["incoming_list"]) -> MetaOapg.properties.incoming_list: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_enabled", "is_delete_messages", "incoming_list", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_delete_messages"]) -> MetaOapg.properties.is_delete_messages: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["incoming_list"]) -> MetaOapg.properties.incoming_list: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_enabled", "is_delete_messages", "incoming_list", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
                    is_delete_messages: typing.Union[MetaOapg.properties.is_delete_messages, bool, ],
                    incoming_list: typing.Union[MetaOapg.properties.incoming_list, list, tuple, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'forwarding_incoming':
                    return super().__new__(
                        cls,
                        *_args,
                        is_enabled=is_enabled,
                        is_delete_messages=is_delete_messages,
                        incoming_list=incoming_list,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class forwarding_outgoing(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "is_enabled",
                        "outgoing_to",
                    }
                    
                    class properties:
                        is_enabled = schemas.BoolSchema
                        outgoing_to = schemas.StrSchema
                        __annotations__ = {
                            "is_enabled": is_enabled,
                            "outgoing_to": outgoing_to,
                        }
                
                is_enabled: MetaOapg.properties.is_enabled
                outgoing_to: MetaOapg.properties.outgoing_to
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["outgoing_to"]) -> MetaOapg.properties.outgoing_to: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_enabled", "outgoing_to", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["outgoing_to"]) -> MetaOapg.properties.outgoing_to: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_enabled", "outgoing_to", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
                    outgoing_to: typing.Union[MetaOapg.properties.outgoing_to, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'forwarding_outgoing':
                    return super().__new__(
                        cls,
                        *_args,
                        is_enabled=is_enabled,
                        outgoing_to=outgoing_to,
                        _configuration=_configuration,
                        **kwargs,
                    )
            comment = schemas.StrSchema
            fqdn = schemas.StrSchema
            mailbox = schemas.StrSchema
            password = schemas.StrSchema
            usage_space = schemas.NumberSchema
            is_webmail = schemas.BoolSchema
            idn_name = schemas.StrSchema
            is_dovecot = schemas.BoolSchema
            __annotations__ = {
                "auto_reply": auto_reply,
                "spam_filter": spam_filter,
                "forwarding_incoming": forwarding_incoming,
                "forwarding_outgoing": forwarding_outgoing,
                "comment": comment,
                "fqdn": fqdn,
                "mailbox": mailbox,
                "password": password,
                "usage_space": usage_space,
                "is_webmail": is_webmail,
                "idn_name": idn_name,
                "is_dovecot": is_dovecot,
            }
    
    password: MetaOapg.properties.password
    auto_reply: MetaOapg.properties.auto_reply
    forwarding_outgoing: MetaOapg.properties.forwarding_outgoing
    mailbox: MetaOapg.properties.mailbox
    fqdn: MetaOapg.properties.fqdn
    is_webmail: MetaOapg.properties.is_webmail
    comment: MetaOapg.properties.comment
    idn_name: MetaOapg.properties.idn_name
    spam_filter: MetaOapg.properties.spam_filter
    is_dovecot: MetaOapg.properties.is_dovecot
    usage_space: MetaOapg.properties.usage_space
    forwarding_incoming: MetaOapg.properties.forwarding_incoming
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_reply"]) -> MetaOapg.properties.auto_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spam_filter"]) -> MetaOapg.properties.spam_filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forwarding_incoming"]) -> MetaOapg.properties.forwarding_incoming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forwarding_outgoing"]) -> MetaOapg.properties.forwarding_outgoing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mailbox"]) -> MetaOapg.properties.mailbox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage_space"]) -> MetaOapg.properties.usage_space: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_webmail"]) -> MetaOapg.properties.is_webmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idn_name"]) -> MetaOapg.properties.idn_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_dovecot"]) -> MetaOapg.properties.is_dovecot: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auto_reply", "spam_filter", "forwarding_incoming", "forwarding_outgoing", "comment", "fqdn", "mailbox", "password", "usage_space", "is_webmail", "idn_name", "is_dovecot", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_reply"]) -> MetaOapg.properties.auto_reply: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spam_filter"]) -> MetaOapg.properties.spam_filter: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forwarding_incoming"]) -> MetaOapg.properties.forwarding_incoming: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forwarding_outgoing"]) -> MetaOapg.properties.forwarding_outgoing: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mailbox"]) -> MetaOapg.properties.mailbox: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage_space"]) -> MetaOapg.properties.usage_space: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_webmail"]) -> MetaOapg.properties.is_webmail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idn_name"]) -> MetaOapg.properties.idn_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_dovecot"]) -> MetaOapg.properties.is_dovecot: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auto_reply", "spam_filter", "forwarding_incoming", "forwarding_outgoing", "comment", "fqdn", "mailbox", "password", "usage_space", "is_webmail", "idn_name", "is_dovecot", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        auto_reply: typing.Union[MetaOapg.properties.auto_reply, dict, frozendict.frozendict, ],
        forwarding_outgoing: typing.Union[MetaOapg.properties.forwarding_outgoing, dict, frozendict.frozendict, ],
        mailbox: typing.Union[MetaOapg.properties.mailbox, str, ],
        fqdn: typing.Union[MetaOapg.properties.fqdn, str, ],
        is_webmail: typing.Union[MetaOapg.properties.is_webmail, bool, ],
        comment: typing.Union[MetaOapg.properties.comment, str, ],
        idn_name: typing.Union[MetaOapg.properties.idn_name, str, ],
        spam_filter: typing.Union[MetaOapg.properties.spam_filter, dict, frozendict.frozendict, ],
        is_dovecot: typing.Union[MetaOapg.properties.is_dovecot, bool, ],
        usage_space: typing.Union[MetaOapg.properties.usage_space, decimal.Decimal, int, float, ],
        forwarding_incoming: typing.Union[MetaOapg.properties.forwarding_incoming, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Mailbox':
        return super().__new__(
            cls,
            *_args,
            password=password,
            auto_reply=auto_reply,
            forwarding_outgoing=forwarding_outgoing,
            mailbox=mailbox,
            fqdn=fqdn,
            is_webmail=is_webmail,
            comment=comment,
            idn_name=idn_name,
            spam_filter=spam_filter,
            is_dovecot=is_dovecot,
            usage_space=usage_space,
            forwarding_incoming=forwarding_incoming,
            _configuration=_configuration,
            **kwargs,
        )
