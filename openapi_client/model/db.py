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


class Db(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    База данных
    """


    class MetaOapg:
        required = {
            "config_parameters",
            "ip",
            "created_at",
            "is_only_local_ip_access",
            "login",
            "type",
            "local_ip",
            "password",
            "account_id",
            "port",
            "preset_id",
            "disk_stats",
            "host",
            "name",
            "id",
            "hash_type",
            "status",
        }
        
        class properties:
            id = schemas.NumberSchema
            created_at = schemas.StrSchema
            account_id = schemas.StrSchema
            login = schemas.StrSchema
            password = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class host(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'host':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "mysql": "MYSQL",
                        "mysql5": "MYSQL5",
                        "postgres": "POSTGRES",
                        "redis": "REDIS",
                        "mongodb": "MONGODB",
                    }
                
                @schemas.classproperty
                def MYSQL(cls):
                    return cls("mysql")
                
                @schemas.classproperty
                def MYSQL5(cls):
                    return cls("mysql5")
                
                @schemas.classproperty
                def POSTGRES(cls):
                    return cls("postgres")
                
                @schemas.classproperty
                def REDIS(cls):
                    return cls("redis")
                
                @schemas.classproperty
                def MONGODB(cls):
                    return cls("mongodb")
            
            
            class hash_type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "caching_sha2": "CACHING_SHA2",
                        "mysql_native": "MYSQL_NATIVE",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def CACHING_SHA2(cls):
                    return cls("caching_sha2")
                
                @schemas.classproperty
                def MYSQL_NATIVE(cls):
                    return cls("mysql_native")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hash_type':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            port = schemas.IntSchema
            
            
            class ip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'ipv4'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ip':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class local_ip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'ipv4'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'local_ip':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "started": "STARTED",
                        "starting": "STARTING",
                        "stoped": "STOPED",
                        "no_paid": "NO_PAID",
                    }
                
                @schemas.classproperty
                def STARTED(cls):
                    return cls("started")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("starting")
                
                @schemas.classproperty
                def STOPED(cls):
                    return cls("stoped")
                
                @schemas.classproperty
                def NO_PAID(cls):
                    return cls("no_paid")
            preset_id = schemas.IntSchema
            
            
            class disk_stats(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    required = {
                        "size",
                        "used",
                    }
                    
                    class properties:
                        size = schemas.NumberSchema
                        used = schemas.NumberSchema
                        __annotations__ = {
                            "size": size,
                            "used": used,
                        }
            
                
                size: MetaOapg.properties.size
                used: MetaOapg.properties.used
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["used"]) -> MetaOapg.properties.used: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["size", "used", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["used"]) -> MetaOapg.properties.used: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["size", "used", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'disk_stats':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def config_parameters() -> typing.Type['ConfigParameters']:
                return ConfigParameters
            is_only_local_ip_access = schemas.BoolSchema
            
            
            class location(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ru-1": "RU1",
                        "ru-2": "RU2",
                        "pl-1": "PL1",
                        "kz-1": "KZ1",
                    }
                
                @schemas.classproperty
                def RU1(cls):
                    return cls("ru-1")
                
                @schemas.classproperty
                def RU2(cls):
                    return cls("ru-2")
                
                @schemas.classproperty
                def PL1(cls):
                    return cls("pl-1")
                
                @schemas.classproperty
                def KZ1(cls):
                    return cls("kz-1")
            __annotations__ = {
                "id": id,
                "created_at": created_at,
                "account_id": account_id,
                "login": login,
                "password": password,
                "name": name,
                "host": host,
                "type": type,
                "hash_type": hash_type,
                "port": port,
                "ip": ip,
                "local_ip": local_ip,
                "status": status,
                "preset_id": preset_id,
                "disk_stats": disk_stats,
                "config_parameters": config_parameters,
                "is_only_local_ip_access": is_only_local_ip_access,
                "location": location,
            }
    
    config_parameters: 'ConfigParameters'
    ip: MetaOapg.properties.ip
    created_at: MetaOapg.properties.created_at
    is_only_local_ip_access: MetaOapg.properties.is_only_local_ip_access
    login: MetaOapg.properties.login
    type: MetaOapg.properties.type
    local_ip: MetaOapg.properties.local_ip
    password: MetaOapg.properties.password
    account_id: MetaOapg.properties.account_id
    port: MetaOapg.properties.port
    preset_id: MetaOapg.properties.preset_id
    disk_stats: MetaOapg.properties.disk_stats
    host: MetaOapg.properties.host
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    hash_type: MetaOapg.properties.hash_type
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash_type"]) -> MetaOapg.properties.hash_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["local_ip"]) -> MetaOapg.properties.local_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preset_id"]) -> MetaOapg.properties.preset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_stats"]) -> MetaOapg.properties.disk_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_parameters"]) -> 'ConfigParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_only_local_ip_access"]) -> MetaOapg.properties.is_only_local_ip_access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "created_at", "account_id", "login", "password", "name", "host", "type", "hash_type", "port", "ip", "local_ip", "status", "preset_id", "disk_stats", "config_parameters", "is_only_local_ip_access", "location", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash_type"]) -> MetaOapg.properties.hash_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["local_ip"]) -> MetaOapg.properties.local_ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preset_id"]) -> MetaOapg.properties.preset_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_stats"]) -> MetaOapg.properties.disk_stats: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_parameters"]) -> 'ConfigParameters': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_only_local_ip_access"]) -> MetaOapg.properties.is_only_local_ip_access: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "created_at", "account_id", "login", "password", "name", "host", "type", "hash_type", "port", "ip", "local_ip", "status", "preset_id", "disk_stats", "config_parameters", "is_only_local_ip_access", "location", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        config_parameters: 'ConfigParameters',
        ip: typing.Union[MetaOapg.properties.ip, None, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        is_only_local_ip_access: typing.Union[MetaOapg.properties.is_only_local_ip_access, bool, ],
        login: typing.Union[MetaOapg.properties.login, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        local_ip: typing.Union[MetaOapg.properties.local_ip, None, str, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, ],
        preset_id: typing.Union[MetaOapg.properties.preset_id, decimal.Decimal, int, ],
        disk_stats: typing.Union[MetaOapg.properties.disk_stats, dict, frozendict.frozendict, None, ],
        host: typing.Union[MetaOapg.properties.host, None, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        hash_type: typing.Union[MetaOapg.properties.hash_type, None, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Db':
        return super().__new__(
            cls,
            *_args,
            config_parameters=config_parameters,
            ip=ip,
            created_at=created_at,
            is_only_local_ip_access=is_only_local_ip_access,
            login=login,
            type=type,
            local_ip=local_ip,
            password=password,
            account_id=account_id,
            port=port,
            preset_id=preset_id,
            disk_stats=disk_stats,
            host=host,
            name=name,
            id=id,
            hash_type=hash_type,
            status=status,
            location=location,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.config_parameters import ConfigParameters
