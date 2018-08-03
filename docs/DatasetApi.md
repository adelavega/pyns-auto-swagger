# swagger_client.DatasetApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_datasets_dataset_id_get**](DatasetApi.md#api_datasets_dataset_id_get) | **GET** /api/datasets/{dataset_id} | Get dataset by id.
[**api_datasets_get**](DatasetApi.md#api_datasets_get) | **GET** /api/datasets | Returns list of datasets.


# **api_datasets_dataset_id_get**
> InlineResponseDefault6 api_datasets_dataset_id_get(dataset_id)

Get dataset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
dataset_id = 56 # int | 

try:
    # Get dataset by id.
    api_response = api_instance.api_datasets_dataset_id_get(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->api_datasets_dataset_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **int**|  | 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_datasets_get**
> list[InlineResponseDefault5] api_datasets_get()

Returns list of datasets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()

try:
    # Returns list of datasets.
    api_response = api_instance.api_datasets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->api_datasets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponseDefault5]**](InlineResponseDefault5.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

