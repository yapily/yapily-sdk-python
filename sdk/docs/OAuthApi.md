# yapily.OAuthApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token**](OAuthApi.md#oauth_token) | **POST** /oauth/token | Retrieve Access Token


# **oauth_token**
> YapilyAccessToken oauth_token(grant_type)

Retrieve Access Token

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = yapily.OAuthApi(yapily.ApiClient(configuration))
grant_type = 'client_credentials' # str | Grant type (default to client_credentials)

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
 **grant_type** | **str**| Grant type | [default to client_credentials]

### Return type

[**YapilyAccessToken**](YapilyAccessToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

