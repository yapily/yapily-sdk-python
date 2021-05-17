# yapily.ApplicationsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_me_using_get**](ApplicationsApi.md#get_application_me_using_get) | **GET** /me | Returns the details of the application that owns the request credentials


# **get_application_me_using_get**
> Application get_application_me_using_get(x_yapily_api_version=x_yapily_api_version)

Returns the details of the application that owns the request credentials

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint
configuration = yapily.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = yapily.Configuration()
# Configure OAuth2 access token for authorization: tokenAuth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.yapily.com:443
configuration.host = "https://api.yapily.com:443"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.ApplicationsApi(api_client)
    x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)

    try:
        # Returns the details of the application that owns the request credentials
        api_response = api_instance.get_application_me_using_get(x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_me_using_get: %s\n" % e)
```

* OAuth Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint
configuration = yapily.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = yapily.Configuration()
# Configure OAuth2 access token for authorization: tokenAuth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.yapily.com:443
configuration.host = "https://api.yapily.com:443"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.ApplicationsApi(api_client)
    x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)

    try:
        # Returns the details of the application that owns the request credentials
        api_response = api_instance.get_application_me_using_get(x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_me_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_yapily_api_version** | **str**| Api Version | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

