# yapily.TransactionsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions_using_get**](TransactionsApi.md#get_transactions_using_get) | **GET** /accounts/{accountId}/transactions | Get account transactions


# **get_transactions_using_get**
> ApiListResponseOfTransaction get_transactions_using_get(consent, account_id, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)

Get account transactions

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
    api_instance = yapily.TransactionsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
_with = ['_with_example'] # list[str] | with (optional)
_from = '_from_example' # str | from (optional)
before = 'before_example' # str | before (optional)
limit = 56 # int | limit (optional)
sort = 'sort_example' # str | sort (optional)
offset = 56 # int | offset (optional)
cursor = 'cursor_example' # str | cursor (optional)

    try:
        # Get account transactions
        api_response = api_instance.get_transactions_using_get(consent, account_id, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_using_get: %s\n" % e)
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
    api_instance = yapily.TransactionsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
_with = ['_with_example'] # list[str] | with (optional)
_from = '_from_example' # str | from (optional)
before = 'before_example' # str | before (optional)
limit = 56 # int | limit (optional)
sort = 'sort_example' # str | sort (optional)
offset = 56 # int | offset (optional)
cursor = 'cursor_example' # str | cursor (optional)

    try:
        # Get account transactions
        api_response = api_instance.get_transactions_using_get(consent, account_id, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| accountId | 
 **_with** | [**list[str]**](str.md)| with | [optional] 
 **_from** | **str**| from | [optional] 
 **before** | **str**| before | [optional] 
 **limit** | **int**| limit | [optional] 
 **sort** | **str**| sort | [optional] 
 **offset** | **int**| offset | [optional] 
 **cursor** | **str**| cursor | [optional] 

### Return type

[**ApiListResponseOfTransaction**](ApiListResponseOfTransaction.md)

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

