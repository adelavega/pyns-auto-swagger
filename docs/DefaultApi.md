# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_user_get**](DefaultApi.md#api_user_get) | **GET** /api/user | Get current user information.
[**api_user_post**](DefaultApi.md#api_user_post) | **POST** /api/user | Add a new user.
[**api_user_put**](DefaultApi.md#api_user_put) | **PUT** /api/user | Edit user information.
[**api_user_resend_confirmation_post**](DefaultApi.md#api_user_resend_confirmation_post) | **POST** /api/user/resend_confirmation | Resend confirmation email.
[**api_user_reset_password_post**](DefaultApi.md#api_user_reset_password_post) | **POST** /api/user/reset_password | 
[**api_user_submit_token_post**](DefaultApi.md#api_user_submit_token_post) | **POST** /api/user/submit_token | 


# **api_user_get**
> InlineResponseDefault12 api_user_get(authorization)

Get current user information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}

try:
    # Get current user information.
    api_response = api_instance.api_user_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Format:  JWT {authorization_token} | 

### Return type

[**InlineResponseDefault12**](InlineResponseDefault12.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_post**
> InlineResponseDefault12 api_user_post(body=body)

Add a new user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Body4() # Body4 |  (optional)

try:
    # Add a new user.
    api_response = api_instance.api_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**InlineResponseDefault12**](InlineResponseDefault12.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_put**
> InlineResponseDefault12 api_user_put(authorization, body=body)

Edit user information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}
body = swagger_client.Body3() # Body3 |  (optional)

try:
    # Edit user information.
    api_response = api_instance.api_user_put(authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Format:  JWT {authorization_token} | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**InlineResponseDefault12**](InlineResponseDefault12.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_resend_confirmation_post**
> api_user_resend_confirmation_post(authorization)

Resend confirmation email.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | Format:  JWT {authorization_token}

try:
    # Resend confirmation email.
    api_instance.api_user_resend_confirmation_post(authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_resend_confirmation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Format:  JWT {authorization_token} | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_reset_password_post**
> api_user_reset_password_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Body5() # Body5 |  (optional)

try:
    api_instance.api_user_reset_password_post(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_reset_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_submit_token_post**
> api_user_submit_token_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Body6() # Body6 |  (optional)

try:
    api_instance.api_user_submit_token_post(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->api_user_submit_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

