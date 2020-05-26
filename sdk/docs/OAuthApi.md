# yapily.OAuthApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token**](OAuthApi.md#oauth_token) | **POST** /oauth/token | Retrieve Access Token


# **oauth_token**
> YapilyAccessToken oauth_token(grant_type)

Retrieve Access Token

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.OAuthApi(api_client)
    grant_type = 'client_credentials' # str | Grant type (default to 'client_credentials')

    try:
        # Retrieve Access Token
        api_response = api_instance.oauth_token(grant_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OAuthApi->oauth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Grant type | [default to &#39;client_credentials&#39;]

### Return type

[**YapilyAccessToken**](YapilyAccessToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

