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


class ConfigParameters(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            auto_increment_increment = schemas.StrSchema
            auto_increment_offset = schemas.StrSchema
            innodb_io_capacity = schemas.StrSchema
            innodb_purge_threads = schemas.StrSchema
            innodb_read_io_threads = schemas.StrSchema
            innodb_thread_concurrency = schemas.StrSchema
            innodb_write_io_threads = schemas.StrSchema
            join_buffer_size = schemas.StrSchema
            max_allowed_packet = schemas.StrSchema
            max_heap_table_size = schemas.StrSchema
            autovacuum_analyze_scale_factor = schemas.StrSchema
            bgwriter_delay = schemas.StrSchema
            bgwriter_lru_maxpages = schemas.StrSchema
            deadlock_timeout = schemas.StrSchema
            gin_pending_list_limit = schemas.StrSchema
            idle_in_transaction_session_timeout = schemas.StrSchema
            idle_session_timeout = schemas.StrSchema
            join_collapse_limit = schemas.StrSchema
            lock_timeout = schemas.StrSchema
            max_prepared_transactions = schemas.StrSchema
            max_connections = schemas.StrSchema
            shared_buffers = schemas.StrSchema
            wal_buffers = schemas.StrSchema
            temp_buffers = schemas.StrSchema
            work_mem = schemas.StrSchema
            sql_mode = schemas.StrSchema
            query_cache_type = schemas.StrSchema
            query_cache_size = schemas.StrSchema
            __annotations__ = {
                "auto_increment_increment": auto_increment_increment,
                "auto_increment_offset": auto_increment_offset,
                "innodb_io_capacity": innodb_io_capacity,
                "innodb_purge_threads": innodb_purge_threads,
                "innodb_read_io_threads": innodb_read_io_threads,
                "innodb_thread_concurrency": innodb_thread_concurrency,
                "innodb_write_io_threads": innodb_write_io_threads,
                "join_buffer_size": join_buffer_size,
                "max_allowed_packet": max_allowed_packet,
                "max_heap_table_size": max_heap_table_size,
                "autovacuum_analyze_scale_factor": autovacuum_analyze_scale_factor,
                "bgwriter_delay": bgwriter_delay,
                "bgwriter_lru_maxpages": bgwriter_lru_maxpages,
                "deadlock_timeout": deadlock_timeout,
                "gin_pending_list_limit": gin_pending_list_limit,
                "idle_in_transaction_session_timeout": idle_in_transaction_session_timeout,
                "idle_session_timeout": idle_session_timeout,
                "join_collapse_limit": join_collapse_limit,
                "lock_timeout": lock_timeout,
                "max_prepared_transactions": max_prepared_transactions,
                "max_connections": max_connections,
                "shared_buffers": shared_buffers,
                "wal_buffers": wal_buffers,
                "temp_buffers": temp_buffers,
                "work_mem": work_mem,
                "sql_mode": sql_mode,
                "query_cache_type": query_cache_type,
                "query_cache_size": query_cache_size,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_increment_increment"]) -> MetaOapg.properties.auto_increment_increment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_increment_offset"]) -> MetaOapg.properties.auto_increment_offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["innodb_io_capacity"]) -> MetaOapg.properties.innodb_io_capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["innodb_purge_threads"]) -> MetaOapg.properties.innodb_purge_threads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["innodb_read_io_threads"]) -> MetaOapg.properties.innodb_read_io_threads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["innodb_thread_concurrency"]) -> MetaOapg.properties.innodb_thread_concurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["innodb_write_io_threads"]) -> MetaOapg.properties.innodb_write_io_threads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join_buffer_size"]) -> MetaOapg.properties.join_buffer_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_allowed_packet"]) -> MetaOapg.properties.max_allowed_packet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_heap_table_size"]) -> MetaOapg.properties.max_heap_table_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autovacuum_analyze_scale_factor"]) -> MetaOapg.properties.autovacuum_analyze_scale_factor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bgwriter_delay"]) -> MetaOapg.properties.bgwriter_delay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bgwriter_lru_maxpages"]) -> MetaOapg.properties.bgwriter_lru_maxpages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deadlock_timeout"]) -> MetaOapg.properties.deadlock_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gin_pending_list_limit"]) -> MetaOapg.properties.gin_pending_list_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idle_in_transaction_session_timeout"]) -> MetaOapg.properties.idle_in_transaction_session_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idle_session_timeout"]) -> MetaOapg.properties.idle_session_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join_collapse_limit"]) -> MetaOapg.properties.join_collapse_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_timeout"]) -> MetaOapg.properties.lock_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_prepared_transactions"]) -> MetaOapg.properties.max_prepared_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_connections"]) -> MetaOapg.properties.max_connections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_buffers"]) -> MetaOapg.properties.shared_buffers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wal_buffers"]) -> MetaOapg.properties.wal_buffers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temp_buffers"]) -> MetaOapg.properties.temp_buffers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_mem"]) -> MetaOapg.properties.work_mem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sql_mode"]) -> MetaOapg.properties.sql_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query_cache_type"]) -> MetaOapg.properties.query_cache_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query_cache_size"]) -> MetaOapg.properties.query_cache_size: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auto_increment_increment", "auto_increment_offset", "innodb_io_capacity", "innodb_purge_threads", "innodb_read_io_threads", "innodb_thread_concurrency", "innodb_write_io_threads", "join_buffer_size", "max_allowed_packet", "max_heap_table_size", "autovacuum_analyze_scale_factor", "bgwriter_delay", "bgwriter_lru_maxpages", "deadlock_timeout", "gin_pending_list_limit", "idle_in_transaction_session_timeout", "idle_session_timeout", "join_collapse_limit", "lock_timeout", "max_prepared_transactions", "max_connections", "shared_buffers", "wal_buffers", "temp_buffers", "work_mem", "sql_mode", "query_cache_type", "query_cache_size", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_increment_increment"]) -> typing.Union[MetaOapg.properties.auto_increment_increment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_increment_offset"]) -> typing.Union[MetaOapg.properties.auto_increment_offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["innodb_io_capacity"]) -> typing.Union[MetaOapg.properties.innodb_io_capacity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["innodb_purge_threads"]) -> typing.Union[MetaOapg.properties.innodb_purge_threads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["innodb_read_io_threads"]) -> typing.Union[MetaOapg.properties.innodb_read_io_threads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["innodb_thread_concurrency"]) -> typing.Union[MetaOapg.properties.innodb_thread_concurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["innodb_write_io_threads"]) -> typing.Union[MetaOapg.properties.innodb_write_io_threads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join_buffer_size"]) -> typing.Union[MetaOapg.properties.join_buffer_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_allowed_packet"]) -> typing.Union[MetaOapg.properties.max_allowed_packet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_heap_table_size"]) -> typing.Union[MetaOapg.properties.max_heap_table_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autovacuum_analyze_scale_factor"]) -> typing.Union[MetaOapg.properties.autovacuum_analyze_scale_factor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bgwriter_delay"]) -> typing.Union[MetaOapg.properties.bgwriter_delay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bgwriter_lru_maxpages"]) -> typing.Union[MetaOapg.properties.bgwriter_lru_maxpages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deadlock_timeout"]) -> typing.Union[MetaOapg.properties.deadlock_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gin_pending_list_limit"]) -> typing.Union[MetaOapg.properties.gin_pending_list_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idle_in_transaction_session_timeout"]) -> typing.Union[MetaOapg.properties.idle_in_transaction_session_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idle_session_timeout"]) -> typing.Union[MetaOapg.properties.idle_session_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join_collapse_limit"]) -> typing.Union[MetaOapg.properties.join_collapse_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_timeout"]) -> typing.Union[MetaOapg.properties.lock_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_prepared_transactions"]) -> typing.Union[MetaOapg.properties.max_prepared_transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_connections"]) -> typing.Union[MetaOapg.properties.max_connections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_buffers"]) -> typing.Union[MetaOapg.properties.shared_buffers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wal_buffers"]) -> typing.Union[MetaOapg.properties.wal_buffers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temp_buffers"]) -> typing.Union[MetaOapg.properties.temp_buffers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_mem"]) -> typing.Union[MetaOapg.properties.work_mem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sql_mode"]) -> typing.Union[MetaOapg.properties.sql_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query_cache_type"]) -> typing.Union[MetaOapg.properties.query_cache_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query_cache_size"]) -> typing.Union[MetaOapg.properties.query_cache_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auto_increment_increment", "auto_increment_offset", "innodb_io_capacity", "innodb_purge_threads", "innodb_read_io_threads", "innodb_thread_concurrency", "innodb_write_io_threads", "join_buffer_size", "max_allowed_packet", "max_heap_table_size", "autovacuum_analyze_scale_factor", "bgwriter_delay", "bgwriter_lru_maxpages", "deadlock_timeout", "gin_pending_list_limit", "idle_in_transaction_session_timeout", "idle_session_timeout", "join_collapse_limit", "lock_timeout", "max_prepared_transactions", "max_connections", "shared_buffers", "wal_buffers", "temp_buffers", "work_mem", "sql_mode", "query_cache_type", "query_cache_size", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        auto_increment_increment: typing.Union[MetaOapg.properties.auto_increment_increment, str, schemas.Unset] = schemas.unset,
        auto_increment_offset: typing.Union[MetaOapg.properties.auto_increment_offset, str, schemas.Unset] = schemas.unset,
        innodb_io_capacity: typing.Union[MetaOapg.properties.innodb_io_capacity, str, schemas.Unset] = schemas.unset,
        innodb_purge_threads: typing.Union[MetaOapg.properties.innodb_purge_threads, str, schemas.Unset] = schemas.unset,
        innodb_read_io_threads: typing.Union[MetaOapg.properties.innodb_read_io_threads, str, schemas.Unset] = schemas.unset,
        innodb_thread_concurrency: typing.Union[MetaOapg.properties.innodb_thread_concurrency, str, schemas.Unset] = schemas.unset,
        innodb_write_io_threads: typing.Union[MetaOapg.properties.innodb_write_io_threads, str, schemas.Unset] = schemas.unset,
        join_buffer_size: typing.Union[MetaOapg.properties.join_buffer_size, str, schemas.Unset] = schemas.unset,
        max_allowed_packet: typing.Union[MetaOapg.properties.max_allowed_packet, str, schemas.Unset] = schemas.unset,
        max_heap_table_size: typing.Union[MetaOapg.properties.max_heap_table_size, str, schemas.Unset] = schemas.unset,
        autovacuum_analyze_scale_factor: typing.Union[MetaOapg.properties.autovacuum_analyze_scale_factor, str, schemas.Unset] = schemas.unset,
        bgwriter_delay: typing.Union[MetaOapg.properties.bgwriter_delay, str, schemas.Unset] = schemas.unset,
        bgwriter_lru_maxpages: typing.Union[MetaOapg.properties.bgwriter_lru_maxpages, str, schemas.Unset] = schemas.unset,
        deadlock_timeout: typing.Union[MetaOapg.properties.deadlock_timeout, str, schemas.Unset] = schemas.unset,
        gin_pending_list_limit: typing.Union[MetaOapg.properties.gin_pending_list_limit, str, schemas.Unset] = schemas.unset,
        idle_in_transaction_session_timeout: typing.Union[MetaOapg.properties.idle_in_transaction_session_timeout, str, schemas.Unset] = schemas.unset,
        idle_session_timeout: typing.Union[MetaOapg.properties.idle_session_timeout, str, schemas.Unset] = schemas.unset,
        join_collapse_limit: typing.Union[MetaOapg.properties.join_collapse_limit, str, schemas.Unset] = schemas.unset,
        lock_timeout: typing.Union[MetaOapg.properties.lock_timeout, str, schemas.Unset] = schemas.unset,
        max_prepared_transactions: typing.Union[MetaOapg.properties.max_prepared_transactions, str, schemas.Unset] = schemas.unset,
        max_connections: typing.Union[MetaOapg.properties.max_connections, str, schemas.Unset] = schemas.unset,
        shared_buffers: typing.Union[MetaOapg.properties.shared_buffers, str, schemas.Unset] = schemas.unset,
        wal_buffers: typing.Union[MetaOapg.properties.wal_buffers, str, schemas.Unset] = schemas.unset,
        temp_buffers: typing.Union[MetaOapg.properties.temp_buffers, str, schemas.Unset] = schemas.unset,
        work_mem: typing.Union[MetaOapg.properties.work_mem, str, schemas.Unset] = schemas.unset,
        sql_mode: typing.Union[MetaOapg.properties.sql_mode, str, schemas.Unset] = schemas.unset,
        query_cache_type: typing.Union[MetaOapg.properties.query_cache_type, str, schemas.Unset] = schemas.unset,
        query_cache_size: typing.Union[MetaOapg.properties.query_cache_size, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfigParameters':
        return super().__new__(
            cls,
            *_args,
            auto_increment_increment=auto_increment_increment,
            auto_increment_offset=auto_increment_offset,
            innodb_io_capacity=innodb_io_capacity,
            innodb_purge_threads=innodb_purge_threads,
            innodb_read_io_threads=innodb_read_io_threads,
            innodb_thread_concurrency=innodb_thread_concurrency,
            innodb_write_io_threads=innodb_write_io_threads,
            join_buffer_size=join_buffer_size,
            max_allowed_packet=max_allowed_packet,
            max_heap_table_size=max_heap_table_size,
            autovacuum_analyze_scale_factor=autovacuum_analyze_scale_factor,
            bgwriter_delay=bgwriter_delay,
            bgwriter_lru_maxpages=bgwriter_lru_maxpages,
            deadlock_timeout=deadlock_timeout,
            gin_pending_list_limit=gin_pending_list_limit,
            idle_in_transaction_session_timeout=idle_in_transaction_session_timeout,
            idle_session_timeout=idle_session_timeout,
            join_collapse_limit=join_collapse_limit,
            lock_timeout=lock_timeout,
            max_prepared_transactions=max_prepared_transactions,
            max_connections=max_connections,
            shared_buffers=shared_buffers,
            wal_buffers=wal_buffers,
            temp_buffers=temp_buffers,
            work_mem=work_mem,
            sql_mode=sql_mode,
            query_cache_type=query_cache_type,
            query_cache_size=query_cache_size,
            _configuration=_configuration,
            **kwargs,
        )
