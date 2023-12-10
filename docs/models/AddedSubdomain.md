# openapi_client.model.added_subdomain.AddedSubdomain

Добавленный поддомен.

## Model Type Info
| Input Type                   | Accessed Type          | Description           | Notes |
|------------------------------|------------------------|-----------------------|-------|
| dict, frozendict.frozendict, | frozendict.frozendict, | Добавленный поддомен. |       |

### Dictionary Keys
| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                              |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| **subdomain**       | str,                                                                                                                                        | str,                                                                                    | Поддомен.                                                          |                                                                    |
| **status**          | str,                                                                                                                                        | str,                                                                                    | Результат добавления поддомена.                                    | must be one of ["success", "empty_cname", "duplicate", "failed", ] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                         |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

