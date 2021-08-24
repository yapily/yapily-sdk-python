# yapily.TransactionsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions_using_get**](TransactionsApi.md#get_transactions_using_get) | **GET** /accounts/{accountId}/transactions | Get account transactions


# **get_transactions_using_get**
> ApiListResponseOfTransaction get_transactions_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)

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
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
_with = ['_with_example'] # list[str] | __Optional__. Can be `categories`, `categories-business` or `merchant`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'merchant' enrichment data is requested, the enrichment response will include merchant data only if it can be evaluated from the transaction. (optional)
_from = '_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. (optional)
sort = 'sort_example' # str | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)
cursor = 'cursor_example' # str | __Optional__. This property is not currently in use. (optional)

    try:
        # Get account transactions
        api_response = api_instance.get_transactions_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)
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
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
_with = ['_with_example'] # list[str] | __Optional__. Can be `categories`, `categories-business` or `merchant`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'merchant' enrichment data is requested, the enrichment response will include merchant data only if it can be evaluated from the transaction. (optional)
_from = '_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. (optional)
sort = 'sort_example' # str | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)
cursor = 'cursor_example' # str | __Optional__. This property is not currently in use. (optional)

    try:
        # Get account transactions
        api_response = api_instance.get_transactions_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, _with=_with, _from=_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **_with** | [**list[str]**](str.md)| __Optional__. Can be &#x60;categories&#x60;, &#x60;categories-business&#x60; or &#x60;merchant&#x60;. When set, will include enrichment data in the transactions returned. &lt;br&gt;&lt;br&gt;Enrichment data is optional, e.g. when &#39;merchant&#39; enrichment data is requested, the enrichment response will include merchant data only if it can be evaluated from the transaction. | [optional] 
 **_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. | [optional] 
 **sort** | **str**| __Optional__. Sort transaction records by date ascending with &#39;date&#39; or descending with &#39;-date&#39;. The default sort order is descending | [optional] 
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] 
 **cursor** | **str**| __Optional__. This property is not currently in use. | [optional] 

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

