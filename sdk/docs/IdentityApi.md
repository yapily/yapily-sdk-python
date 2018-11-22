# yapily.IdentityApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_identity_using_get**](IdentityApi.md#get_identity_using_get) | **GET** /identity | Get identity


# **get_identity_using_get**
> ApiResponseOfIdentity get_identity_using_get(consent)

Get identity

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
api_instance = yapily.IdentityApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token

try:
    # Get identity
    api_response = api_instance.get_identity_using_get(consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 

### Return type

[**ApiResponseOfIdentity**](ApiResponseOfIdentity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

