# yapily.TransactionsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions_using_get**](TransactionsApi.md#get_transactions_using_get) | **GET** /accounts/{accountId}/transactions | Get account transactions


# **get_transactions_using_get**
> ClientBasedApiListResponseOfTransaction get_transactions_using_get(consent, account_id, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset)

Get account transactions

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
# Configure OAuth2 access token for authorization: tokenAuth
configuration = yapily.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = yapily.TransactionsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
_with = ['_with_example'] # list[str] | with (optional)
_from = '_from_example' # str | from (optional)
before = 'before_example' # str | before (optional)
limit = 56 # int | limit (optional)
sort = 'sort_example' # str | sort (optional)
offset = 56 # int | offset (optional)

try:
    # Get account transactions
    api_response = api_instance.get_transactions_using_get(consent, account_id, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset)
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

### Return type

[**ClientBasedApiListResponseOfTransaction**](ClientBasedApiListResponseOfTransaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

