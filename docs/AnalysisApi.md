# swagger_client.AnalysisApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_analyses_analysis_id_bundle_get**](AnalysisApi.md#api_analyses_analysis_id_bundle_get) | **GET** /api/analyses/{analysis_id}/bundle | Get analysis tarball bundle.
[**api_analyses_analysis_id_clone_post**](AnalysisApi.md#api_analyses_analysis_id_clone_post) | **POST** /api/analyses/{analysis_id}/clone | Clone analysis.
[**api_analyses_analysis_id_compile_post**](AnalysisApi.md#api_analyses_analysis_id_compile_post) | **POST** /api/analyses/{analysis_id}/compile | Compile and lock analysis.
[**api_analyses_analysis_id_delete**](AnalysisApi.md#api_analyses_analysis_id_delete) | **DELETE** /api/analyses/{analysis_id} | Delete analysis.
[**api_analyses_analysis_id_full_get**](AnalysisApi.md#api_analyses_analysis_id_full_get) | **GET** /api/analyses/{analysis_id}/full | Get analysis (including nested fields).
[**api_analyses_analysis_id_get**](AnalysisApi.md#api_analyses_analysis_id_get) | **GET** /api/analyses/{analysis_id} | Get analysis by id.
[**api_analyses_analysis_id_put**](AnalysisApi.md#api_analyses_analysis_id_put) | **PUT** /api/analyses/{analysis_id} | Edit analysis.
[**api_analyses_analysis_id_resources_get**](AnalysisApi.md#api_analyses_analysis_id_resources_get) | **GET** /api/analyses/{analysis_id}/resources | Get analysis resources.
[**api_analyses_analysis_id_status_get**](AnalysisApi.md#api_analyses_analysis_id_status_get) | **GET** /api/analyses/{analysis_id}/status | Check if analysis has compiled.
[**api_analyses_get**](AnalysisApi.md#api_analyses_get) | **GET** /api/analyses | Returns list of public analyses.
[**api_analyses_post**](AnalysisApi.md#api_analyses_post) | **POST** /api/analyses | Add new analysis!


# **api_analyses_analysis_id_bundle_get**
> api_analyses_analysis_id_bundle_get(analysis_id)

Get analysis tarball bundle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Get analysis tarball bundle.
    api_instance.api_analyses_analysis_id_bundle_get(analysis_id)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_bundle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_clone_post**
> InlineResponseDefault api_analyses_analysis_id_clone_post(analysis_id, authorization)

Clone analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}

try:
    # Clone analysis.
    api_response = api_instance.api_analyses_analysis_id_clone_post(analysis_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **authorization** | **str**| Format:  JWT {authorization_token} | 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_compile_post**
> InlineResponseDefault api_analyses_analysis_id_compile_post(analysis_id, authorization)

Compile and lock analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}

try:
    # Compile and lock analysis.
    api_response = api_instance.api_analyses_analysis_id_compile_post(analysis_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_compile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **authorization** | **str**| Format:  JWT {authorization_token} | 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_delete**
> InlineResponseDefault api_analyses_analysis_id_delete(analysis_id, authorization)

Delete analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}

try:
    # Delete analysis.
    api_response = api_instance.api_analyses_analysis_id_delete(analysis_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **authorization** | **str**| Format:  JWT {authorization_token} | 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_full_get**
> InlineResponseDefault1 api_analyses_analysis_id_full_get(analysis_id)

Get analysis (including nested fields).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Get analysis (including nested fields).
    api_response = api_instance.api_analyses_analysis_id_full_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_full_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_get**
> InlineResponseDefault api_analyses_analysis_id_get(analysis_id)

Get analysis by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Get analysis by id.
    api_response = api_instance.api_analyses_analysis_id_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_put**
> InlineResponseDefault api_analyses_analysis_id_put(analysis_id, authorization, body=body)

Edit analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Edit analysis.
    api_response = api_instance.api_analyses_analysis_id_put(analysis_id, authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **authorization** | **str**| Format:  JWT {authorization_token} | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_resources_get**
> InlineResponseDefault2 api_analyses_analysis_id_resources_get(analysis_id)

Get analysis resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Get analysis resources.
    api_response = api_instance.api_analyses_analysis_id_resources_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 

### Return type

[**InlineResponseDefault2**](InlineResponseDefault2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_analysis_id_status_get**
> InlineResponseDefault3 api_analyses_analysis_id_status_get(analysis_id)

Check if analysis has compiled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Check if analysis has compiled.
    api_response = api_instance.api_analyses_analysis_id_status_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_get**
> list[InlineResponseDefault] api_analyses_get()

Returns list of public analyses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    # Returns list of public analyses.
    api_response = api_instance.api_analyses_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponseDefault]**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_analyses_post**
> InlineResponseDefault api_analyses_post(authorization, body=body)

Add new analysis!

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}
body = swagger_client.Body() # Body |  (optional)

try:
    # Add new analysis!
    api_response = api_instance.api_analyses_post(authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Format:  JWT {authorization_token} | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

