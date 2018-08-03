# swagger_client.RunApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_runs_get**](RunApi.md#api_runs_get) | **GET** /api/runs | Returns list of runs.
[**api_runs_run_id_get**](RunApi.md#api_runs_run_id_get) | **GET** /api/runs/{run_id} | Get run by id.
[**api_tasks_get**](RunApi.md#api_tasks_get) | **GET** /api/tasks | Returns list of tasks.
[**api_tasks_task_id_get**](RunApi.md#api_tasks_task_id_get) | **GET** /api/tasks/{task_id} | Get task by id.


# **api_runs_get**
> list[InlineResponseDefault10] api_runs_get(session=session, task_id=task_id, number=number, subject=subject, dataset_id=dataset_id)

Returns list of runs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
session = 'session_example' # str | Session number(s). (optional)
task_id = 'task_id_example' # str | Task id(s). (optional)
number = 'number_example' # str | Run number(s). (optional)
subject = 'subject_example' # str | Subject id(s). (optional)
dataset_id = 56 # int | Dataset id. (optional)

try:
    # Returns list of runs.
    api_response = api_instance.api_runs_get(session=session, task_id=task_id, number=number, subject=subject, dataset_id=dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->api_runs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| Session number(s). | [optional] 
 **task_id** | **str**| Task id(s). | [optional] 
 **number** | **str**| Run number(s). | [optional] 
 **subject** | **str**| Subject id(s). | [optional] 
 **dataset_id** | **int**| Dataset id. | [optional] 

### Return type

[**list[InlineResponseDefault10]**](InlineResponseDefault10.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_runs_run_id_get**
> InlineResponseDefault10 api_runs_run_id_get(run_id)

Get run by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
run_id = 56 # int | 

try:
    # Get run by id.
    api_response = api_instance.api_runs_run_id_get(run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->api_runs_run_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_get**
> list[InlineResponseDefault11] api_tasks_get(dataset_id=dataset_id)

Returns list of tasks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
dataset_id = 56 # int | Dataset id(s). (optional)

try:
    # Returns list of tasks.
    api_response = api_instance.api_tasks_get(dataset_id=dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->api_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **int**| Dataset id(s). | [optional] 

### Return type

[**list[InlineResponseDefault11]**](InlineResponseDefault11.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_task_id_get**
> InlineResponseDefault11 api_tasks_task_id_get(task_id)

Get task by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
task_id = 56 # int | 

try:
    # Get task by id.
    api_response = api_instance.api_tasks_task_id_get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->api_tasks_task_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 

### Return type

[**InlineResponseDefault11**](InlineResponseDefault11.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

