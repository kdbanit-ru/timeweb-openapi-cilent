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


class DomainRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Заявка на продление/регистрацию/трансфер домена.
    """


    class MetaOapg:
        required = {
            "date",
            "prime",
            "period",
            "fqdn",
            "message",
            "type",
            "is_antispam_enabled",
            "is_whois_privacy_enabled",
            "auth_code",
            "error_code_transfer",
            "is_autoprolong_enabled",
            "account_id",
            "money_source",
            "group_id",
            "domain_bundle_id",
            "soon_expire",
            "id",
            "sort_order",
            "person_id",
        }
        
        class properties:
            account_id = schemas.StrSchema
            
            
            class auth_code(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'auth_code':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            date = schemas.DateTimeSchema
            
            
            class domain_bundle_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'domain_bundle_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class error_code_transfer(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error_code_transfer':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            fqdn = schemas.StrSchema
            group_id = schemas.NumberSchema
            id = schemas.NumberSchema
            is_antispam_enabled = schemas.BoolSchema
            is_autoprolong_enabled = schemas.BoolSchema
            is_whois_privacy_enabled = schemas.BoolSchema
            
            
            class message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'message':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class money_source(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "use": "USE",
                        "bonus": "BONUS",
                        "invoice": "INVOICE",
                    }
                
                @schemas.classproperty
                def USE(cls):
                    return cls("use")
                
                @schemas.classproperty
                def BONUS(cls):
                    return cls("bonus")
                
                @schemas.classproperty
                def INVOICE(cls):
                    return cls("invoice")
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'money_source':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def period() -> typing.Type['DomainPaymentPeriod']:
                return DomainPaymentPeriod
            person_id = schemas.NumberSchema
            
            
            class prime(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            DomainPrimeType,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'prime':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            soon_expire = schemas.NumberSchema
            sort_order = schemas.NumberSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "request": "REQUEST",
                        "prolong": "PROLONG",
                        "transfer": "TRANSFER",
                    }
                
                @schemas.classproperty
                def REQUEST(cls):
                    return cls("request")
                
                @schemas.classproperty
                def PROLONG(cls):
                    return cls("prolong")
                
                @schemas.classproperty
                def TRANSFER(cls):
                    return cls("transfer")
            __annotations__ = {
                "account_id": account_id,
                "auth_code": auth_code,
                "date": date,
                "domain_bundle_id": domain_bundle_id,
                "error_code_transfer": error_code_transfer,
                "fqdn": fqdn,
                "group_id": group_id,
                "id": id,
                "is_antispam_enabled": is_antispam_enabled,
                "is_autoprolong_enabled": is_autoprolong_enabled,
                "is_whois_privacy_enabled": is_whois_privacy_enabled,
                "message": message,
                "money_source": money_source,
                "period": period,
                "person_id": person_id,
                "prime": prime,
                "soon_expire": soon_expire,
                "sort_order": sort_order,
                "type": type,
            }
    
    date: MetaOapg.properties.date
    prime: MetaOapg.properties.prime
    period: 'DomainPaymentPeriod'
    fqdn: MetaOapg.properties.fqdn
    message: MetaOapg.properties.message
    type: MetaOapg.properties.type
    is_antispam_enabled: MetaOapg.properties.is_antispam_enabled
    is_whois_privacy_enabled: MetaOapg.properties.is_whois_privacy_enabled
    auth_code: MetaOapg.properties.auth_code
    error_code_transfer: MetaOapg.properties.error_code_transfer
    is_autoprolong_enabled: MetaOapg.properties.is_autoprolong_enabled
    account_id: MetaOapg.properties.account_id
    money_source: MetaOapg.properties.money_source
    group_id: MetaOapg.properties.group_id
    domain_bundle_id: MetaOapg.properties.domain_bundle_id
    soon_expire: MetaOapg.properties.soon_expire
    id: MetaOapg.properties.id
    sort_order: MetaOapg.properties.sort_order
    person_id: MetaOapg.properties.person_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_code"]) -> MetaOapg.properties.auth_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain_bundle_id"]) -> MetaOapg.properties.domain_bundle_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code_transfer"]) -> MetaOapg.properties.error_code_transfer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_antispam_enabled"]) -> MetaOapg.properties.is_antispam_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_autoprolong_enabled"]) -> MetaOapg.properties.is_autoprolong_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_whois_privacy_enabled"]) -> MetaOapg.properties.is_whois_privacy_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["money_source"]) -> MetaOapg.properties.money_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period"]) -> 'DomainPaymentPeriod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["person_id"]) -> MetaOapg.properties.person_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prime"]) -> MetaOapg.properties.prime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soon_expire"]) -> MetaOapg.properties.soon_expire: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_id", "auth_code", "date", "domain_bundle_id", "error_code_transfer", "fqdn", "group_id", "id", "is_antispam_enabled", "is_autoprolong_enabled", "is_whois_privacy_enabled", "message", "money_source", "period", "person_id", "prime", "soon_expire", "sort_order", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_code"]) -> MetaOapg.properties.auth_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain_bundle_id"]) -> MetaOapg.properties.domain_bundle_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code_transfer"]) -> MetaOapg.properties.error_code_transfer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_antispam_enabled"]) -> MetaOapg.properties.is_antispam_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_autoprolong_enabled"]) -> MetaOapg.properties.is_autoprolong_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_whois_privacy_enabled"]) -> MetaOapg.properties.is_whois_privacy_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["money_source"]) -> MetaOapg.properties.money_source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period"]) -> 'DomainPaymentPeriod': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["person_id"]) -> MetaOapg.properties.person_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prime"]) -> MetaOapg.properties.prime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soon_expire"]) -> MetaOapg.properties.soon_expire: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_id", "auth_code", "date", "domain_bundle_id", "error_code_transfer", "fqdn", "group_id", "id", "is_antispam_enabled", "is_autoprolong_enabled", "is_whois_privacy_enabled", "message", "money_source", "period", "person_id", "prime", "soon_expire", "sort_order", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, datetime, ],
        prime: typing.Union[MetaOapg.properties.prime, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        period: 'DomainPaymentPeriod',
        fqdn: typing.Union[MetaOapg.properties.fqdn, str, ],
        message: typing.Union[MetaOapg.properties.message, None, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        is_antispam_enabled: typing.Union[MetaOapg.properties.is_antispam_enabled, bool, ],
        is_whois_privacy_enabled: typing.Union[MetaOapg.properties.is_whois_privacy_enabled, bool, ],
        auth_code: typing.Union[MetaOapg.properties.auth_code, None, str, ],
        error_code_transfer: typing.Union[MetaOapg.properties.error_code_transfer, None, str, ],
        is_autoprolong_enabled: typing.Union[MetaOapg.properties.is_autoprolong_enabled, bool, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        money_source: typing.Union[MetaOapg.properties.money_source, None, str, ],
        group_id: typing.Union[MetaOapg.properties.group_id, decimal.Decimal, int, float, ],
        domain_bundle_id: typing.Union[MetaOapg.properties.domain_bundle_id, None, str, ],
        soon_expire: typing.Union[MetaOapg.properties.soon_expire, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        sort_order: typing.Union[MetaOapg.properties.sort_order, decimal.Decimal, int, float, ],
        person_id: typing.Union[MetaOapg.properties.person_id, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DomainRequest':
        return super().__new__(
            cls,
            *_args,
            date=date,
            prime=prime,
            period=period,
            fqdn=fqdn,
            message=message,
            type=type,
            is_antispam_enabled=is_antispam_enabled,
            is_whois_privacy_enabled=is_whois_privacy_enabled,
            auth_code=auth_code,
            error_code_transfer=error_code_transfer,
            is_autoprolong_enabled=is_autoprolong_enabled,
            account_id=account_id,
            money_source=money_source,
            group_id=group_id,
            domain_bundle_id=domain_bundle_id,
            soon_expire=soon_expire,
            id=id,
            sort_order=sort_order,
            person_id=person_id,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.domain_payment_period import DomainPaymentPeriod
from openapi_client.model.domain_prime_type import DomainPrimeType
