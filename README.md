# openapi-client
# Введение
API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.

Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.

В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.


## Запросы
Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса:
|Метод|Применение|
|--- |--- |
|GET|Извлекает данные о коллекциях и отдельных ресурсах.|
|POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.|
|PUT|Обновляет существующий ресурс.|
|PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.|
|DELETE|Удаляет ресурс.|

Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.

### Параметры в запросах
Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать:
- `limit` — обозначает количество записей, которое необходимо вернуть
 - `offset` — указывает на смещение, относительно начала списка
 - `search` — позволяет указать набор символов для поиска
 - `sort` — можно задать правило сортировки коллекции

## Ответы
Запросы вернут один из следующих кодов состояния ответа HTTP:

|Статус|Описание|
|--- |--- |
|200 OK|Действие с ресурсом было выполнено успешно.|
|201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.|
|204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.|
|400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.|
|401 Unauthorized|Ошибка аутентификации.|
|403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.|
|404 Not Found|Запрашиваемый ресурс не найден.|
|409 Conflict|Запрос конфликтует с текущим состоянием.|
|423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.|
|429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.|
|500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|

### Структура успешного ответа
Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов: 
|Название поля|Тип|Описание|
|--- |--- |--- |
|[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.|
|meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.|
|response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|

Пример запроса на получение списка SSH-ключей:
```
    HTTP/2.0 200 OK
    {
      \"ssh_keys\":[
          {
            \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",
            \"created_at\":\"2021-09-15T19:52:27Z\",
            \"expired_at\":null,
            \"id\":5297,
            \"is_default\":false,
            \"name\":\"example@device.local\",
            \"used_at\":null,
            \"used_by\":[]
          }
      ],
      \"meta\":{
          \"total\":1
      },
      \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"
    }
```

### Структура ответа с ошибкой
|Название поля|Тип|Описание|
|--- |--- |--- |
|status_code|number|Короткий числовой идентификатор ошибки.|
|error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.|
|message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.|
|response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|

Пример:
```
    HTTP/2.0 403 Forbidden
    {
      \"status_code\": 403,
      \"error_code\":  \"forbidden\",
      \"message\":     \"You do not have access for the attempted action\",
      \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"
    }
```

## Статусы ресурсов
Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.

Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.

Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.

 

## Ограничение скорости запросов (Rate Limiting)
Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.

Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.


## Аутентификация
Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.

Токен необходимо передавать в заголовке каждого запроса в формате:
```
  Authorization: Bearer $TIMEWEB_CLOUD_TOKEN
```

## Формат примеров API
Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.

Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так:
```
  curl -X PATCH 
    -H \"Content-Type: application/json\" 
    -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\" 
    -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}' 
    \"https://api.timeweb.cloud/api/v1/dedicated/1051\"
```
- Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`.
- Строки `-H` задают требуемые HTTP-заголовки.
- Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.

Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:

```
TIMEWEB_CLOUD_TOKEN=\"token\"
```

После этого токен будет автоматически подставляться в ваши запросы.

Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.


## Версионирование
API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.

Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import firewall_api
from openapi_client.model.firewall_group_in_api import FirewallGroupInAPI
from openapi_client.model.firewall_group_out_response import FirewallGroupOutResponse
from openapi_client.model.firewall_group_resource_out_response import FirewallGroupResourceOutResponse
from openapi_client.model.firewall_group_resources_out_response import FirewallGroupResourcesOutResponse
from openapi_client.model.firewall_groups_out_response import FirewallGroupsOutResponse
from openapi_client.model.firewall_rule_in_api import FirewallRuleInAPI
from openapi_client.model.firewall_rule_out_response import FirewallRuleOutResponse
from openapi_client.model.firewall_rules_out_response import FirewallRulesOutResponse
from openapi_client.model.resource_type import ResourceType
# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firewall_api.FirewallApi(api_client)
    group_id = "group_id_example" # str | Идентификатор группы правил
resource_id = "resource_id_example" # str | Идентификатор ресурса
resource_type = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=false, isModel=true, isExplode=true, baseName='resource_type', paramName='resource_type', dataType='bool, date, datetime, dict, float, int, list, str, none_type', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='null', unescapedDescription='null', baseType='null', defaultValue='server', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='None', jsonSchema='{
  "name" : "resource_type",
  "in" : "query",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "allOf" : [ {
      "$ref" : "#/components/schemas/ResourceType"
    } ],
    "default" : "server"
  }
}', isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=true, isArray=false, isMap=false, isFile=false, isEnum=false, isEnumRef=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=CodegenComposedSchemas{oneOf=null, anyOf=null, allOf=[CodegenProperty{openApiType='ResourceType', baseName='all_of_0', complexType='ResourceType', getter='getAllOf0', setter='setAllOf0', description='null', dataType='ResourceType', datatypeWithEnum='ResourceType', dataFormat='null', name='all_of_0', min='null', max='null', defaultValue='null', defaultValueWithParam=' = data.all_of_0;', baseType='ResourceType', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='ResourceType("server")', jsonSchema='{
  "$ref" : "#/components/schemas/ResourceType"
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=false, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues={values=[server]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='AllOf0', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=#/components/schemas/ResourceType, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}], not=null}, hasMultipleTypes=false, schema=CodegenProperty{openApiType='object', baseName='ResourceTypeSchema', complexType='null', getter='getResourceType', setter='setResourceType', description='null', dataType='bool, date, datetime, dict, float, int, list, str, none_type', datatypeWithEnum='bool, date, datetime, dict, float, int, list, str, none_type', dataFormat='null', name='resource_type', min='null', max='null', defaultValue='server', defaultValueWithParam=' = data.resource_type;', baseType='object', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='None', jsonSchema='{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ResourceType"
  } ],
  "default" : "server"
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=true, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=true, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='ResourceType', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=CodegenComposedSchemas{oneOf=null, anyOf=null, allOf=[CodegenProperty{openApiType='ResourceType', baseName='all_of_0', complexType='ResourceType', getter='getAllOf0', setter='setAllOf0', description='null', dataType='ResourceType', datatypeWithEnum='ResourceType', dataFormat='null', name='all_of_0', min='null', max='null', defaultValue='null', defaultValueWithParam=' = data.all_of_0;', baseType='ResourceType', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='ResourceType("server")', jsonSchema='{
  "$ref" : "#/components/schemas/ResourceType"
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=false, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues={values=[server]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='AllOf0', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=#/components/schemas/ResourceType, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}], not=null}, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})

    try:
        # Линковка ресурса в firewall group
        api_response = api_instance.add_resource_to_group(group_idresource_idresource_type=resource_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FirewallApi->add_resource_to_group: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.timeweb.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FirewallApi* | [**add_resource_to_group**](docs/apis/tags/FirewallApi.md#add_resource_to_group) | **post** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Линковка ресурса в firewall group
*FirewallApi* | [**create_group**](docs/apis/tags/FirewallApi.md#create_group) | **post** /api/v1/firewall/groups | Создание группы правил
*FirewallApi* | [**create_group_rule**](docs/apis/tags/FirewallApi.md#create_group_rule) | **post** /api/v1/firewall/groups/{group_id}/rules | Создание firewall правила
*FirewallApi* | [**delete_group**](docs/apis/tags/FirewallApi.md#delete_group) | **delete** /api/v1/firewall/groups/{group_id} | Удаление группы правил
*FirewallApi* | [**delete_group_rule**](docs/apis/tags/FirewallApi.md#delete_group_rule) | **delete** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Удаление firewall правила
*FirewallApi* | [**delete_resource_from_group**](docs/apis/tags/FirewallApi.md#delete_resource_from_group) | **delete** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Отлинковка ресурса из firewall group
*FirewallApi* | [**get_group**](docs/apis/tags/FirewallApi.md#get_group) | **get** /api/v1/firewall/groups/{group_id} | Получение информации о группе правил
*FirewallApi* | [**get_group_resources**](docs/apis/tags/FirewallApi.md#get_group_resources) | **get** /api/v1/firewall/groups/{group_id}/resources | Получение слинкованных ресурсов
*FirewallApi* | [**get_group_rule**](docs/apis/tags/FirewallApi.md#get_group_rule) | **get** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Получение информации о правиле
*FirewallApi* | [**get_group_rules**](docs/apis/tags/FirewallApi.md#get_group_rules) | **get** /api/v1/firewall/groups/{group_id}/rules | Получение списка правил
*FirewallApi* | [**get_groups**](docs/apis/tags/FirewallApi.md#get_groups) | **get** /api/v1/firewall/groups | Получение групп правил
*FirewallApi* | [**get_rules_for_resource**](docs/apis/tags/FirewallApi.md#get_rules_for_resource) | **get** /api/v1/firewall/service/{resource_type}/{resource_id} | Получение групп правил для ресурса
*FirewallApi* | [**update_group**](docs/apis/tags/FirewallApi.md#update_group) | **patch** /api/v1/firewall/groups/{group_id} | Обновление группы правил
*FirewallApi* | [**update_group_rule**](docs/apis/tags/FirewallApi.md#update_group_rule) | **patch** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Обновление firewall правила
*KubernetesApi* | [**create_cluster**](docs/apis/tags/KubernetesApi.md#create_cluster) | **post** /api/v1/k8s/clusters | Создание кластера
*KubernetesApi* | [**create_cluster_node_group**](docs/apis/tags/KubernetesApi.md#create_cluster_node_group) | **post** /api/v1/k8s/clusters/{cluster_id}/groups | Создание группы нод
*KubernetesApi* | [**delete_cluster**](docs/apis/tags/KubernetesApi.md#delete_cluster) | **delete** /api/v1/k8s/clusters/{cluster_id} | Удаление кластера
*KubernetesApi* | [**delete_cluster_node**](docs/apis/tags/KubernetesApi.md#delete_cluster_node) | **delete** /api/v1/k8s/clusters/{cluster_id}/nodes/{node_id} | Удаление ноды
*KubernetesApi* | [**delete_cluster_node_group**](docs/apis/tags/KubernetesApi.md#delete_cluster_node_group) | **delete** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Удаление группы нод
*KubernetesApi* | [**get_cluster**](docs/apis/tags/KubernetesApi.md#get_cluster) | **get** /api/v1/k8s/clusters/{cluster_id} | Получение информации о кластере
*KubernetesApi* | [**get_cluster_kubeconfig**](docs/apis/tags/KubernetesApi.md#get_cluster_kubeconfig) | **get** /api/v1/k8s/clusters/{cluster_id}/kubeconfig | Получение файла kubeconfig
*KubernetesApi* | [**get_cluster_node_group**](docs/apis/tags/KubernetesApi.md#get_cluster_node_group) | **get** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Получение информации о группе нод
*KubernetesApi* | [**get_cluster_node_groups**](docs/apis/tags/KubernetesApi.md#get_cluster_node_groups) | **get** /api/v1/k8s/clusters/{cluster_id}/groups | Получение групп нод кластера
*KubernetesApi* | [**get_cluster_nodes**](docs/apis/tags/KubernetesApi.md#get_cluster_nodes) | **get** /api/v1/k8s/clusters/{cluster_id}/nodes | Получение списка нод
*KubernetesApi* | [**get_cluster_nodes_from_group**](docs/apis/tags/KubernetesApi.md#get_cluster_nodes_from_group) | **get** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Получение списка нод, принадлежащих группе
*KubernetesApi* | [**get_cluster_resources**](docs/apis/tags/KubernetesApi.md#get_cluster_resources) | **get** /api/v1/k8s/clusters/{cluster_id}/resources | Получение ресурсов кластера
*KubernetesApi* | [**get_clusters**](docs/apis/tags/KubernetesApi.md#get_clusters) | **get** /api/v1/k8s/clusters | Получение списка кластеров
*KubernetesApi* | [**get_k8_s_network_drivers**](docs/apis/tags/KubernetesApi.md#get_k8_s_network_drivers) | **get** /api/v1/k8s/network_drivers | Получение списка сетевых драйверов k8s
*KubernetesApi* | [**get_k8_s_versions**](docs/apis/tags/KubernetesApi.md#get_k8_s_versions) | **get** /api/v1/k8s/k8s_versions | Получение списка версий k8s
*KubernetesApi* | [**get_kubernetes_presets**](docs/apis/tags/KubernetesApi.md#get_kubernetes_presets) | **get** /api/v1/presets/k8s | Получение списка тарифов
*KubernetesApi* | [**increase_count_of_nodes_in_group**](docs/apis/tags/KubernetesApi.md#increase_count_of_nodes_in_group) | **post** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Увеличение количества нод в группе на указанное количество
*KubernetesApi* | [**reduce_count_of_nodes_in_group**](docs/apis/tags/KubernetesApi.md#reduce_count_of_nodes_in_group) | **delete** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Уменьшение количества нод в группе на указанное количество
*KubernetesApi* | [**update_cluster**](docs/apis/tags/KubernetesApi.md#update_cluster) | **patch** /api/v1/k8s/clusters/{cluster_id} | Обновление информации о кластере
*S3Api* | [**add_storage_subdomain_certificate**](docs/apis/tags/S3Api.md#add_storage_subdomain_certificate) | **post** /api/v1/storages/certificates/generate | Добавление сертификата для поддомена хранилища
*S3Api* | [**add_storage_subdomains**](docs/apis/tags/S3Api.md#add_storage_subdomains) | **post** /api/v1/storages/buckets/{bucket_id}/subdomains | Добавление поддоменов для хранилища
*S3Api* | [**copy_storage_file**](docs/apis/tags/S3Api.md#copy_storage_file) | **post** /api/v1/storages/buckets/{bucket_id}/object-manager/copy | Копирование файла/директории в хранилище
*S3Api* | [**create_folder_in_storage**](docs/apis/tags/S3Api.md#create_folder_in_storage) | **post** /api/v1/storages/buckets/{bucket_id}/object-manager/mkdir | Создание директории в хранилище
*S3Api* | [**create_storage**](docs/apis/tags/S3Api.md#create_storage) | **post** /api/v1/storages/buckets | Создание хранилища
*S3Api* | [**delete_storage**](docs/apis/tags/S3Api.md#delete_storage) | **delete** /api/v1/storages/buckets/{bucket_id} | Удаление хранилища на аккаунте
*S3Api* | [**delete_storage_file**](docs/apis/tags/S3Api.md#delete_storage_file) | **delete** /api/v1/storages/buckets/{bucket_id}/object-manager/remove | Удаление файла/директории в хранилище
*S3Api* | [**delete_storage_subdomains**](docs/apis/tags/S3Api.md#delete_storage_subdomains) | **delete** /api/v1/storages/buckets/{bucket_id}/subdomains | Удаление поддоменов хранилища
*S3Api* | [**get_storage_files_list**](docs/apis/tags/S3Api.md#get_storage_files_list) | **get** /api/v1/storages/buckets/{bucket_id}/object-manager/list | Получение списка файлов в хранилище по префиксу
*S3Api* | [**get_storage_subdomains**](docs/apis/tags/S3Api.md#get_storage_subdomains) | **get** /api/v1/storages/buckets/{bucket_id}/subdomains | Получение списка поддоменов хранилища
*S3Api* | [**get_storage_transfer_status**](docs/apis/tags/S3Api.md#get_storage_transfer_status) | **get** /api/v1/storages/buckets/{bucket_id}/transfer-status | Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud
*S3Api* | [**get_storage_users**](docs/apis/tags/S3Api.md#get_storage_users) | **get** /api/v1/storages/users | Получение списка пользователей хранилищ аккаунта
*S3Api* | [**get_storages**](docs/apis/tags/S3Api.md#get_storages) | **get** /api/v1/storages/buckets | Получение списка хранилищ аккаунта
*S3Api* | [**get_storages_presets**](docs/apis/tags/S3Api.md#get_storages_presets) | **get** /api/v1/presets/storages | Получение списка тарифов для хранилищ
*S3Api* | [**rename_storage_file**](docs/apis/tags/S3Api.md#rename_storage_file) | **post** /api/v1/storages/buckets/{bucket_id}/object-manager/rename | Переименование файла/директории в хранилище
*S3Api* | [**transfer_storage**](docs/apis/tags/S3Api.md#transfer_storage) | **post** /api/v1/storages/transfer | Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud
*S3Api* | [**update_storage**](docs/apis/tags/S3Api.md#update_storage) | **patch** /api/v1/storages/buckets/{bucket_id} | Изменение хранилища на аккаунте
*S3Api* | [**update_storage_user**](docs/apis/tags/S3Api.md#update_storage_user) | **patch** /api/v1/storages/users/{user_id} | Изменение пароля пользователя-администратора хранилища
*S3Api* | [**upload_file_to_storage**](docs/apis/tags/S3Api.md#upload_file_to_storage) | **post** /api/v1/storages/buckets/{bucket_id}/object-manager/upload | Загрузка файлов в хранилище
*SSHApi* | [**add_key_to_server**](docs/apis/tags/SSHApi.md#add_key_to_server) | **post** /api/v1/servers/{server_id}/ssh-keys | Добавление SSH-ключей на сервер
*SSHApi* | [**create_key**](docs/apis/tags/SSHApi.md#create_key) | **post** /api/v1/ssh-keys | Создание SSH-ключа
*SSHApi* | [**delete_key**](docs/apis/tags/SSHApi.md#delete_key) | **delete** /api/v1/ssh-keys/{ssh_key_id} | Удаление SSH-ключа по уникальному идентификатору
*SSHApi* | [**delete_key_from_server**](docs/apis/tags/SSHApi.md#delete_key_from_server) | **delete** /api/v1/servers/{server_id}/ssh-keys/{ssh_key_id} | Удаление SSH-ключей с сервера
*SSHApi* | [**get_key**](docs/apis/tags/SSHApi.md#get_key) | **get** /api/v1/ssh-keys/{ssh_key_id} | Получение SSH-ключа по уникальному идентификатору
*SSHApi* | [**get_keys**](docs/apis/tags/SSHApi.md#get_keys) | **get** /api/v1/ssh-keys | Получение списка SSH-ключей
*SSHApi* | [**update_key**](docs/apis/tags/SSHApi.md#update_key) | **patch** /api/v1/ssh-keys/{ssh_key_id} | Изменение SSH-ключа по уникальному идентификатору
*VPCApi* | [**create_vpc**](docs/apis/tags/VPCApi.md#create_vpc) | **post** /api/v2/vpcs | Создание VPC
*VPCApi* | [**delete_vpc**](docs/apis/tags/VPCApi.md#delete_vpc) | **delete** /api/v1/vpcs/{vpc_id} | Удаление VPC по идентификатору сети
*VPCApi* | [**get_vpc**](docs/apis/tags/VPCApi.md#get_vpc) | **get** /api/v2/vpcs/{vpc_id} | Получение VPC
*VPCApi* | [**get_vpc_ports**](docs/apis/tags/VPCApi.md#get_vpc_ports) | **get** /api/v1/vpcs/{vpc_id}/ports | Получение списка портов для VPC
*VPCApi* | [**get_vpc_services**](docs/apis/tags/VPCApi.md#get_vpc_services) | **get** /api/v2/vpcs/{vpc_id}/services | Получение списка сервисов в VPC
*VPCApi* | [**get_vpcs**](docs/apis/tags/VPCApi.md#get_vpcs) | **get** /api/v2/vpcs | Получение списка VPCs
*VPCApi* | [**update_vpcs**](docs/apis/tags/VPCApi.md#update_vpcs) | **patch** /api/v2/vpcs/{vpc_id} | Изменение VPC по идентификатору сети
*Api* | [**add_countries_to_allowed_list**](docs/apis/tags/Api.md#add_countries_to_allowed_list) | **post** /api/v1/auth/access/countries | Добавление стран в список разрешенных
*Api* | [**add_ips_to_allowed_list**](docs/apis/tags/Api.md#add_ips_to_allowed_list) | **post** /api/v1/auth/access/ips | Добавление IP-адресов в список разрешенных
*Api* | [**delete_countries_from_allowed_list**](docs/apis/tags/Api.md#delete_countries_from_allowed_list) | **delete** /api/v1/auth/access/countries | Удаление стран из списка разрешенных
*Api* | [**delete_ips_from_allowed_list**](docs/apis/tags/Api.md#delete_ips_from_allowed_list) | **delete** /api/v1/auth/access/ips | Удаление IP-адресов из списка разрешенных
*Api* | [**get_account_status**](docs/apis/tags/Api.md#get_account_status) | **get** /api/v1/account/status | Получение статуса аккаунта
*Api* | [**get_auth_access_settings**](docs/apis/tags/Api.md#get_auth_access_settings) | **get** /api/v1/auth/access | Получить информацию о ограничениях авторизации пользователя
*Api* | [**get_countries**](docs/apis/tags/Api.md#get_countries) | **get** /api/v1/auth/access/countries | Получение списка стран
*Api* | [**get_finances**](docs/apis/tags/Api.md#get_finances) | **get** /api/v1/account/finances | Получение платежной информации
*Api* | [**get_notification_settings**](docs/apis/tags/Api.md#get_notification_settings) | **get** /api/v1/account/notification-settings | Получение настроек уведомлений аккаунта
*Api* | [**update_auth_restrictions_by_countries**](docs/apis/tags/Api.md#update_auth_restrictions_by_countries) | **post** /api/v1/auth/access/countries/enabled | Включение/отключение ограничений по стране
*Api* | [**update_auth_restrictions_by_ip**](docs/apis/tags/Api.md#update_auth_restrictions_by_ip) | **post** /api/v1/auth/access/ips/enabled | Включение/отключение ограничений по IP-адресу
*Api* | [**update_notification_settings**](docs/apis/tags/Api.md#update_notification_settings) | **patch** /api/v1/account/notification-settings | Изменение настроек уведомлений аккаунта
*Api* | [**create_database**](docs/apis/tags/Api.md#create_database) | **post** /api/v1/dbs | Создание базы данных
*Api* | [**create_database_backup**](docs/apis/tags/Api.md#create_database_backup) | **post** /api/v1/dbs/{db_id}/backups | Создание бэкапа базы данных
*Api* | [**create_database_cluster**](docs/apis/tags/Api.md#create_database_cluster) | **post** /api/v1/databases | Создание кластера базы данных
*Api* | [**create_database_instance**](docs/apis/tags/Api.md#create_database_instance) | **post** /api/v1/databases/{db_cluster_id}/instances | Создание инстанса базы данных
*Api* | [**create_database_user**](docs/apis/tags/Api.md#create_database_user) | **post** /api/v1/databases/{db_cluster_id}/admins | Создание пользователя базы данных
*Api* | [**delete_database**](docs/apis/tags/Api.md#delete_database) | **delete** /api/v1/dbs/{db_id} | Удаление базы данных
*Api* | [**delete_database_backup**](docs/apis/tags/Api.md#delete_database_backup) | **delete** /api/v1/dbs/{db_id}/backups/{backup_id} | Удаление бэкапа базы данных
*Api* | [**delete_database_cluster**](docs/apis/tags/Api.md#delete_database_cluster) | **delete** /api/v1/databases/{db_cluster_id} | Удаление кластера базы данных
*Api* | [**delete_database_instance**](docs/apis/tags/Api.md#delete_database_instance) | **delete** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Удаление инстанса базы данных
*Api* | [**delete_database_user**](docs/apis/tags/Api.md#delete_database_user) | **delete** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Удаление пользователя базы данных
*Api* | [**get_database**](docs/apis/tags/Api.md#get_database) | **get** /api/v1/dbs/{db_id} | Получение базы данных
*Api* | [**get_database_auto_backups_settings**](docs/apis/tags/Api.md#get_database_auto_backups_settings) | **get** /api/v1/dbs/{db_id}/auto-backups | Получение настроек автобэкапов базы данных
*Api* | [**get_database_backup**](docs/apis/tags/Api.md#get_database_backup) | **get** /api/v1/dbs/{db_id}/backups/{backup_id} | Получение бэкапа базы данных
*Api* | [**get_database_backups**](docs/apis/tags/Api.md#get_database_backups) | **get** /api/v1/dbs/{db_id}/backups | Список бэкапов базы данных
*Api* | [**get_database_cluster**](docs/apis/tags/Api.md#get_database_cluster) | **get** /api/v1/databases/{db_cluster_id} | Получение кластера базы данных
*Api* | [**get_database_clusters**](docs/apis/tags/Api.md#get_database_clusters) | **get** /api/v1/databases | Получение списка кластеров баз данных
*Api* | [**get_database_instance**](docs/apis/tags/Api.md#get_database_instance) | **get** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Получение инстанса базы данных
*Api* | [**get_database_instances**](docs/apis/tags/Api.md#get_database_instances) | **get** /api/v1/databases/{db_cluster_id}/instances | Получение списка инстансов баз данных
*Api* | [**get_database_user**](docs/apis/tags/Api.md#get_database_user) | **get** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Получение пользователя базы данных
*Api* | [**get_database_users**](docs/apis/tags/Api.md#get_database_users) | **get** /api/v1/databases/{db_cluster_id}/admins | Получение списка пользователей базы данных
*Api* | [**get_databases**](docs/apis/tags/Api.md#get_databases) | **get** /api/v1/dbs | Получение списка всех баз данных
*Api* | [**get_databases_presets**](docs/apis/tags/Api.md#get_databases_presets) | **get** /api/v1/presets/dbs | Получение списка тарифов для баз данных
*Api* | [**restore_database_from_backup**](docs/apis/tags/Api.md#restore_database_from_backup) | **put** /api/v1/dbs/{db_id}/backups/{backup_id} | Восстановление базы данных из бэкапа
*Api* | [**update_database**](docs/apis/tags/Api.md#update_database) | **patch** /api/v1/dbs/{db_id} | Обновление базы данных
*Api* | [**update_database_auto_backups_settings**](docs/apis/tags/Api.md#update_database_auto_backups_settings) | **patch** /api/v1/dbs/{db_id}/auto-backups | Изменение настроек автобэкапов базы данных
*Api* | [**update_database_cluster**](docs/apis/tags/Api.md#update_database_cluster) | **patch** /api/v1/databases/{db_cluster_id} | Изменение кластера базы данных
*Api* | [**update_database_instance**](docs/apis/tags/Api.md#update_database_instance) | **patch** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Изменение инстанса базы данных
*Api* | [**update_database_user**](docs/apis/tags/Api.md#update_database_user) | **patch** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Изменение пользователя базы данных
*Api* | [**add_ips_to_balancer**](docs/apis/tags/Api.md#add_ips_to_balancer) | **post** /api/v1/balancers/{balancer_id}/ips | Добавление IP-адресов к балансировщику
*Api* | [**create_balancer**](docs/apis/tags/Api.md#create_balancer) | **post** /api/v1/balancers | Создание бaлансировщика
*Api* | [**create_balancer_rule**](docs/apis/tags/Api.md#create_balancer_rule) | **post** /api/v1/balancers/{balancer_id}/rules | Создание правила для балансировщика
*Api* | [**delete_balancer**](docs/apis/tags/Api.md#delete_balancer) | **delete** /api/v1/balancers/{balancer_id} | Удаление балансировщика
*Api* | [**delete_balancer_rule**](docs/apis/tags/Api.md#delete_balancer_rule) | **delete** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Удаление правила для балансировщика
*Api* | [**delete_ips_from_balancer**](docs/apis/tags/Api.md#delete_ips_from_balancer) | **delete** /api/v1/balancers/{balancer_id}/ips | Удаление IP-адресов из балансировщика
*Api* | [**get_balancer**](docs/apis/tags/Api.md#get_balancer) | **get** /api/v1/balancers/{balancer_id} | Получение бaлансировщика
*Api* | [**get_balancer_ips**](docs/apis/tags/Api.md#get_balancer_ips) | **get** /api/v1/balancers/{balancer_id}/ips | Получение списка IP-адресов балансировщика
*Api* | [**get_balancer_rules**](docs/apis/tags/Api.md#get_balancer_rules) | **get** /api/v1/balancers/{balancer_id}/rules | Получение правил балансировщика
*Api* | [**get_balancers**](docs/apis/tags/Api.md#get_balancers) | **get** /api/v1/balancers | Получение списка всех бaлансировщиков
*Api* | [**get_balancers_presets**](docs/apis/tags/Api.md#get_balancers_presets) | **get** /api/v1/presets/balancers | Получение списка тарифов для балансировщика
*Api* | [**update_balancer**](docs/apis/tags/Api.md#update_balancer) | **patch** /api/v1/balancers/{balancer_id} | Обновление балансировщика
*Api* | [**update_balancer_rule**](docs/apis/tags/Api.md#update_balancer_rule) | **patch** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Обновление правила для балансировщика
*Api* | [**create_dedicated_server**](docs/apis/tags/Api.md#create_dedicated_server) | **post** /api/v1/dedicated-servers | Создание выделенного сервера
*Api* | [**delete_dedicated_server**](docs/apis/tags/Api.md#delete_dedicated_server) | **delete** /api/v1/dedicated-servers/{dedicated_id} | Удаление выделенного сервера
*Api* | [**get_dedicated_server**](docs/apis/tags/Api.md#get_dedicated_server) | **get** /api/v1/dedicated-servers/{dedicated_id} | Получение выделенного сервера
*Api* | [**get_dedicated_server_preset_additional_services**](docs/apis/tags/Api.md#get_dedicated_server_preset_additional_services) | **get** /api/v1/presets/dedicated-servers/{preset_id}/additional-services | Получение дополнительных услуг для выделенного сервера
*Api* | [**get_dedicated_servers**](docs/apis/tags/Api.md#get_dedicated_servers) | **get** /api/v1/dedicated-servers | Получение списка выделенных серверов
*Api* | [**get_dedicated_servers_presets**](docs/apis/tags/Api.md#get_dedicated_servers_presets) | **get** /api/v1/presets/dedicated-servers | Получение списка тарифов для выделенного сервера
*Api* | [**update_dedicated_server**](docs/apis/tags/Api.md#update_dedicated_server) | **patch** /api/v1/dedicated-servers/{dedicated_id} | Обновление выделенного сервера
*Api* | [**add_domain**](docs/apis/tags/Api.md#add_domain) | **post** /api/v1/add-domain/{fqdn} | Добавление домена на аккаунт
*Api* | [**add_subdomain**](docs/apis/tags/Api.md#add_subdomain) | **post** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Добавление поддомена
*Api* | [**check_domain**](docs/apis/tags/Api.md#check_domain) | **get** /api/v1/check-domain/{fqdn} | Проверить, доступен ли домен для регистрации
*Api* | [**create_domain_dns_record**](docs/apis/tags/Api.md#create_domain_dns_record) | **post** /api/v1/domains/{fqdn}/dns-records | Добавить информацию о DNS-записи для домена или поддомена
*Api* | [**create_domain_request**](docs/apis/tags/Api.md#create_domain_request) | **post** /api/v1/domains-requests | Создание заявки на регистрацию/продление/трансфер домена
*Api* | [**delete_domain**](docs/apis/tags/Api.md#delete_domain) | **delete** /api/v1/domains/{fqdn} | Удаление домена
*Api* | [**delete_domain_dns_record**](docs/apis/tags/Api.md#delete_domain_dns_record) | **delete** /api/v1/domains/{fqdn}/dns-records/{record_id} | Удалить информацию о DNS-записи для домена или поддомена
*Api* | [**delete_subdomain**](docs/apis/tags/Api.md#delete_subdomain) | **delete** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Удаление поддомена
*Api* | [**get_domain**](docs/apis/tags/Api.md#get_domain) | **get** /api/v1/domains/{fqdn} | Получение информации о домене
*Api* | [**get_domain_default_dns_records**](docs/apis/tags/Api.md#get_domain_default_dns_records) | **get** /api/v1/domains/{fqdn}/default-dns-records | Получить информацию обо всех DNS-записях по умолчанию домена или поддомена
*Api* | [**get_domain_dns_records**](docs/apis/tags/Api.md#get_domain_dns_records) | **get** /api/v1/domains/{fqdn}/dns-records | Получить информацию обо всех пользовательских DNS-записях домена или поддомена
*Api* | [**get_domain_name_servers**](docs/apis/tags/Api.md#get_domain_name_servers) | **get** /api/v1/domains/{fqdn}/name-servers | Получение списка name-серверов домена
*Api* | [**get_domain_request**](docs/apis/tags/Api.md#get_domain_request) | **get** /api/v1/domains-requests/{request_id} | Получение заявки на регистрацию/продление/трансфер домена
*Api* | [**get_domain_requests**](docs/apis/tags/Api.md#get_domain_requests) | **get** /api/v1/domains-requests | Получение списка заявок на регистрацию/продление/трансфер домена
*Api* | [**get_domains**](docs/apis/tags/Api.md#get_domains) | **get** /api/v1/domains | Получение списка всех доменов
*Api* | [**get_tld**](docs/apis/tags/Api.md#get_tld) | **get** /api/v1/tlds/{tld_id} | Получить информацию о доменной зоне по идентификатору
*Api* | [**get_tlds**](docs/apis/tags/Api.md#get_tlds) | **get** /api/v1/tlds | Получить информацию о доменных зонах
*Api* | [**update_domain_auto_prolongation**](docs/apis/tags/Api.md#update_domain_auto_prolongation) | **patch** /api/v1/domains/{fqdn} | Включение/выключение автопродления домена
*Api* | [**update_domain_dns_record**](docs/apis/tags/Api.md#update_domain_dns_record) | **patch** /api/v1/domains/{fqdn}/dns-records/{record_id} | Обновить информацию о DNS-записи домена или поддомена
*Api* | [**update_domain_name_servers**](docs/apis/tags/Api.md#update_domain_name_servers) | **put** /api/v1/domains/{fqdn}/name-servers | Изменение name-серверов домена
*Api* | [**update_domain_request**](docs/apis/tags/Api.md#update_domain_request) | **patch** /api/v1/domains-requests/{request_id} | Оплата/обновление заявки на регистрацию/продление/трансфер домена
*Api* | [**add_server_ip**](docs/apis/tags/Api.md#add_server_ip) | **post** /api/v1/servers/{server_id}/ips | Добавление IP-адреса сервера
*Api* | [**clone_server**](docs/apis/tags/Api.md#clone_server) | **post** /api/v1/servers/{server_id}/clone | Клонирование сервера
*Api* | [**create_server**](docs/apis/tags/Api.md#create_server) | **post** /api/v1/servers | Создание сервера
*Api* | [**create_server_disk**](docs/apis/tags/Api.md#create_server_disk) | **post** /api/v1/servers/{server_id}/disks | Создание диска сервера
*Api* | [**create_server_disk_backup**](docs/apis/tags/Api.md#create_server_disk_backup) | **post** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Создание бэкапа диска сервера
*Api* | [**delete_server**](docs/apis/tags/Api.md#delete_server) | **delete** /api/v1/servers/{server_id} | Удаление сервера
*Api* | [**delete_server_disk**](docs/apis/tags/Api.md#delete_server_disk) | **delete** /api/v1/servers/{server_id}/disks/{disk_id} | Удаление диска сервера
*Api* | [**delete_server_disk_backup**](docs/apis/tags/Api.md#delete_server_disk_backup) | **delete** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Удаление бэкапа диска сервера
*Api* | [**delete_server_ip**](docs/apis/tags/Api.md#delete_server_ip) | **delete** /api/v1/servers/{server_id}/ips | Удаление IP-адреса сервера
*Api* | [**get_configurators**](docs/apis/tags/Api.md#get_configurators) | **get** /api/v1/configurator/servers | Получение списка конфигураторов серверов
*Api* | [**get_os_list**](docs/apis/tags/Api.md#get_os_list) | **get** /api/v1/os/servers | Получение списка операционных систем
*Api* | [**get_server**](docs/apis/tags/Api.md#get_server) | **get** /api/v1/servers/{server_id} | Получение сервера
*Api* | [**get_server_disk**](docs/apis/tags/Api.md#get_server_disk) | **get** /api/v1/servers/{server_id}/disks/{disk_id} | Получение диска сервера
*Api* | [**get_server_disk_auto_backup_settings**](docs/apis/tags/Api.md#get_server_disk_auto_backup_settings) | **get** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Получить настройки автобэкапов диска сервера
*Api* | [**get_server_disk_backup**](docs/apis/tags/Api.md#get_server_disk_backup) | **get** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Получение бэкапа диска сервера
*Api* | [**get_server_disk_backups**](docs/apis/tags/Api.md#get_server_disk_backups) | **get** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Получение списка бэкапов диска сервера
*Api* | [**get_server_disks**](docs/apis/tags/Api.md#get_server_disks) | **get** /api/v1/servers/{server_id}/disks | Получение списка дисков сервера
*Api* | [**get_server_ips**](docs/apis/tags/Api.md#get_server_ips) | **get** /api/v1/servers/{server_id}/ips | Получение списка IP-адресов сервера
*Api* | [**get_server_logs**](docs/apis/tags/Api.md#get_server_logs) | **get** /api/v1/servers/{server_id}/logs | Получение списка логов сервера
*Api* | [**get_server_statistics**](docs/apis/tags/Api.md#get_server_statistics) | **get** /api/v1/servers/{server_id}/statistics | Получение статистики сервера
*Api* | [**get_servers**](docs/apis/tags/Api.md#get_servers) | **get** /api/v1/servers | Получение списка серверов
*Api* | [**get_servers_presets**](docs/apis/tags/Api.md#get_servers_presets) | **get** /api/v1/presets/servers | Получение списка тарифов серверов
*Api* | [**get_software**](docs/apis/tags/Api.md#get_software) | **get** /api/v1/software/servers | Получение списка ПО из маркетплейса
*Api* | [**image_unmount_and_server_reload**](docs/apis/tags/Api.md#image_unmount_and_server_reload) | **post** /api/v1/servers/{server_id}/image-unmount | Отмонтирование ISO образа и перезагрузка сервера
*Api* | [**perform_action_on_backup**](docs/apis/tags/Api.md#perform_action_on_backup) | **post** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action | Выполнение действия над бэкапом диска сервера
*Api* | [**perform_action_on_server**](docs/apis/tags/Api.md#perform_action_on_server) | **post** /api/v1/servers/{server_id}/action | Выполнение действия над сервером
*Api* | [**update_server**](docs/apis/tags/Api.md#update_server) | **patch** /api/v1/servers/{server_id} | Изменение сервера
*Api* | [**update_server_disk**](docs/apis/tags/Api.md#update_server_disk) | **patch** /api/v1/servers/{server_id}/disks/{disk_id} | Изменение параметров диска сервера
*Api* | [**update_server_disk_auto_backup_settings**](docs/apis/tags/Api.md#update_server_disk_auto_backup_settings) | **patch** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Изменение настроек автобэкапов диска сервера
*Api* | [**update_server_disk_backup**](docs/apis/tags/Api.md#update_server_disk_backup) | **patch** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Изменение бэкапа диска сервера
*Api* | [**update_server_ip**](docs/apis/tags/Api.md#update_server_ip) | **patch** /api/v1/servers/{server_id}/ips | Изменение IP-адреса сервера
*Api* | [**update_server_nat**](docs/apis/tags/Api.md#update_server_nat) | **patch** /api/v1/servers/{server_id}/local-networks/nat-mode | Изменение правил маршрутизации трафика сервера (NAT)
*Api* | [**update_server_os_boot_mode**](docs/apis/tags/Api.md#update_server_os_boot_mode) | **post** /api/v1/servers/{server_id}/boot-mode | Выбор типа загрузки операционной системы сервера
*Api* | [**create_image**](docs/apis/tags/Api.md#create_image) | **post** /api/v1/images | Создание образа
*Api* | [**create_image_download_url**](docs/apis/tags/Api.md#create_image_download_url) | **post** /api/v1/images/{image_id}/download-url | Создание ссылки на скачивание образа
*Api* | [**delete_image**](docs/apis/tags/Api.md#delete_image) | **delete** /api/v1/images/{image_id} | Удаление образа
*Api* | [**delete_image_download_url**](docs/apis/tags/Api.md#delete_image_download_url) | **delete** /api/v1/images/{image_id}/download-url/{image_url_id} | Удаление ссылки на образ
*Api* | [**get_image**](docs/apis/tags/Api.md#get_image) | **get** /api/v1/images/{image_id} | Получение информации о образе
*Api* | [**get_image_download_url**](docs/apis/tags/Api.md#get_image_download_url) | **get** /api/v1/images/{image_id}/download-url/{image_url_id} | Получение информации о ссылке на скачивание образа
*Api* | [**get_image_download_urls**](docs/apis/tags/Api.md#get_image_download_urls) | **get** /api/v1/images/{image_id}/download-url | Получение информации о ссылках на скачивание образов
*Api* | [**get_images**](docs/apis/tags/Api.md#get_images) | **get** /api/v1/images | Получение списка образов
*Api* | [**update_image**](docs/apis/tags/Api.md#update_image) | **patch** /api/v1/images/{image_id} | Обновление информации о образе
*Api* | [**upload_image**](docs/apis/tags/Api.md#upload_image) | **post** /api/v1/images/{image_id} | Загрузка образа
*Api* | [**create_domain_mailbox**](docs/apis/tags/Api.md#create_domain_mailbox) | **post** /api/v1/mail/domains/{domain} | Создание почтового ящика
*Api* | [**delete_mailbox**](docs/apis/tags/Api.md#delete_mailbox) | **delete** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Удаление почтового ящика
*Api* | [**get_domain_mail_info**](docs/apis/tags/Api.md#get_domain_mail_info) | **get** /api/v1/mail/domains/{domain}/info | Получение почтовой информации о домене
*Api* | [**get_domain_mailboxes**](docs/apis/tags/Api.md#get_domain_mailboxes) | **get** /api/v1/mail/domains/{domain} | Получение списка почтовых ящиков домена
*Api* | [**get_mail_quota**](docs/apis/tags/Api.md#get_mail_quota) | **get** /api/v1/mail/quota | Получение квоты почты аккаунта
*Api* | [**get_mailbox**](docs/apis/tags/Api.md#get_mailbox) | **get** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Получение почтового ящика
*Api* | [**get_mailboxes**](docs/apis/tags/Api.md#get_mailboxes) | **get** /api/v1/mail | Получение списка почтовых ящиков аккаунта
*Api* | [**update_domain_mail_info**](docs/apis/tags/Api.md#update_domain_mail_info) | **patch** /api/v1/mail/domains/{domain}/info | Изменение почтовой информации о домене
*Api* | [**update_mail_quota**](docs/apis/tags/Api.md#update_mail_quota) | **patch** /api/v1/mail/quota | Изменение квоты почты аккаунта
*Api* | [**update_mailbox**](docs/apis/tags/Api.md#update_mailbox) | **patch** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Изменение почтового ящика
*Api* | [**add_balancer_to_project**](docs/apis/tags/Api.md#add_balancer_to_project) | **post** /api/v1/projects/{project_id}/resources/balancers | Добавление балансировщика в проект
*Api* | [**add_cluster_to_project**](docs/apis/tags/Api.md#add_cluster_to_project) | **post** /api/v1/projects/{project_id}/resources/clusters | Добавление кластера в проект
*Api* | [**add_database_to_project**](docs/apis/tags/Api.md#add_database_to_project) | **post** /api/v1/projects/{project_id}/resources/databases | Добавление базы данных в проект
*Api* | [**add_dedicated_server_to_project**](docs/apis/tags/Api.md#add_dedicated_server_to_project) | **post** /api/v1/projects/{project_id}/resources/dedicated | Добавление выделенного сервера в проект
*Api* | [**add_server_to_project**](docs/apis/tags/Api.md#add_server_to_project) | **post** /api/v1/projects/{project_id}/resources/servers | Добавление сервера в проект
*Api* | [**add_storage_to_project**](docs/apis/tags/Api.md#add_storage_to_project) | **post** /api/v1/projects/{project_id}/resources/buckets | Добавление хранилища в проект
*Api* | [**create_project**](docs/apis/tags/Api.md#create_project) | **post** /api/v1/projects | Создание проекта
*Api* | [**delete_project**](docs/apis/tags/Api.md#delete_project) | **delete** /api/v1/projects/{project_id} | Удаление проекта
*Api* | [**get_account_balancers**](docs/apis/tags/Api.md#get_account_balancers) | **get** /api/v1/projects/resources/balancers | Получение списка всех балансировщиков на аккаунте
*Api* | [**get_account_clusters**](docs/apis/tags/Api.md#get_account_clusters) | **get** /api/v1/projects/resources/clusters | Получение списка всех кластеров на аккаунте
*Api* | [**get_account_databases**](docs/apis/tags/Api.md#get_account_databases) | **get** /api/v1/projects/resources/databases | Получение списка всех баз данных на аккаунте
*Api* | [**get_account_dedicated_servers**](docs/apis/tags/Api.md#get_account_dedicated_servers) | **get** /api/v1/projects/resources/dedicated | Получение списка всех выделенных серверов на аккаунте
*Api* | [**get_account_servers**](docs/apis/tags/Api.md#get_account_servers) | **get** /api/v1/projects/resources/servers | Получение списка всех серверов на аккаунте
*Api* | [**get_account_storages**](docs/apis/tags/Api.md#get_account_storages) | **get** /api/v1/projects/resources/buckets | Получение списка всех хранилищ на аккаунте
*Api* | [**get_all_project_resources**](docs/apis/tags/Api.md#get_all_project_resources) | **get** /api/v1/projects/{project_id}/resources | Получение всех ресурсов проекта
*Api* | [**get_project**](docs/apis/tags/Api.md#get_project) | **get** /api/v1/projects/{project_id} | Получение проекта по идентификатору
*Api* | [**get_project_balancers**](docs/apis/tags/Api.md#get_project_balancers) | **get** /api/v1/projects/{project_id}/resources/balancers | Получение списка балансировщиков проекта
*Api* | [**get_project_clusters**](docs/apis/tags/Api.md#get_project_clusters) | **get** /api/v1/projects/{project_id}/resources/clusters | Получение списка кластеров проекта
*Api* | [**get_project_databases**](docs/apis/tags/Api.md#get_project_databases) | **get** /api/v1/projects/{project_id}/resources/databases | Получение списка баз данных проекта
*Api* | [**get_project_dedicated_servers**](docs/apis/tags/Api.md#get_project_dedicated_servers) | **get** /api/v1/projects/{project_id}/resources/dedicated | Получение списка выделенных серверов проекта
*Api* | [**get_project_servers**](docs/apis/tags/Api.md#get_project_servers) | **get** /api/v1/projects/{project_id}/resources/servers | Получение списка серверов проекта
*Api* | [**get_project_storages**](docs/apis/tags/Api.md#get_project_storages) | **get** /api/v1/projects/{project_id}/resources/buckets | Получение списка хранилищ проекта
*Api* | [**get_projects**](docs/apis/tags/Api.md#get_projects) | **get** /api/v1/projects | Получение списка проектов
*Api* | [**transfer_resource_to_another_project**](docs/apis/tags/Api.md#transfer_resource_to_another_project) | **put** /api/v1/projects/{project_id}/resources/transfer | Перенести ресурс в другой проект
*Api* | [**update_project**](docs/apis/tags/Api.md#update_project) | **put** /api/v1/projects/{project_id} | Изменение проекта
*APIApi* | [**create_token**](docs/apis/tags/APIApi.md#create_token) | **post** /api/v1/auth/api-keys | Создание токена
*APIApi* | [**delete_token**](docs/apis/tags/APIApi.md#delete_token) | **delete** /api/v1/auth/api-keys/{token_id} | Удалить токен
*APIApi* | [**get_tokens**](docs/apis/tags/APIApi.md#get_tokens) | **get** /api/v1/auth/api-keys | Получение списка выпущенных токенов
*APIApi* | [**reissue_token**](docs/apis/tags/APIApi.md#reissue_token) | **put** /api/v1/auth/api-keys/{token_id} | Перевыпустить токен
*APIApi* | [**update_token**](docs/apis/tags/APIApi.md#update_token) | **patch** /api/v1/auth/api-keys/{token_id} | Изменить токен

## Documentation For Models

 - [AddCountries](docs/models/AddCountries.md)
 - [AddIps](docs/models/AddIps.md)
 - [AddedSubdomain](docs/models/AddedSubdomain.md)
 - [ApiKey](docs/models/ApiKey.md)
 - [AutoBackup](docs/models/AutoBackup.md)
 - [AutoReplyIsDisabled](docs/models/AutoReplyIsDisabled.md)
 - [AutoReplyIsEnabled](docs/models/AutoReplyIsEnabled.md)
 - [Backup](docs/models/Backup.md)
 - [Balancer](docs/models/Balancer.md)
 - [BaseError](docs/models/BaseError.md)
 - [Bonus](docs/models/Bonus.md)
 - [Bucket](docs/models/Bucket.md)
 - [BucketUser](docs/models/BucketUser.md)
 - [ClusterEdit](docs/models/ClusterEdit.md)
 - [ClusterIn](docs/models/ClusterIn.md)
 - [ClusterOut](docs/models/ClusterOut.md)
 - [ClusterResponse](docs/models/ClusterResponse.md)
 - [Clusterk8s](docs/models/Clusterk8s.md)
 - [ClustersResponse](docs/models/ClustersResponse.md)
 - [ConfigParameters](docs/models/ConfigParameters.md)
 - [CreateAdmin](docs/models/CreateAdmin.md)
 - [CreateApiKey](docs/models/CreateApiKey.md)
 - [CreateBalancer](docs/models/CreateBalancer.md)
 - [CreateCluster](docs/models/CreateCluster.md)
 - [CreateDb](docs/models/CreateDb.md)
 - [CreateDedicatedServer](docs/models/CreateDedicatedServer.md)
 - [CreateDns](docs/models/CreateDns.md)
 - [CreateInstance](docs/models/CreateInstance.md)
 - [CreateProject](docs/models/CreateProject.md)
 - [CreateRule](docs/models/CreateRule.md)
 - [CreateServer](docs/models/CreateServer.md)
 - [CreateVpc](docs/models/CreateVpc.md)
 - [CreatedApiKey](docs/models/CreatedApiKey.md)
 - [DatabaseAdmin](docs/models/DatabaseAdmin.md)
 - [DatabaseCluster](docs/models/DatabaseCluster.md)
 - [DatabaseInstance](docs/models/DatabaseInstance.md)
 - [Db](docs/models/Db.md)
 - [DedicatedServer](docs/models/DedicatedServer.md)
 - [DedicatedServerAdditionalService](docs/models/DedicatedServerAdditionalService.md)
 - [DedicatedServerPreset](docs/models/DedicatedServerPreset.md)
 - [DeleteServiceResponse](docs/models/DeleteServiceResponse.md)
 - [DnsRecord](docs/models/DnsRecord.md)
 - [Domain](docs/models/Domain.md)
 - [DomainInfo](docs/models/DomainInfo.md)
 - [DomainNameServer](docs/models/DomainNameServer.md)
 - [DomainPaymentPeriod](docs/models/DomainPaymentPeriod.md)
 - [DomainPrimeType](docs/models/DomainPrimeType.md)
 - [DomainProlong](docs/models/DomainProlong.md)
 - [DomainRegister](docs/models/DomainRegister.md)
 - [DomainRequest](docs/models/DomainRequest.md)
 - [DomainTransfer](docs/models/DomainTransfer.md)
 - [EditApiKey](docs/models/EditApiKey.md)
 - [Finances](docs/models/Finances.md)
 - [FirewallGroupInAPI](docs/models/FirewallGroupInAPI.md)
 - [FirewallGroupOutAPI](docs/models/FirewallGroupOutAPI.md)
 - [FirewallGroupOutResponse](docs/models/FirewallGroupOutResponse.md)
 - [FirewallGroupResourceOutAPI](docs/models/FirewallGroupResourceOutAPI.md)
 - [FirewallGroupResourceOutResponse](docs/models/FirewallGroupResourceOutResponse.md)
 - [FirewallGroupResourcesOutResponse](docs/models/FirewallGroupResourcesOutResponse.md)
 - [FirewallGroupsOutResponse](docs/models/FirewallGroupsOutResponse.md)
 - [FirewallRuleDirection](docs/models/FirewallRuleDirection.md)
 - [FirewallRuleInAPI](docs/models/FirewallRuleInAPI.md)
 - [FirewallRuleOutAPI](docs/models/FirewallRuleOutAPI.md)
 - [FirewallRuleOutResponse](docs/models/FirewallRuleOutResponse.md)
 - [FirewallRuleProtocol](docs/models/FirewallRuleProtocol.md)
 - [FirewallRulesOutResponse](docs/models/FirewallRulesOutResponse.md)
 - [ForwardingIncomingIsDisabled](docs/models/ForwardingIncomingIsDisabled.md)
 - [ForwardingIncomingIsEnabled](docs/models/ForwardingIncomingIsEnabled.md)
 - [ForwardingOutgoingIsDisabled](docs/models/ForwardingOutgoingIsDisabled.md)
 - [ForwardingOutgoingIsEnabled](docs/models/ForwardingOutgoingIsEnabled.md)
 - [Free](docs/models/Free.md)
 - [ImageDownloadAPI](docs/models/ImageDownloadAPI.md)
 - [ImageDownloadResponse](docs/models/ImageDownloadResponse.md)
 - [ImageDownloadsResponse](docs/models/ImageDownloadsResponse.md)
 - [ImageInAPI](docs/models/ImageInAPI.md)
 - [ImageOutAPI](docs/models/ImageOutAPI.md)
 - [ImageOutResponse](docs/models/ImageOutResponse.md)
 - [ImageStatus](docs/models/ImageStatus.md)
 - [ImageUpdateAPI](docs/models/ImageUpdateAPI.md)
 - [ImageUrlAuth](docs/models/ImageUrlAuth.md)
 - [ImageUrlIn](docs/models/ImageUrlIn.md)
 - [ImagesOutResponse](docs/models/ImagesOutResponse.md)
 - [Invoice](docs/models/Invoice.md)
 - [K8SVersionsResponse](docs/models/K8SVersionsResponse.md)
 - [Location](docs/models/Location.md)
 - [Mailbox](docs/models/Mailbox.md)
 - [MasterPresetOutApi](docs/models/MasterPresetOutApi.md)
 - [Meta](docs/models/Meta.md)
 - [Network](docs/models/Network.md)
 - [NetworkDriversResponse](docs/models/NetworkDriversResponse.md)
 - [NodeCount](docs/models/NodeCount.md)
 - [NodeGroupIn](docs/models/NodeGroupIn.md)
 - [NodeGroupOut](docs/models/NodeGroupOut.md)
 - [NodeGroupResponse](docs/models/NodeGroupResponse.md)
 - [NodeGroupsResponse](docs/models/NodeGroupsResponse.md)
 - [NodeOut](docs/models/NodeOut.md)
 - [NodesResponse](docs/models/NodesResponse.md)
 - [NotificationSetting](docs/models/NotificationSetting.md)
 - [NotificationSettingChannel](docs/models/NotificationSettingChannel.md)
 - [NotificationSettingType](docs/models/NotificationSettingType.md)
 - [OS](docs/models/OS.md)
 - [PresetsBalancer](docs/models/PresetsBalancer.md)
 - [PresetsDbs](docs/models/PresetsDbs.md)
 - [PresetsResponse](docs/models/PresetsResponse.md)
 - [PresetsStorage](docs/models/PresetsStorage.md)
 - [Project](docs/models/Project.md)
 - [ProjectResource](docs/models/ProjectResource.md)
 - [Quota](docs/models/Quota.md)
 - [RefreshApiKey](docs/models/RefreshApiKey.md)
 - [RemoveCountries](docs/models/RemoveCountries.md)
 - [RemoveIps](docs/models/RemoveIps.md)
 - [Resource](docs/models/Resource.md)
 - [ResourceTransfer](docs/models/ResourceTransfer.md)
 - [ResourceType](docs/models/ResourceType.md)
 - [Resources](docs/models/Resources.md)
 - [ResourcesResponse](docs/models/ResourcesResponse.md)
 - [ResponseId](docs/models/ResponseId.md)
 - [ResponseIdResponseId](docs/models/ResponseIdResponseId.md)
 - [Rule](docs/models/Rule.md)
 - [S3Object](docs/models/S3Object.md)
 - [S3Subdomain](docs/models/S3Subdomain.md)
 - [SchemasBaseError](docs/models/SchemasBaseError.md)
 - [ServerBackup](docs/models/ServerBackup.md)
 - [ServerDisk](docs/models/ServerDisk.md)
 - [ServerIp](docs/models/ServerIp.md)
 - [ServerLog](docs/models/ServerLog.md)
 - [ServersConfigurator](docs/models/ServersConfigurator.md)
 - [ServersOs](docs/models/ServersOs.md)
 - [ServersPreset](docs/models/ServersPreset.md)
 - [ServersSoftware](docs/models/ServersSoftware.md)
 - [SettingCondition](docs/models/SettingCondition.md)
 - [SpamFilterIsDisabled](docs/models/SpamFilterIsDisabled.md)
 - [SpamFilterIsEnabled](docs/models/SpamFilterIsEnabled.md)
 - [SshKey](docs/models/SshKey.md)
 - [Status](docs/models/Status.md)
 - [Subdomain](docs/models/Subdomain.md)
 - [TopLevelDomain](docs/models/TopLevelDomain.md)
 - [TransferStatus](docs/models/TransferStatus.md)
 - [URLType](docs/models/URLType.md)
 - [UpdateAdmin](docs/models/UpdateAdmin.md)
 - [UpdateBalancer](docs/models/UpdateBalancer.md)
 - [UpdateCluster](docs/models/UpdateCluster.md)
 - [UpdateDb](docs/models/UpdateDb.md)
 - [UpdateDomain](docs/models/UpdateDomain.md)
 - [UpdateDomainNameServers](docs/models/UpdateDomainNameServers.md)
 - [UpdateInstance](docs/models/UpdateInstance.md)
 - [UpdateMailbox](docs/models/UpdateMailbox.md)
 - [UpdateProject](docs/models/UpdateProject.md)
 - [UpdateRule](docs/models/UpdateRule.md)
 - [UpdateServer](docs/models/UpdateServer.md)
 - [UpdateVpc](docs/models/UpdateVpc.md)
 - [UploadSuccessful](docs/models/UploadSuccessful.md)
 - [UploadSuccessfulResponse](docs/models/UploadSuccessfulResponse.md)
 - [UrlStatus](docs/models/UrlStatus.md)
 - [Use](docs/models/Use.md)
 - [Vds](docs/models/Vds.md)
 - [Vpc](docs/models/Vpc.md)
 - [VpcPort](docs/models/VpcPort.md)
 - [VpcService](docs/models/VpcService.md)
 - [WorkerPresetOutApi](docs/models/WorkerPresetOutApi.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: Bearer authentication (JWT)


## Author

info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud
info@timeweb.cloud

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
