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


class Vds(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Сервер
    """


    class MetaOapg:
        required = {
            "image",
            "disks",
            "os",
            "software",
            "qemu_agent",
            "cpu",
            "created_at",
            "cloud_init",
            "networks",
            "start_at",
            "avatar_id",
            "vnc_pass",
            "preset_id",
            "boot_mode",
            "name",
            "comment",
            "configurator_id",
            "location",
            "cpu_frequency",
            "id",
            "is_ddos_guard",
            "root_pass",
            "ram",
            "status",
        }
        
        class properties:
            id = schemas.NumberSchema
            name = schemas.StrSchema
            comment = schemas.StrSchema
            created_at = schemas.StrSchema
            
            
            class os(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "name",
                        "id",
                        "version",
                    }
                    
                    class properties:
                        id = schemas.NumberSchema
                        
                        
                        class name(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def BITRIX(cls):
                                return cls("bitrix")
                            
                            @schemas.classproperty
                            def BRAINYCP(cls):
                                return cls("brainycp")
                            
                            @schemas.classproperty
                            def CENTOS(cls):
                                return cls("centos")
                            
                            @schemas.classproperty
                            def DEBIAN(cls):
                                return cls("debian")
                            
                            @schemas.classproperty
                            def FEDORA(cls):
                                return cls("fedora")
                            
                            @schemas.classproperty
                            def FREEBSD(cls):
                                return cls("freebsd")
                            
                            @schemas.classproperty
                            def GENTOO(cls):
                                return cls("gentoo")
                            
                            @schemas.classproperty
                            def ROUTEROS(cls):
                                return cls("routeros")
                            
                            @schemas.classproperty
                            def UBUNTU(cls):
                                return cls("ubuntu")
                            
                            @schemas.classproperty
                            def WINDOWS(cls):
                                return cls("windows")
                        
                        
                        class version(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'version':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "id": id,
                            "name": name,
                            "version": version,
                        }
                
                name: MetaOapg.properties.name
                id: MetaOapg.properties.id
                version: MetaOapg.properties.version
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "version", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "version", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, ],
                    id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
                    version: typing.Union[MetaOapg.properties.version, None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'os':
                    return super().__new__(
                        cls,
                        *_args,
                        name=name,
                        id=id,
                        version=version,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class software(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        id = schemas.NumberSchema
                        name = schemas.StrSchema
                        __annotations__ = {
                            "id": id,
                            "name": name,
                        }
            
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'software':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class preset_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'preset_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class location(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            
            
            class configurator_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configurator_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class boot_mode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STD(cls):
                    return cls("std")
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
                
                @schemas.classproperty
                def CD(cls):
                    return cls("cd")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INSTALLING(cls):
                    return cls("installing")
                
                @schemas.classproperty
                def SOFTWARE_INSTALL(cls):
                    return cls("software_install")
                
                @schemas.classproperty
                def REINSTALLING(cls):
                    return cls("reinstalling")
                
                @schemas.classproperty
                def ON(cls):
                    return cls("on")
                
                @schemas.classproperty
                def OFF(cls):
                    return cls("off")
                
                @schemas.classproperty
                def TURNING_ON(cls):
                    return cls("turning_on")
                
                @schemas.classproperty
                def TURNING_OFF(cls):
                    return cls("turning_off")
                
                @schemas.classproperty
                def HARD_TURNING_OFF(cls):
                    return cls("hard_turning_off")
                
                @schemas.classproperty
                def REBOOTING(cls):
                    return cls("rebooting")
                
                @schemas.classproperty
                def HARD_REBOOTING(cls):
                    return cls("hard_rebooting")
                
                @schemas.classproperty
                def REMOVING(cls):
                    return cls("removing")
                
                @schemas.classproperty
                def REMOVED(cls):
                    return cls("removed")
                
                @schemas.classproperty
                def CLONING(cls):
                    return cls("cloning")
                
                @schemas.classproperty
                def TRANSFER(cls):
                    return cls("transfer")
                
                @schemas.classproperty
                def BLOCKED(cls):
                    return cls("blocked")
                
                @schemas.classproperty
                def CONFIGURING(cls):
                    return cls("configuring")
                
                @schemas.classproperty
                def NO_PAID(cls):
                    return cls("no_paid")
                
                @schemas.classproperty
                def PERMANENT_BLOCKED(cls):
                    return cls("permanent_blocked")
            
            
            class start_at(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'start_at':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            is_ddos_guard = schemas.BoolSchema
            cpu = schemas.NumberSchema
            cpu_frequency = schemas.StrSchema
            ram = schemas.NumberSchema
            
            
            class disks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "is_mounted",
                                "is_system",
                                "size",
                                "system_name",
                                "id",
                                "used",
                                "type",
                                "status",
                            }
                            
                            class properties:
                                id = schemas.NumberSchema
                                size = schemas.NumberSchema
                                used = schemas.NumberSchema
                                type = schemas.StrSchema
                                is_mounted = schemas.BoolSchema
                                is_system = schemas.BoolSchema
                                system_name = schemas.StrSchema
                                status = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "size": size,
                                    "used": used,
                                    "type": type,
                                    "is_mounted": is_mounted,
                                    "is_system": is_system,
                                    "system_name": system_name,
                                    "status": status,
                                }
                    
                        
                        is_mounted: MetaOapg.properties.is_mounted
                        is_system: MetaOapg.properties.is_system
                        size: MetaOapg.properties.size
                        system_name: MetaOapg.properties.system_name
                        id: MetaOapg.properties.id
                        used: MetaOapg.properties.used
                        type: MetaOapg.properties.type
                        status: MetaOapg.properties.status
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["used"]) -> MetaOapg.properties.used: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["is_mounted"]) -> MetaOapg.properties.is_mounted: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["is_system"]) -> MetaOapg.properties.is_system: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["system_name"]) -> MetaOapg.properties.system_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "size", "used", "type", "is_mounted", "is_system", "system_name", "status", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["used"]) -> MetaOapg.properties.used: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["is_mounted"]) -> MetaOapg.properties.is_mounted: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["is_system"]) -> MetaOapg.properties.is_system: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["system_name"]) -> MetaOapg.properties.system_name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "size", "used", "type", "is_mounted", "is_system", "system_name", "status", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            is_mounted: typing.Union[MetaOapg.properties.is_mounted, bool, ],
                            is_system: typing.Union[MetaOapg.properties.is_system, bool, ],
                            size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, float, ],
                            system_name: typing.Union[MetaOapg.properties.system_name, str, ],
                            id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
                            used: typing.Union[MetaOapg.properties.used, decimal.Decimal, int, float, ],
                            type: typing.Union[MetaOapg.properties.type, str, ],
                            status: typing.Union[MetaOapg.properties.status, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                is_mounted=is_mounted,
                                is_system=is_system,
                                size=size,
                                system_name=system_name,
                                id=id,
                                used=used,
                                type=type,
                                status=status,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'disks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class avatar_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'avatar_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            vnc_pass = schemas.StrSchema
            
            
            class root_pass(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'root_pass':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class image(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    required = {
                        "name",
                        "is_custom",
                        "id",
                    }
                    
                    class properties:
                        id = schemas.StrSchema
                        name = schemas.StrSchema
                        is_custom = schemas.BoolSchema
                        __annotations__ = {
                            "id": id,
                            "name": name,
                            "is_custom": is_custom,
                        }
            
                
                name: MetaOapg.properties.name
                is_custom: MetaOapg.properties.is_custom
                id: MetaOapg.properties.id
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_custom"]) -> MetaOapg.properties.is_custom: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "is_custom", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_custom"]) -> MetaOapg.properties.is_custom: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "is_custom", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'image':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class networks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "type",
                                "ips",
                            }
                            
                            class properties:
                                
                                
                                class type(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                    
                                    @schemas.classproperty
                                    def PUBLIC(cls):
                                        return cls("public")
                                    
                                    @schemas.classproperty
                                    def LOCAL(cls):
                                        return cls("local")
                                
                                
                                class nat_mode(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                    
                                    @schemas.classproperty
                                    def DNAT_AND_SNAT(cls):
                                        return cls("dnat_and_snat")
                                    
                                    @schemas.classproperty
                                    def SNAT(cls):
                                        return cls("snat")
                                    
                                    @schemas.classproperty
                                    def NO_NAT(cls):
                                        return cls("no_nat")
                                
                                
                                class bandwidth(
                                    schemas.NumberBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneDecimalMixin
                                ):
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[None, decimal.Decimal, int, float, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'bandwidth':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                        )
                                
                                
                                class ips(
                                    schemas.ListBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneTupleMixin
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.AnyTypeSchema,
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                required = {
                                                    "ip",
                                                    "is_main",
                                                    "type",
                                                }
                                                
                                                class properties:
                                                    
                                                    
                                                    class type(
                                                        schemas.EnumBase,
                                                        schemas.StrSchema
                                                    ):
                                                        
                                                        @schemas.classproperty
                                                        def IPV4(cls):
                                                            return cls("ipv4")
                                                        
                                                        @schemas.classproperty
                                                        def IPV6(cls):
                                                            return cls("ipv6")
                                                    ip = schemas.StrSchema
                                                    ptr = schemas.StrSchema
                                                    is_main = schemas.BoolSchema
                                                    __annotations__ = {
                                                        "type": type,
                                                        "ip": ip,
                                                        "ptr": ptr,
                                                        "is_main": is_main,
                                                    }
                                        
                                            
                                            ip: MetaOapg.properties.ip
                                            is_main: MetaOapg.properties.is_main
                                            type: MetaOapg.properties.type
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["ptr"]) -> MetaOapg.properties.ptr: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["is_main"]) -> MetaOapg.properties.is_main: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                            
                                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "ip", "ptr", "is_main", ], str]):
                                                # dict_instance[name] accessor
                                                return super().__getitem__(name)
                                            
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["ptr"]) -> typing.Union[MetaOapg.properties.ptr, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["is_main"]) -> MetaOapg.properties.is_main: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                            
                                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "ip", "ptr", "is_main", ], str]):
                                                return super().get_item_oapg(name)
                                            
                                        
                                            def __new__(
                                                cls,
                                                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                                ip: typing.Union[MetaOapg.properties.ip, str, ],
                                                is_main: typing.Union[MetaOapg.properties.is_main, bool, ],
                                                type: typing.Union[MetaOapg.properties.type, str, ],
                                                ptr: typing.Union[MetaOapg.properties.ptr, str, schemas.Unset] = schemas.unset,
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                            ) -> 'items':
                                                return super().__new__(
                                                    cls,
                                                    *_args,
                                                    ip=ip,
                                                    is_main=is_main,
                                                    type=type,
                                                    ptr=ptr,
                                                    _configuration=_configuration,
                                                    **kwargs,
                                                )
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[list, tuple, None, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'ips':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                        )
                                is_ddos_guard = schemas.BoolSchema
                                __annotations__ = {
                                    "type": type,
                                    "nat_mode": nat_mode,
                                    "bandwidth": bandwidth,
                                    "ips": ips,
                                    "is_ddos_guard": is_ddos_guard,
                                }
                    
                        
                        type: MetaOapg.properties.type
                        ips: MetaOapg.properties.ips
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["nat_mode"]) -> MetaOapg.properties.nat_mode: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["bandwidth"]) -> MetaOapg.properties.bandwidth: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ips"]) -> MetaOapg.properties.ips: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["is_ddos_guard"]) -> MetaOapg.properties.is_ddos_guard: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "nat_mode", "bandwidth", "ips", "is_ddos_guard", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["nat_mode"]) -> typing.Union[MetaOapg.properties.nat_mode, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["bandwidth"]) -> typing.Union[MetaOapg.properties.bandwidth, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ips"]) -> MetaOapg.properties.ips: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["is_ddos_guard"]) -> typing.Union[MetaOapg.properties.is_ddos_guard, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "nat_mode", "bandwidth", "ips", "is_ddos_guard", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            type: typing.Union[MetaOapg.properties.type, str, ],
                            ips: typing.Union[MetaOapg.properties.ips, list, tuple, None, ],
                            nat_mode: typing.Union[MetaOapg.properties.nat_mode, str, schemas.Unset] = schemas.unset,
                            bandwidth: typing.Union[MetaOapg.properties.bandwidth, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            is_ddos_guard: typing.Union[MetaOapg.properties.is_ddos_guard, bool, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                type=type,
                                ips=ips,
                                nat_mode=nat_mode,
                                bandwidth=bandwidth,
                                is_ddos_guard=is_ddos_guard,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'networks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class cloud_init(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cloud_init':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            is_qemu_agent = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "comment": comment,
                "created_at": created_at,
                "os": os,
                "software": software,
                "preset_id": preset_id,
                "location": location,
                "configurator_id": configurator_id,
                "boot_mode": boot_mode,
                "status": status,
                "start_at": start_at,
                "is_ddos_guard": is_ddos_guard,
                "cpu": cpu,
                "cpu_frequency": cpu_frequency,
                "ram": ram,
                "disks": disks,
                "avatar_id": avatar_id,
                "vnc_pass": vnc_pass,
                "root_pass": root_pass,
                "image": image,
                "networks": networks,
                "cloud_init": cloud_init,
                "is_qemu_agent": is_qemu_agent,
            }
    
    image: MetaOapg.properties.image
    disks: MetaOapg.properties.disks
    os: MetaOapg.properties.os
    software: MetaOapg.properties.software
    qemu_agent: schemas.AnyTypeSchema
    cpu: MetaOapg.properties.cpu
    created_at: MetaOapg.properties.created_at
    cloud_init: MetaOapg.properties.cloud_init
    networks: MetaOapg.properties.networks
    start_at: MetaOapg.properties.start_at
    avatar_id: MetaOapg.properties.avatar_id
    vnc_pass: MetaOapg.properties.vnc_pass
    preset_id: MetaOapg.properties.preset_id
    boot_mode: MetaOapg.properties.boot_mode
    name: MetaOapg.properties.name
    comment: MetaOapg.properties.comment
    configurator_id: MetaOapg.properties.configurator_id
    location: MetaOapg.properties.location
    cpu_frequency: MetaOapg.properties.cpu_frequency
    id: MetaOapg.properties.id
    is_ddos_guard: MetaOapg.properties.is_ddos_guard
    root_pass: MetaOapg.properties.root_pass
    ram: MetaOapg.properties.ram
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["software"]) -> MetaOapg.properties.software: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preset_id"]) -> MetaOapg.properties.preset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurator_id"]) -> MetaOapg.properties.configurator_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boot_mode"]) -> MetaOapg.properties.boot_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_at"]) -> MetaOapg.properties.start_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_ddos_guard"]) -> MetaOapg.properties.is_ddos_guard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu"]) -> MetaOapg.properties.cpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_frequency"]) -> MetaOapg.properties.cpu_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ram"]) -> MetaOapg.properties.ram: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disks"]) -> MetaOapg.properties.disks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_id"]) -> MetaOapg.properties.avatar_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vnc_pass"]) -> MetaOapg.properties.vnc_pass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["root_pass"]) -> MetaOapg.properties.root_pass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networks"]) -> MetaOapg.properties.networks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloud_init"]) -> MetaOapg.properties.cloud_init: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_qemu_agent"]) -> MetaOapg.properties.is_qemu_agent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "comment", "created_at", "os", "software", "preset_id", "location", "configurator_id", "boot_mode", "status", "start_at", "is_ddos_guard", "cpu", "cpu_frequency", "ram", "disks", "avatar_id", "vnc_pass", "root_pass", "image", "networks", "cloud_init", "is_qemu_agent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["software"]) -> MetaOapg.properties.software: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preset_id"]) -> MetaOapg.properties.preset_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurator_id"]) -> MetaOapg.properties.configurator_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boot_mode"]) -> MetaOapg.properties.boot_mode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_at"]) -> MetaOapg.properties.start_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_ddos_guard"]) -> MetaOapg.properties.is_ddos_guard: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu"]) -> MetaOapg.properties.cpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_frequency"]) -> MetaOapg.properties.cpu_frequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ram"]) -> MetaOapg.properties.ram: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disks"]) -> MetaOapg.properties.disks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_id"]) -> MetaOapg.properties.avatar_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vnc_pass"]) -> MetaOapg.properties.vnc_pass: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["root_pass"]) -> MetaOapg.properties.root_pass: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networks"]) -> MetaOapg.properties.networks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloud_init"]) -> MetaOapg.properties.cloud_init: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_qemu_agent"]) -> typing.Union[MetaOapg.properties.is_qemu_agent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "comment", "created_at", "os", "software", "preset_id", "location", "configurator_id", "boot_mode", "status", "start_at", "is_ddos_guard", "cpu", "cpu_frequency", "ram", "disks", "avatar_id", "vnc_pass", "root_pass", "image", "networks", "cloud_init", "is_qemu_agent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, dict, frozendict.frozendict, None, ],
        disks: typing.Union[MetaOapg.properties.disks, list, tuple, ],
        os: typing.Union[MetaOapg.properties.os, dict, frozendict.frozendict, ],
        software: typing.Union[MetaOapg.properties.software, dict, frozendict.frozendict, None, ],
        qemu_agent: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        cpu: typing.Union[MetaOapg.properties.cpu, decimal.Decimal, int, float, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        cloud_init: typing.Union[MetaOapg.properties.cloud_init, None, str, ],
        networks: typing.Union[MetaOapg.properties.networks, list, tuple, ],
        start_at: typing.Union[MetaOapg.properties.start_at, None, str, datetime, ],
        avatar_id: typing.Union[MetaOapg.properties.avatar_id, None, str, ],
        vnc_pass: typing.Union[MetaOapg.properties.vnc_pass, str, ],
        preset_id: typing.Union[MetaOapg.properties.preset_id, None, decimal.Decimal, int, float, ],
        boot_mode: typing.Union[MetaOapg.properties.boot_mode, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, ],
        configurator_id: typing.Union[MetaOapg.properties.configurator_id, None, decimal.Decimal, int, float, ],
        location: typing.Union[MetaOapg.properties.location, str, ],
        cpu_frequency: typing.Union[MetaOapg.properties.cpu_frequency, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        is_ddos_guard: typing.Union[MetaOapg.properties.is_ddos_guard, bool, ],
        root_pass: typing.Union[MetaOapg.properties.root_pass, None, str, ],
        ram: typing.Union[MetaOapg.properties.ram, decimal.Decimal, int, float, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        is_qemu_agent: typing.Union[MetaOapg.properties.is_qemu_agent, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Vds':
        return super().__new__(
            cls,
            *_args,
            image=image,
            disks=disks,
            os=os,
            software=software,
            qemu_agent=qemu_agent,
            cpu=cpu,
            created_at=created_at,
            cloud_init=cloud_init,
            networks=networks,
            start_at=start_at,
            avatar_id=avatar_id,
            vnc_pass=vnc_pass,
            preset_id=preset_id,
            boot_mode=boot_mode,
            name=name,
            comment=comment,
            configurator_id=configurator_id,
            location=location,
            cpu_frequency=cpu_frequency,
            id=id,
            is_ddos_guard=is_ddos_guard,
            root_pass=root_pass,
            ram=ram,
            status=status,
            is_qemu_agent=is_qemu_agent,
            _configuration=_configuration,
            **kwargs,
        )
