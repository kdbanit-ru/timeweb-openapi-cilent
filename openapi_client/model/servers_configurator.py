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


class ServersConfigurator(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "requirements",
            "disk_type",
            "location",
            "cpu_frequency",
            "id",
            "is_allowed_local_network",
        }
        
        class properties:
            id = schemas.NumberSchema
            
            
            class location(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ru-1": "RU1",
                        "pl-1": "PL1",
                        "kz-1": "KZ1",
                    }
                
                @schemas.classproperty
                def RU1(cls):
                    return cls("ru-1")
                
                @schemas.classproperty
                def PL1(cls):
                    return cls("pl-1")
                
                @schemas.classproperty
                def KZ1(cls):
                    return cls("kz-1")
            
            
            class disk_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ssd": "SSD",
                        "nvme": "NVME",
                        "hdd": "HDD",
                    }
                
                @schemas.classproperty
                def SSD(cls):
                    return cls("ssd")
                
                @schemas.classproperty
                def NVME(cls):
                    return cls("nvme")
                
                @schemas.classproperty
                def HDD(cls):
                    return cls("hdd")
            is_allowed_local_network = schemas.BoolSchema
            cpu_frequency = schemas.StrSchema
            
            
            class requirements(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    required = {
                        "disk_min",
                        "disk_max",
                        "network_bandwidth_max",
                        "disk_step",
                        "network_bandwidth_step",
                        "cpu_step",
                        "network_bandwidth_min",
                        "cpu_max",
                        "ram_min",
                        "ram_max",
                        "cpu_min",
                        "ram_step",
                    }
                    
                    class properties:
                        cpu_min = schemas.NumberSchema
                        cpu_step = schemas.NumberSchema
                        cpu_max = schemas.NumberSchema
                        ram_min = schemas.NumberSchema
                        ram_step = schemas.NumberSchema
                        ram_max = schemas.NumberSchema
                        disk_min = schemas.NumberSchema
                        disk_step = schemas.NumberSchema
                        disk_max = schemas.NumberSchema
                        network_bandwidth_min = schemas.NumberSchema
                        network_bandwidth_step = schemas.NumberSchema
                        network_bandwidth_max = schemas.NumberSchema
                        __annotations__ = {
                            "cpu_min": cpu_min,
                            "cpu_step": cpu_step,
                            "cpu_max": cpu_max,
                            "ram_min": ram_min,
                            "ram_step": ram_step,
                            "ram_max": ram_max,
                            "disk_min": disk_min,
                            "disk_step": disk_step,
                            "disk_max": disk_max,
                            "network_bandwidth_min": network_bandwidth_min,
                            "network_bandwidth_step": network_bandwidth_step,
                            "network_bandwidth_max": network_bandwidth_max,
                        }
            
                
                disk_min: MetaOapg.properties.disk_min
                disk_max: MetaOapg.properties.disk_max
                network_bandwidth_max: MetaOapg.properties.network_bandwidth_max
                disk_step: MetaOapg.properties.disk_step
                network_bandwidth_step: MetaOapg.properties.network_bandwidth_step
                cpu_step: MetaOapg.properties.cpu_step
                network_bandwidth_min: MetaOapg.properties.network_bandwidth_min
                cpu_max: MetaOapg.properties.cpu_max
                ram_min: MetaOapg.properties.ram_min
                ram_max: MetaOapg.properties.ram_max
                cpu_min: MetaOapg.properties.cpu_min
                ram_step: MetaOapg.properties.ram_step
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cpu_min"]) -> MetaOapg.properties.cpu_min: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cpu_step"]) -> MetaOapg.properties.cpu_step: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cpu_max"]) -> MetaOapg.properties.cpu_max: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ram_min"]) -> MetaOapg.properties.ram_min: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ram_step"]) -> MetaOapg.properties.ram_step: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ram_max"]) -> MetaOapg.properties.ram_max: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["disk_min"]) -> MetaOapg.properties.disk_min: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["disk_step"]) -> MetaOapg.properties.disk_step: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["disk_max"]) -> MetaOapg.properties.disk_max: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["network_bandwidth_min"]) -> MetaOapg.properties.network_bandwidth_min: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["network_bandwidth_step"]) -> MetaOapg.properties.network_bandwidth_step: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["network_bandwidth_max"]) -> MetaOapg.properties.network_bandwidth_max: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["cpu_min", "cpu_step", "cpu_max", "ram_min", "ram_step", "ram_max", "disk_min", "disk_step", "disk_max", "network_bandwidth_min", "network_bandwidth_step", "network_bandwidth_max", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cpu_min"]) -> MetaOapg.properties.cpu_min: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cpu_step"]) -> MetaOapg.properties.cpu_step: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cpu_max"]) -> MetaOapg.properties.cpu_max: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ram_min"]) -> MetaOapg.properties.ram_min: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ram_step"]) -> MetaOapg.properties.ram_step: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ram_max"]) -> MetaOapg.properties.ram_max: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["disk_min"]) -> MetaOapg.properties.disk_min: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["disk_step"]) -> MetaOapg.properties.disk_step: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["disk_max"]) -> MetaOapg.properties.disk_max: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["network_bandwidth_min"]) -> MetaOapg.properties.network_bandwidth_min: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["network_bandwidth_step"]) -> MetaOapg.properties.network_bandwidth_step: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["network_bandwidth_max"]) -> MetaOapg.properties.network_bandwidth_max: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cpu_min", "cpu_step", "cpu_max", "ram_min", "ram_step", "ram_max", "disk_min", "disk_step", "disk_max", "network_bandwidth_min", "network_bandwidth_step", "network_bandwidth_max", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    disk_min: typing.Union[MetaOapg.properties.disk_min, decimal.Decimal, int, float, ],
                    disk_max: typing.Union[MetaOapg.properties.disk_max, decimal.Decimal, int, float, ],
                    network_bandwidth_max: typing.Union[MetaOapg.properties.network_bandwidth_max, decimal.Decimal, int, float, ],
                    disk_step: typing.Union[MetaOapg.properties.disk_step, decimal.Decimal, int, float, ],
                    network_bandwidth_step: typing.Union[MetaOapg.properties.network_bandwidth_step, decimal.Decimal, int, float, ],
                    cpu_step: typing.Union[MetaOapg.properties.cpu_step, decimal.Decimal, int, float, ],
                    network_bandwidth_min: typing.Union[MetaOapg.properties.network_bandwidth_min, decimal.Decimal, int, float, ],
                    cpu_max: typing.Union[MetaOapg.properties.cpu_max, decimal.Decimal, int, float, ],
                    ram_min: typing.Union[MetaOapg.properties.ram_min, decimal.Decimal, int, float, ],
                    ram_max: typing.Union[MetaOapg.properties.ram_max, decimal.Decimal, int, float, ],
                    cpu_min: typing.Union[MetaOapg.properties.cpu_min, decimal.Decimal, int, float, ],
                    ram_step: typing.Union[MetaOapg.properties.ram_step, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'requirements':
                    return super().__new__(
                        cls,
                        *_args,
                        disk_min=disk_min,
                        disk_max=disk_max,
                        network_bandwidth_max=network_bandwidth_max,
                        disk_step=disk_step,
                        network_bandwidth_step=network_bandwidth_step,
                        cpu_step=cpu_step,
                        network_bandwidth_min=network_bandwidth_min,
                        cpu_max=cpu_max,
                        ram_min=ram_min,
                        ram_max=ram_max,
                        cpu_min=cpu_min,
                        ram_step=ram_step,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "location": location,
                "disk_type": disk_type,
                "is_allowed_local_network": is_allowed_local_network,
                "cpu_frequency": cpu_frequency,
                "requirements": requirements,
            }

    
    requirements: MetaOapg.properties.requirements
    disk_type: MetaOapg.properties.disk_type
    location: MetaOapg.properties.location
    cpu_frequency: MetaOapg.properties.cpu_frequency
    id: MetaOapg.properties.id
    is_allowed_local_network: MetaOapg.properties.is_allowed_local_network
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_type"]) -> MetaOapg.properties.disk_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_allowed_local_network"]) -> MetaOapg.properties.is_allowed_local_network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_frequency"]) -> MetaOapg.properties.cpu_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> MetaOapg.properties.requirements: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "location", "disk_type", "is_allowed_local_network", "cpu_frequency", "requirements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_type"]) -> MetaOapg.properties.disk_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_allowed_local_network"]) -> MetaOapg.properties.is_allowed_local_network: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_frequency"]) -> MetaOapg.properties.cpu_frequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> MetaOapg.properties.requirements: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "location", "disk_type", "is_allowed_local_network", "cpu_frequency", "requirements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        requirements: typing.Union[MetaOapg.properties.requirements, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        disk_type: typing.Union[MetaOapg.properties.disk_type, str, ],
        location: typing.Union[MetaOapg.properties.location, str, ],
        cpu_frequency: typing.Union[MetaOapg.properties.cpu_frequency, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        is_allowed_local_network: typing.Union[MetaOapg.properties.is_allowed_local_network, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServersConfigurator':
        return super().__new__(
            cls,
            *_args,
            requirements=requirements,
            disk_type=disk_type,
            location=location,
            cpu_frequency=cpu_frequency,
            id=id,
            is_allowed_local_network=is_allowed_local_network,
            _configuration=_configuration,
            **kwargs,
        )
