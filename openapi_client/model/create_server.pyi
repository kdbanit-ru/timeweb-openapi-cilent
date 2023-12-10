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


class CreateServer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bandwidth",
            "name",
            "is_ddos_guard",
        }
        
        class properties:
            is_ddos_guard = schemas.BoolSchema
            bandwidth = schemas.NumberSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class configuration(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "disk",
                        "cpu",
                        "configurator_id",
                        "ram",
                    }
                    
                    class properties:
                        configurator_id = schemas.NumberSchema
                        disk = schemas.NumberSchema
                        cpu = schemas.NumberSchema
                        ram = schemas.NumberSchema
                        __annotations__ = {
                            "configurator_id": configurator_id,
                            "disk": disk,
                            "cpu": cpu,
                            "ram": ram,
                        }
                
                disk: MetaOapg.properties.disk
                cpu: MetaOapg.properties.cpu
                configurator_id: MetaOapg.properties.configurator_id
                ram: MetaOapg.properties.ram
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["configurator_id"]) -> MetaOapg.properties.configurator_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["disk"]) -> MetaOapg.properties.disk: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cpu"]) -> MetaOapg.properties.cpu: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ram"]) -> MetaOapg.properties.ram: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurator_id", "disk", "cpu", "ram", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["configurator_id"]) -> MetaOapg.properties.configurator_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["disk"]) -> MetaOapg.properties.disk: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cpu"]) -> MetaOapg.properties.cpu: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ram"]) -> MetaOapg.properties.ram: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurator_id", "disk", "cpu", "ram", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    disk: typing.Union[MetaOapg.properties.disk, decimal.Decimal, int, float, ],
                    cpu: typing.Union[MetaOapg.properties.cpu, decimal.Decimal, int, float, ],
                    configurator_id: typing.Union[MetaOapg.properties.configurator_id, decimal.Decimal, int, float, ],
                    ram: typing.Union[MetaOapg.properties.ram, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'configuration':
                    return super().__new__(
                        cls,
                        *_args,
                        disk=disk,
                        cpu=cpu,
                        configurator_id=configurator_id,
                        ram=ram,
                        _configuration=_configuration,
                        **kwargs,
                    )
            os_id = schemas.NumberSchema
            image_id = schemas.UUIDSchema
            software_id = schemas.NumberSchema
            preset_id = schemas.NumberSchema
            avatar_id = schemas.StrSchema
            
            
            class comment(
                schemas.StrSchema
            ):
                pass
            
            
            class ssh_keys_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssh_keys_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            is_local_network = schemas.BoolSchema
        
            @staticmethod
            def network() -> typing.Type['Network']:
                return Network
            cloud_init = schemas.StrSchema
            __annotations__ = {
                "is_ddos_guard": is_ddos_guard,
                "bandwidth": bandwidth,
                "name": name,
                "configuration": configuration,
                "os_id": os_id,
                "image_id": image_id,
                "software_id": software_id,
                "preset_id": preset_id,
                "avatar_id": avatar_id,
                "comment": comment,
                "ssh_keys_ids": ssh_keys_ids,
                "is_local_network": is_local_network,
                "network": network,
                "cloud_init": cloud_init,
            }

    
    bandwidth: MetaOapg.properties.bandwidth
    name: MetaOapg.properties.name
    is_ddos_guard: MetaOapg.properties.is_ddos_guard
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_ddos_guard"]) -> MetaOapg.properties.is_ddos_guard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bandwidth"]) -> MetaOapg.properties.bandwidth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> MetaOapg.properties.configuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_id"]) -> MetaOapg.properties.os_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_id"]) -> MetaOapg.properties.image_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["software_id"]) -> MetaOapg.properties.software_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preset_id"]) -> MetaOapg.properties.preset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_id"]) -> MetaOapg.properties.avatar_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssh_keys_ids"]) -> MetaOapg.properties.ssh_keys_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_local_network"]) -> MetaOapg.properties.is_local_network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'Network': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloud_init"]) -> MetaOapg.properties.cloud_init: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_ddos_guard", "bandwidth", "name", "configuration", "os_id", "image_id", "software_id", "preset_id", "avatar_id", "comment", "ssh_keys_ids", "is_local_network", "network", "cloud_init", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_ddos_guard"]) -> MetaOapg.properties.is_ddos_guard: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bandwidth"]) -> MetaOapg.properties.bandwidth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union[MetaOapg.properties.configuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_id"]) -> typing.Union[MetaOapg.properties.os_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_id"]) -> typing.Union[MetaOapg.properties.image_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["software_id"]) -> typing.Union[MetaOapg.properties.software_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preset_id"]) -> typing.Union[MetaOapg.properties.preset_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_id"]) -> typing.Union[MetaOapg.properties.avatar_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssh_keys_ids"]) -> typing.Union[MetaOapg.properties.ssh_keys_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_local_network"]) -> typing.Union[MetaOapg.properties.is_local_network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> typing.Union['Network', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloud_init"]) -> typing.Union[MetaOapg.properties.cloud_init, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_ddos_guard", "bandwidth", "name", "configuration", "os_id", "image_id", "software_id", "preset_id", "avatar_id", "comment", "ssh_keys_ids", "is_local_network", "network", "cloud_init", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        bandwidth: typing.Union[MetaOapg.properties.bandwidth, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        is_ddos_guard: typing.Union[MetaOapg.properties.is_ddos_guard, bool, ],
        configuration: typing.Union[MetaOapg.properties.configuration, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        os_id: typing.Union[MetaOapg.properties.os_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        image_id: typing.Union[MetaOapg.properties.image_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        software_id: typing.Union[MetaOapg.properties.software_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        preset_id: typing.Union[MetaOapg.properties.preset_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        avatar_id: typing.Union[MetaOapg.properties.avatar_id, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        ssh_keys_ids: typing.Union[MetaOapg.properties.ssh_keys_ids, list, tuple, schemas.Unset] = schemas.unset,
        is_local_network: typing.Union[MetaOapg.properties.is_local_network, bool, schemas.Unset] = schemas.unset,
        network: typing.Union['Network', schemas.Unset] = schemas.unset,
        cloud_init: typing.Union[MetaOapg.properties.cloud_init, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateServer':
        return super().__new__(
            cls,
            *_args,
            bandwidth=bandwidth,
            name=name,
            is_ddos_guard=is_ddos_guard,
            configuration=configuration,
            os_id=os_id,
            image_id=image_id,
            software_id=software_id,
            preset_id=preset_id,
            avatar_id=avatar_id,
            comment=comment,
            ssh_keys_ids=ssh_keys_ids,
            is_local_network=is_local_network,
            network=network,
            cloud_init=cloud_init,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.network import Network