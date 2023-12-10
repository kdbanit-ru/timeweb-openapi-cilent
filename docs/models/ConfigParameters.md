# openapi_client.model.config_parameters.ConfigParameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**auto_increment_increment** | str,  | str,  | Интервал между значениями столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**auto_increment_offset** | str,  | str,  | Начальное значение для столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_io_capacity** | str,  | str,  | Количество операций ввода-вывода в секунду &#x60;IOPS&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_purge_threads** | str,  | str,  | Количество потоков ввода-вывода, используемых для операций очистки (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_read_io_threads** | str,  | str,  | Количество потоков ввода-вывода, используемых для операций чтения (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_thread_concurrency** | str,  | str,  | Максимальное число потоков, которые могут исполняться (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_write_io_threads** | str,  | str,  | Количество потоков ввода-вывода, используемых для операций записи (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**join_buffer_size** | str,  | str,  | Минимальный размер буфера (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**max_allowed_packet** | str,  | str,  | Максимальный размер одного пакета, строки или параметра, отправляемого функцией &#x60;mysql_stmt_send_long_data()&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**max_heap_table_size** | str,  | str,  | Максимальный размер пользовательских MEMORY-таблиц (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**autovacuum_analyze_scale_factor** | str,  | str,  | Доля измененных или удаленных записей в таблице, при которой процесс автоочистки выполнит команду &#x60;ANALYZE&#x60; (&#x60;postgres&#x60;). | [optional] 
**bgwriter_delay** | str,  | str,  | Задержка между запусками процесса фоновой записи (&#x60;postgres&#x60;). | [optional] 
**bgwriter_lru_maxpages** | str,  | str,  | Максимальное число элементов буферного кеша (&#x60;postgres&#x60;). | [optional] 
**deadlock_timeout** | str,  | str,  | Время ожидания, по истечении которого будет выполняться проверка состояния перекрестной блокировки (&#x60;postgres&#x60;). | [optional] 
**gin_pending_list_limit** | str,  | str,  | Максимальный размер очереди записей индекса &#x60;GIN&#x60; (&#x60;postgres&#x60;). | [optional] 
**idle_in_transaction_session_timeout** | str,  | str,  | Время простоя открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (&#x60;postgres&#x60;). | [optional] 
**idle_session_timeout** | str,  | str,  | Время простоя не открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (&#x60;postgres&#x60;). | [optional] 
**join_collapse_limit** | str,  | str,  | Значение количества элементов в списке &#x60;FROM&#x60; при превышении которого, планировщик будет переносить в список явные инструкции &#x60;JOIN&#x60; (&#x60;postgres&#x60;). | [optional] 
**lock_timeout** | str,  | str,  | Время ожидания освобождения блокировки (&#x60;postgres&#x60;). | [optional] 
**max_prepared_transactions** | str,  | str,  | Максимальное число транзакций, которые могут одновременно находиться в подготовленном состоянии (&#x60;postgres&#x60;). | [optional] 
**max_connections** | str,  | str,  | Допустимое количество соединений (&#x60;postgres&#x60; | &#x60;mysql&#x60;). | [optional] 
**shared_buffers** | str,  | str,  | Устанавливает количество буферов общей памяти, используемых сервером (&#x60;postgres&#x60;). | [optional] 
**wal_buffers** | str,  | str,  | Устанавливает количество буферов дисковых страниц в общей памяти для WAL (&#x60;postgres&#x60;). | [optional] 
**temp_buffers** | str,  | str,  | Устанавливает максимальное количество временных буферов, используемых каждой сессией (&#x60;postgres&#x60;). | [optional] 
**work_mem** | str,  | str,  | Устанавливает максимальное количество памяти, используемое для рабочих пространств запросов (&#x60;postgres&#x60;). | [optional] 
**sql_mode** | str,  | str,  | Устанавливает режим SQL. Можно задать несколько режимов, разделяя их запятой. (&#x60;mysql&#x60;). | [optional] 
**query_cache_type** | str,  | str,  | Параметр включает или отключает работу MySQL Query Cache (&#x60;mysql&#x60;). | [optional] 
**query_cache_size** | str,  | str,  | Размер в байтах, доступный для кэша запросов (&#x60;mysql&#x60;). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

