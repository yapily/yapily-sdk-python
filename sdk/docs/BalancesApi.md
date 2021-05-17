# yapily.BalancesApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balances_using_get**](BalancesApi.md#get_account_balances_using_get) | **GET** /accounts/{accountId}/balances | Get account balances


# **get_account_balances_using_get**
> ApiResponseOfBalances get_account_balances_using_get(account_id, x_yapily_api_version=x_yapily_api_version, consent=consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Get account balances

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
    api_instance = yapily.BalancesApi(api_client)
    account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
consent = 'consent_example' # str | Consent Token (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get account balances
        api_response = api_instance.get_account_balances_using_get(account_id, x_yapily_api_version=x_yapily_api_version, consent=consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BalancesApi->get_account_balances_using_get: %s\n" % e)
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
    api_instance = yapily.BalancesApi(api_client)
    account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
consent = 'consent_example' # str | Consent Token (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get account balances
        api_response = api_instance.get_account_balances_using_get(account_id, x_yapily_api_version=x_yapily_api_version, consent=consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BalancesApi->get_account_balances_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **consent** | **str**| Consent Token | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiResponseOfBalances**](ApiResponseOfBalances.md)

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

