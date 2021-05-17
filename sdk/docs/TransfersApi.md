# yapily.TransfersApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_using_put**](TransfersApi.md#transfer_using_put) | **PUT** /accounts/{accountId}/transfer | Transfer money from one account to another account accessible with the same consent


# **transfer_using_put**
> ApiResponseOfTransferResponse transfer_using_put(consent, account_id, x_yapily_api_version=x_yapily_api_version, transfer_request=transfer_request)

Transfer money from one account to another account accessible with the same consent

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
    api_instance = yapily.TransfersApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
transfer_request = yapily.TransferRequest() # TransferRequest | transferRequest (optional)

    try:
        # Transfer money from one account to another account accessible with the same consent
        api_response = api_instance.transfer_using_put(consent, account_id, x_yapily_api_version=x_yapily_api_version, transfer_request=transfer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->transfer_using_put: %s\n" % e)
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
    api_instance = yapily.TransfersApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
transfer_request = yapily.TransferRequest() # TransferRequest | transferRequest (optional)

    try:
        # Transfer money from one account to another account accessible with the same consent
        api_response = api_instance.transfer_using_put(consent, account_id, x_yapily_api_version=x_yapily_api_version, transfer_request=transfer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransfersApi->transfer_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| Account Id | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **transfer_request** | [**TransferRequest**](TransferRequest.md)| transferRequest | [optional] 

### Return type

[**ApiResponseOfTransferResponse**](ApiResponseOfTransferResponse.md)

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

