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


class Domain(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Домен
    """


    class MetaOapg:
        required = {
            "request_status",
            "days_left",
            "fqdn",
            "is_whois_privacy_enabled",
            "paid_till",
            "allowed_buy_periods",
            "linked_ip",
            "subdomains",
            "is_autoprolong_enabled",
            "is_premium",
            "domain_status",
            "is_prolong_allowed",
            "provider",
            "premium_prolong_cost",
            "expiration",
            "id",
            "is_technical",
            "tld_id",
            "person_id",
        }
        
        class properties:
            
            
            class allowed_buy_periods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "period",
                                "price",
                            }
                            
                            class properties:
                            
                                @staticmethod
                                def period() -> typing.Type['DomainPaymentPeriod']:
                                    return DomainPaymentPeriod
                                price = schemas.NumberSchema
                                __annotations__ = {
                                    "period": period,
                                    "price": price,
                                }
                        
                        period: 'DomainPaymentPeriod'
                        price: MetaOapg.properties.price
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["period"]) -> 'DomainPaymentPeriod': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["period", "price", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["period"]) -> 'DomainPaymentPeriod': ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["period", "price", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            period: 'DomainPaymentPeriod',
                            price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                period=period,
                                price=price,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'allowed_buy_periods':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            days_left = schemas.NumberSchema
            
            
            class domain_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "awaiting_payment": "AWAITING_PAYMENT",
                        "expired": "EXPIRED",
                        "final_expired": "FINAL_EXPIRED",
                        "free": "FREE",
                        "no_paid": "NO_PAID",
                        "ns_based": "NS_BASED",
                        "paid": "PAID",
                        "soon_expire": "SOON_EXPIRE",
                        "today_expired": "TODAY_EXPIRED",
                    }
                
                @schemas.classproperty
                def AWAITING_PAYMENT(cls):
                    return cls("awaiting_payment")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("expired")
                
                @schemas.classproperty
                def FINAL_EXPIRED(cls):
                    return cls("final_expired")
                
                @schemas.classproperty
                def FREE(cls):
                    return cls("free")
                
                @schemas.classproperty
                def NO_PAID(cls):
                    return cls("no_paid")
                
                @schemas.classproperty
                def NS_BASED(cls):
                    return cls("ns_based")
                
                @schemas.classproperty
                def PAID(cls):
                    return cls("paid")
                
                @schemas.classproperty
                def SOON_EXPIRE(cls):
                    return cls("soon_expire")
                
                @schemas.classproperty
                def TODAY_EXPIRED(cls):
                    return cls("today_expired")
            expiration = schemas.StrSchema
            fqdn = schemas.StrSchema
            id = schemas.NumberSchema
            
            
            class is_autoprolong_enabled(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_autoprolong_enabled':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            is_premium = schemas.BoolSchema
            is_prolong_allowed = schemas.BoolSchema
            is_technical = schemas.BoolSchema
            
            
            class is_whois_privacy_enabled(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_whois_privacy_enabled':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class linked_ip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'linked_ip':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class paid_till(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paid_till':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class person_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'person_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class premium_prolong_cost(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'premium_prolong_cost':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class provider(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'provider':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class request_status(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "prolongation_fail": "PROLONGATION_FAIL",
                        "prolongation_request": "PROLONGATION_REQUEST",
                        "registration_fail": "REGISTRATION_FAIL",
                        "registration_request": "REGISTRATION_REQUEST",
                        "transfer_fail": "TRANSFER_FAIL",
                        "transfer_request": "TRANSFER_REQUEST",
                        "awaiting_person": "AWAITING_PERSON",
                    }
                
                @schemas.classproperty
                def PROLONGATION_FAIL(cls):
                    return cls("prolongation_fail")
                
                @schemas.classproperty
                def PROLONGATION_REQUEST(cls):
                    return cls("prolongation_request")
                
                @schemas.classproperty
                def REGISTRATION_FAIL(cls):
                    return cls("registration_fail")
                
                @schemas.classproperty
                def REGISTRATION_REQUEST(cls):
                    return cls("registration_request")
                
                @schemas.classproperty
                def TRANSFER_FAIL(cls):
                    return cls("transfer_fail")
                
                @schemas.classproperty
                def TRANSFER_REQUEST(cls):
                    return cls("transfer_request")
                
                @schemas.classproperty
                def AWAITING_PERSON(cls):
                    return cls("awaiting_person")
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'request_status':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class subdomains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Subdomain']:
                        return Subdomain
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Subdomain'], typing.List['Subdomain']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subdomains':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Subdomain':
                    return super().__getitem__(i)
            
            
            class tld_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tld_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "allowed_buy_periods": allowed_buy_periods,
                "days_left": days_left,
                "domain_status": domain_status,
                "expiration": expiration,
                "fqdn": fqdn,
                "id": id,
                "is_autoprolong_enabled": is_autoprolong_enabled,
                "is_premium": is_premium,
                "is_prolong_allowed": is_prolong_allowed,
                "is_technical": is_technical,
                "is_whois_privacy_enabled": is_whois_privacy_enabled,
                "linked_ip": linked_ip,
                "paid_till": paid_till,
                "person_id": person_id,
                "premium_prolong_cost": premium_prolong_cost,
                "provider": provider,
                "request_status": request_status,
                "subdomains": subdomains,
                "tld_id": tld_id,
            }
    
    request_status: MetaOapg.properties.request_status
    days_left: MetaOapg.properties.days_left
    fqdn: MetaOapg.properties.fqdn
    is_whois_privacy_enabled: MetaOapg.properties.is_whois_privacy_enabled
    paid_till: MetaOapg.properties.paid_till
    allowed_buy_periods: MetaOapg.properties.allowed_buy_periods
    linked_ip: MetaOapg.properties.linked_ip
    subdomains: MetaOapg.properties.subdomains
    is_autoprolong_enabled: MetaOapg.properties.is_autoprolong_enabled
    is_premium: MetaOapg.properties.is_premium
    domain_status: MetaOapg.properties.domain_status
    is_prolong_allowed: MetaOapg.properties.is_prolong_allowed
    provider: MetaOapg.properties.provider
    premium_prolong_cost: MetaOapg.properties.premium_prolong_cost
    expiration: MetaOapg.properties.expiration
    id: MetaOapg.properties.id
    is_technical: MetaOapg.properties.is_technical
    tld_id: MetaOapg.properties.tld_id
    person_id: MetaOapg.properties.person_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowed_buy_periods"]) -> MetaOapg.properties.allowed_buy_periods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days_left"]) -> MetaOapg.properties.days_left: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain_status"]) -> MetaOapg.properties.domain_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_autoprolong_enabled"]) -> MetaOapg.properties.is_autoprolong_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_premium"]) -> MetaOapg.properties.is_premium: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_prolong_allowed"]) -> MetaOapg.properties.is_prolong_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_technical"]) -> MetaOapg.properties.is_technical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_whois_privacy_enabled"]) -> MetaOapg.properties.is_whois_privacy_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_ip"]) -> MetaOapg.properties.linked_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid_till"]) -> MetaOapg.properties.paid_till: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["person_id"]) -> MetaOapg.properties.person_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premium_prolong_cost"]) -> MetaOapg.properties.premium_prolong_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_status"]) -> MetaOapg.properties.request_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subdomains"]) -> MetaOapg.properties.subdomains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tld_id"]) -> MetaOapg.properties.tld_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowed_buy_periods", "days_left", "domain_status", "expiration", "fqdn", "id", "is_autoprolong_enabled", "is_premium", "is_prolong_allowed", "is_technical", "is_whois_privacy_enabled", "linked_ip", "paid_till", "person_id", "premium_prolong_cost", "provider", "request_status", "subdomains", "tld_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowed_buy_periods"]) -> MetaOapg.properties.allowed_buy_periods: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days_left"]) -> MetaOapg.properties.days_left: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain_status"]) -> MetaOapg.properties.domain_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_autoprolong_enabled"]) -> MetaOapg.properties.is_autoprolong_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_premium"]) -> MetaOapg.properties.is_premium: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_prolong_allowed"]) -> MetaOapg.properties.is_prolong_allowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_technical"]) -> MetaOapg.properties.is_technical: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_whois_privacy_enabled"]) -> MetaOapg.properties.is_whois_privacy_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_ip"]) -> MetaOapg.properties.linked_ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid_till"]) -> MetaOapg.properties.paid_till: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["person_id"]) -> MetaOapg.properties.person_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premium_prolong_cost"]) -> MetaOapg.properties.premium_prolong_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_status"]) -> MetaOapg.properties.request_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subdomains"]) -> MetaOapg.properties.subdomains: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tld_id"]) -> MetaOapg.properties.tld_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowed_buy_periods", "days_left", "domain_status", "expiration", "fqdn", "id", "is_autoprolong_enabled", "is_premium", "is_prolong_allowed", "is_technical", "is_whois_privacy_enabled", "linked_ip", "paid_till", "person_id", "premium_prolong_cost", "provider", "request_status", "subdomains", "tld_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        request_status: typing.Union[MetaOapg.properties.request_status, None, str, ],
        days_left: typing.Union[MetaOapg.properties.days_left, decimal.Decimal, int, float, ],
        fqdn: typing.Union[MetaOapg.properties.fqdn, str, ],
        is_whois_privacy_enabled: typing.Union[MetaOapg.properties.is_whois_privacy_enabled, None, bool, ],
        paid_till: typing.Union[MetaOapg.properties.paid_till, None, str, ],
        allowed_buy_periods: typing.Union[MetaOapg.properties.allowed_buy_periods, list, tuple, ],
        linked_ip: typing.Union[MetaOapg.properties.linked_ip, None, str, ],
        subdomains: typing.Union[MetaOapg.properties.subdomains, list, tuple, ],
        is_autoprolong_enabled: typing.Union[MetaOapg.properties.is_autoprolong_enabled, None, bool, ],
        is_premium: typing.Union[MetaOapg.properties.is_premium, bool, ],
        domain_status: typing.Union[MetaOapg.properties.domain_status, str, ],
        is_prolong_allowed: typing.Union[MetaOapg.properties.is_prolong_allowed, bool, ],
        provider: typing.Union[MetaOapg.properties.provider, None, str, ],
        premium_prolong_cost: typing.Union[MetaOapg.properties.premium_prolong_cost, None, decimal.Decimal, int, float, ],
        expiration: typing.Union[MetaOapg.properties.expiration, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        is_technical: typing.Union[MetaOapg.properties.is_technical, bool, ],
        tld_id: typing.Union[MetaOapg.properties.tld_id, None, decimal.Decimal, int, float, ],
        person_id: typing.Union[MetaOapg.properties.person_id, None, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Domain':
        return super().__new__(
            cls,
            *_args,
            request_status=request_status,
            days_left=days_left,
            fqdn=fqdn,
            is_whois_privacy_enabled=is_whois_privacy_enabled,
            paid_till=paid_till,
            allowed_buy_periods=allowed_buy_periods,
            linked_ip=linked_ip,
            subdomains=subdomains,
            is_autoprolong_enabled=is_autoprolong_enabled,
            is_premium=is_premium,
            domain_status=domain_status,
            is_prolong_allowed=is_prolong_allowed,
            provider=provider,
            premium_prolong_cost=premium_prolong_cost,
            expiration=expiration,
            id=id,
            is_technical=is_technical,
            tld_id=tld_id,
            person_id=person_id,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.domain_payment_period import DomainPaymentPeriod
from openapi_client.model.subdomain import Subdomain
