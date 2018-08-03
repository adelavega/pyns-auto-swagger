# swagger_client.PredictorsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_predictor_events_get**](PredictorsApi.md#api_predictor_events_get) | **GET** /api/predictor-events | Get events for predictor(s)
[**api_predictors_get**](PredictorsApi.md#api_predictors_get) | **GET** /api/predictors | Get list of predictors.
[**api_predictors_predictor_id_get**](PredictorsApi.md#api_predictors_predictor_id_get) | **GET** /api/predictors/{predictor_id} | Get predictor by id.


# **api_predictor_events_get**
> list[InlineResponseDefault7] api_predictor_events_get(predictor_id=predictor_id, run_id=run_id)

Get events for predictor(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PredictorsApi()
predictor_id = 'predictor_id_example' # str | Predictor id(s) (optional)
run_id = 'run_id_example' # str | Run id(s) (optional)

try:
    # Get events for predictor(s)
    api_response = api_instance.api_predictor_events_get(predictor_id=predictor_id, run_id=run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorsApi->api_predictor_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predictor_id** | **str**| Predictor id(s) | [optional] 
 **run_id** | **str**| Run id(s) | [optional] 

### Return type

[**list[InlineResponseDefault7]**](InlineResponseDefault7.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_predictors_get**
> list[InlineResponseDefault8] api_predictors_get(dataset_id=dataset_id, run_id=run_id, name=name, newest=newest)

Get list of predictors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PredictorsApi()
dataset_id = 'dataset_id_example' # str | Dataset id(s). If set, ignores run ids (optional)
run_id = 'run_id_example' # str | Run id(s). Warning, slow query. (optional)
name = 'name_example' # str | Predictor name(s) (optional)
newest = true # bool | Return only newest Predictor by name (optional) (default to true)

try:
    # Get list of predictors.
    api_response = api_instance.api_predictors_get(dataset_id=dataset_id, run_id=run_id, name=name, newest=newest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorsApi->api_predictors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| Dataset id(s). If set, ignores run ids | [optional] 
 **run_id** | **str**| Run id(s). Warning, slow query. | [optional] 
 **name** | **str**| Predictor name(s) | [optional] 
 **newest** | **bool**| Return only newest Predictor by name | [optional] [default to true]

### Return type

[**list[InlineResponseDefault8]**](InlineResponseDefault8.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_predictors_predictor_id_get**
> InlineResponseDefault9 api_predictors_predictor_id_get(predictor_id)

Get predictor by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PredictorsApi()
predictor_id = 56 # int | 

try:
    # Get predictor by id.
    api_response = api_instance.api_predictors_predictor_id_get(predictor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorsApi->api_predictors_predictor_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predictor_id** | **int**|  | 

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

