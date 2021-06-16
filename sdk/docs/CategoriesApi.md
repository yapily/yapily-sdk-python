# yapily.CategoriesApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_using_get**](CategoriesApi.md#get_categories_using_get) | **GET** /categories/{country} | Retrieves a list of categories returned by the Yapily Categorisation engine for a given locale


# **get_categories_using_get**
> ApiListResponseOfCategory get_categories_using_get(country, x_yapily_api_version=x_yapily_api_version)

Retrieves a list of categories returned by the Yapily Categorisation engine for a given locale

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
    api_instance = yapily.CategoriesApi(api_client)
    country = 'country_example' # str | __Mandatory__. The 2 letter country code e.g. 'GB'.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Retrieves a list of categories returned by the Yapily Categorisation engine for a given locale
        api_response = api_instance.get_categories_using_get(country, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->get_categories_using_get: %s\n" % e)
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
    api_instance = yapily.CategoriesApi(api_client)
    country = 'country_example' # str | __Mandatory__. The 2 letter country code e.g. 'GB'.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Retrieves a list of categories returned by the Yapily Categorisation engine for a given locale
        api_response = api_instance.get_categories_using_get(country, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->get_categories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| __Mandatory__. The 2 letter country code e.g. &#39;GB&#39;. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

[**ApiListResponseOfCategory**](ApiListResponseOfCategory.md)

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

