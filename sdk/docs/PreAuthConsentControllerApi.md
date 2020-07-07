# yapily.PreAuthConsentControllerApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pre_authorisation_using_post**](PreAuthConsentControllerApi.md#create_pre_authorisation_using_post) | **POST** /pre-auth-requests | Initiate request for user to pre authorise


# **create_pre_authorisation_using_post**
> ApiResponseOfAuthorisationRequestResponse create_pre_authorisation_using_post(pre_authorisation_request)

Initiate request for user to pre authorise

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
    api_instance = yapily.PreAuthConsentControllerApi(api_client)
    pre_authorisation_request = yapily.PreAuthorisationRequest() # PreAuthorisationRequest | preAuthorisationRequest

    try:
        # Initiate request for user to pre authorise
        api_response = api_instance.create_pre_authorisation_using_post(pre_authorisation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreAuthConsentControllerApi->create_pre_authorisation_using_post: %s\n" % e)
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
    api_instance = yapily.PreAuthConsentControllerApi(api_client)
    pre_authorisation_request = yapily.PreAuthorisationRequest() # PreAuthorisationRequest | preAuthorisationRequest

    try:
        # Initiate request for user to pre authorise
        api_response = api_instance.create_pre_authorisation_using_post(pre_authorisation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreAuthConsentControllerApi->create_pre_authorisation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_authorisation_request** | [**PreAuthorisationRequest**](PreAuthorisationRequest.md)| preAuthorisationRequest | 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

