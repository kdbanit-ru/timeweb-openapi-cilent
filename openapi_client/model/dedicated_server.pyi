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


class DedicatedServer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Выделенный сервер
    """


    class MetaOapg:
        required = {
            "cpu_description",
            "autoinstall_ready",
            "ip",
            "os_id",
            "created_at",
            "cp_id",
            "bandwidth_id",
            "ipmi_login",
            "additional_ip_addr_id",
            "ram_description",
            "vnc_pass",
            "hdd_description",
            "ipmi_password",
            "network_drive_id",
            "ipv6",
            "price",
            "name",
            "comment",
            "location",
            "id",
            "ipmi_ip",
            "plan_id",
            "node_id",
            "status",
        }
        
        class properties:
            id = schemas.NumberSchema
            cpu_description = schemas.StrSchema
            hdd_description = schemas.StrSchema
            ram_description = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            
            
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
            
            
            class ipmi_ip(
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
                ) -> 'ipmi_ip':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ipmi_login(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ipmi_login':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ipmi_password(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ipmi_password':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ipv6(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'ipv6'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ipv6':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class node_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'node_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            comment = schemas.StrSchema
            
            
            class vnc_pass(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vnc_pass':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INSTALLING(cls):
                    return cls("installing")
                
                @schemas.classproperty
                def INSTALLED(cls):
                    return cls("installed")
                
                @schemas.classproperty
                def ON(cls):
                    return cls("on")
                
                @schemas.classproperty
                def OFF(cls):
                    return cls("off")
            
            
            class os_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'os_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class cp_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cp_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class bandwidth_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bandwidth_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class network_drive_id(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'network_drive_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class additional_ip_addr_id(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additional_ip_addr_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class plan_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'plan_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            price = schemas.NumberSchema
            
            
            class location(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RU1(cls):
                    return cls("ru-1")
                
                @schemas.classproperty
                def PL1(cls):
                    return cls("pl-1")
                
                @schemas.classproperty
                def KZ1(cls):
                    return cls("kz-1")
            autoinstall_ready = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "cpu_description": cpu_description,
                "hdd_description": hdd_description,
                "ram_description": ram_description,
                "created_at": created_at,
                "ip": ip,
                "ipmi_ip": ipmi_ip,
                "ipmi_login": ipmi_login,
                "ipmi_password": ipmi_password,
                "ipv6": ipv6,
                "node_id": node_id,
                "name": name,
                "comment": comment,
                "vnc_pass": vnc_pass,
                "status": status,
                "os_id": os_id,
                "cp_id": cp_id,
                "bandwidth_id": bandwidth_id,
                "network_drive_id": network_drive_id,
                "additional_ip_addr_id": additional_ip_addr_id,
                "plan_id": plan_id,
                "price": price,
                "location": location,
                "autoinstall_ready": autoinstall_ready,
            }
    
    cpu_description: MetaOapg.properties.cpu_description
    autoinstall_ready: MetaOapg.properties.autoinstall_ready
    ip: MetaOapg.properties.ip
    os_id: MetaOapg.properties.os_id
    created_at: MetaOapg.properties.created_at
    cp_id: MetaOapg.properties.cp_id
    bandwidth_id: MetaOapg.properties.bandwidth_id
    ipmi_login: MetaOapg.properties.ipmi_login
    additional_ip_addr_id: MetaOapg.properties.additional_ip_addr_id
    ram_description: MetaOapg.properties.ram_description
    vnc_pass: MetaOapg.properties.vnc_pass
    hdd_description: MetaOapg.properties.hdd_description
    ipmi_password: MetaOapg.properties.ipmi_password
    network_drive_id: MetaOapg.properties.network_drive_id
    ipv6: MetaOapg.properties.ipv6
    price: MetaOapg.properties.price
    name: MetaOapg.properties.name
    comment: MetaOapg.properties.comment
    location: MetaOapg.properties.location
    id: MetaOapg.properties.id
    ipmi_ip: MetaOapg.properties.ipmi_ip
    plan_id: MetaOapg.properties.plan_id
    node_id: MetaOapg.properties.node_id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_description"]) -> MetaOapg.properties.cpu_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hdd_description"]) -> MetaOapg.properties.hdd_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ram_description"]) -> MetaOapg.properties.ram_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipmi_ip"]) -> MetaOapg.properties.ipmi_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipmi_login"]) -> MetaOapg.properties.ipmi_login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipmi_password"]) -> MetaOapg.properties.ipmi_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv6"]) -> MetaOapg.properties.ipv6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vnc_pass"]) -> MetaOapg.properties.vnc_pass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_id"]) -> MetaOapg.properties.os_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cp_id"]) -> MetaOapg.properties.cp_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bandwidth_id"]) -> MetaOapg.properties.bandwidth_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_drive_id"]) -> MetaOapg.properties.network_drive_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_ip_addr_id"]) -> MetaOapg.properties.additional_ip_addr_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan_id"]) -> MetaOapg.properties.plan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoinstall_ready"]) -> MetaOapg.properties.autoinstall_ready: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "cpu_description", "hdd_description", "ram_description", "created_at", "ip", "ipmi_ip", "ipmi_login", "ipmi_password", "ipv6", "node_id", "name", "comment", "vnc_pass", "status", "os_id", "cp_id", "bandwidth_id", "network_drive_id", "additional_ip_addr_id", "plan_id", "price", "location", "autoinstall_ready", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_description"]) -> MetaOapg.properties.cpu_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hdd_description"]) -> MetaOapg.properties.hdd_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ram_description"]) -> MetaOapg.properties.ram_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipmi_ip"]) -> MetaOapg.properties.ipmi_ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipmi_login"]) -> MetaOapg.properties.ipmi_login: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipmi_password"]) -> MetaOapg.properties.ipmi_password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv6"]) -> MetaOapg.properties.ipv6: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vnc_pass"]) -> MetaOapg.properties.vnc_pass: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_id"]) -> MetaOapg.properties.os_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cp_id"]) -> MetaOapg.properties.cp_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bandwidth_id"]) -> MetaOapg.properties.bandwidth_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_drive_id"]) -> MetaOapg.properties.network_drive_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_ip_addr_id"]) -> MetaOapg.properties.additional_ip_addr_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan_id"]) -> MetaOapg.properties.plan_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoinstall_ready"]) -> MetaOapg.properties.autoinstall_ready: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "cpu_description", "hdd_description", "ram_description", "created_at", "ip", "ipmi_ip", "ipmi_login", "ipmi_password", "ipv6", "node_id", "name", "comment", "vnc_pass", "status", "os_id", "cp_id", "bandwidth_id", "network_drive_id", "additional_ip_addr_id", "plan_id", "price", "location", "autoinstall_ready", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cpu_description: typing.Union[MetaOapg.properties.cpu_description, str, ],
        autoinstall_ready: typing.Union[MetaOapg.properties.autoinstall_ready, decimal.Decimal, int, float, ],
        ip: typing.Union[MetaOapg.properties.ip, None, str, ],
        os_id: typing.Union[MetaOapg.properties.os_id, None, decimal.Decimal, int, float, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        cp_id: typing.Union[MetaOapg.properties.cp_id, None, decimal.Decimal, int, float, ],
        bandwidth_id: typing.Union[MetaOapg.properties.bandwidth_id, None, decimal.Decimal, int, float, ],
        ipmi_login: typing.Union[MetaOapg.properties.ipmi_login, None, str, ],
        additional_ip_addr_id: typing.Union[MetaOapg.properties.additional_ip_addr_id, list, tuple, None, ],
        ram_description: typing.Union[MetaOapg.properties.ram_description, str, ],
        vnc_pass: typing.Union[MetaOapg.properties.vnc_pass, None, str, ],
        hdd_description: typing.Union[MetaOapg.properties.hdd_description, str, ],
        ipmi_password: typing.Union[MetaOapg.properties.ipmi_password, None, str, ],
        network_drive_id: typing.Union[MetaOapg.properties.network_drive_id, list, tuple, None, ],
        ipv6: typing.Union[MetaOapg.properties.ipv6, None, str, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, ],
        location: typing.Union[MetaOapg.properties.location, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        ipmi_ip: typing.Union[MetaOapg.properties.ipmi_ip, None, str, ],
        plan_id: typing.Union[MetaOapg.properties.plan_id, None, decimal.Decimal, int, float, ],
        node_id: typing.Union[MetaOapg.properties.node_id, None, decimal.Decimal, int, float, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DedicatedServer':
        return super().__new__(
            cls,
            *_args,
            cpu_description=cpu_description,
            autoinstall_ready=autoinstall_ready,
            ip=ip,
            os_id=os_id,
            created_at=created_at,
            cp_id=cp_id,
            bandwidth_id=bandwidth_id,
            ipmi_login=ipmi_login,
            additional_ip_addr_id=additional_ip_addr_id,
            ram_description=ram_description,
            vnc_pass=vnc_pass,
            hdd_description=hdd_description,
            ipmi_password=ipmi_password,
            network_drive_id=network_drive_id,
            ipv6=ipv6,
            price=price,
            name=name,
            comment=comment,
            location=location,
            id=id,
            ipmi_ip=ipmi_ip,
            plan_id=plan_id,
            node_id=node_id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
