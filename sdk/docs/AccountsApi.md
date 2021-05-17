# yapily.AccountsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_direct_debits_using_get**](AccountsApi.md#get_account_direct_debits_using_get) | **GET** /accounts/{accountId}/direct-debits | Get account direct debits
[**get_account_periodic_payments_using_get**](AccountsApi.md#get_account_periodic_payments_using_get) | **GET** /accounts/{accountId}/periodic-payments | Get account payments detail
[**get_account_scheduled_payments_using_get**](AccountsApi.md#get_account_scheduled_payments_using_get) | **GET** /accounts/{accountId}/scheduled-payments | Get account scheduled payments
[**get_account_using_get**](AccountsApi.md#get_account_using_get) | **GET** /accounts/{accountId} | Get account
[**get_accounts_using_get**](AccountsApi.md#get_accounts_using_get) | **GET** /accounts | Get accounts
[**initiate_account_request_using_post**](AccountsApi.md#initiate_account_request_using_post) | **POST** /account-auth-requests | Initiate a new account request for user to authorize
[**re_authorise_account_using_patch**](AccountsApi.md#re_authorise_account_using_patch) | **PATCH** /account-auth-requests | Re-authorise account request
[**update_pre_authorise_account_consent_using_put**](AccountsApi.md#update_pre_authorise_account_consent_using_put) | **PUT** /account-auth-requests | Update pre authorize consent for user to authorise account


# **get_account_direct_debits_using_get**
> ApiListResponseOfPaymentResponse get_account_direct_debits_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)

Get account direct debits

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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's direct debit results (optional)

    try:
        # Get account direct debits
        api_response = api_instance.get_account_direct_debits_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_direct_debits_using_get: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's direct debit results (optional)

    try:
        # Get account direct debits
        api_response = api_instance.get_account_direct_debits_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_direct_debits_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | 
 **consent** | **str**| Consent Token | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **limit** | **int**| Use this parameter to limit account&#39;s direct debit results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

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

# **get_account_periodic_payments_using_get**
> ApiListResponseOfPaymentResponse get_account_periodic_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)

Get account payments detail

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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's periodic payment order results (optional)

    try:
        # Get account payments detail
        api_response = api_instance.get_account_periodic_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_periodic_payments_using_get: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's periodic payment order results (optional)

    try:
        # Get account payments detail
        api_response = api_instance.get_account_periodic_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_periodic_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | 
 **consent** | **str**| Consent Token | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **limit** | **int**| Use this parameter to limit account&#39;s periodic payment order results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

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

# **get_account_scheduled_payments_using_get**
> ApiListResponseOfPaymentResponse get_account_scheduled_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)

Get account scheduled payments

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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's scheduled payment results (optional)

    try:
        # Get account scheduled payments
        api_response = api_instance.get_account_scheduled_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_scheduled_payments_using_get: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Account Id
consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
limit = 56 # int | Use this parameter to limit account's scheduled payment results (optional)

    try:
        # Get account scheduled payments
        api_response = api_instance.get_account_scheduled_payments_using_get(account_id, consent, x_yapily_api_version=x_yapily_api_version, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_scheduled_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id | 
 **consent** | **str**| Consent Token | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **limit** | **int**| Use this parameter to limit account&#39;s scheduled payment results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

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

# **get_account_using_get**
> ApiResponseOfAccount get_account_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Get account

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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get account
        api_response = api_instance.get_account_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_using_get: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | Account Id
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get account
        api_response = api_instance.get_account_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| Account Id | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiResponseOfAccount**](ApiResponseOfAccount.md)

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

# **get_accounts_using_get**
> ApiListResponseOfAccount get_accounts_using_get(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Get accounts

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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get accounts
        api_response = api_instance.get_accounts_using_get(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_accounts_using_get: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Get accounts
        api_response = api_instance.get_accounts_using_get(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiListResponseOfAccount**](ApiListResponseOfAccount.md)

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

# **initiate_account_request_using_post**
> ApiResponseOfAuthorisationRequestResponse initiate_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Initiate a new account request for user to authorize

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
    api_instance = yapily.AccountsApi(api_client)
    account_auth_request = yapily.AccountAuthorisationRequest() # AccountAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Initiate a new account request for user to authorize
        api_response = api_instance.initiate_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->initiate_account_request_using_post: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    account_auth_request = yapily.AccountAuthorisationRequest() # AccountAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Initiate a new account request for user to authorize
        api_response = api_instance.initiate_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->initiate_account_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_auth_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)| accountAuthRequest | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

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

# **re_authorise_account_using_patch**
> ApiResponseOfAuthorisationRequestResponse re_authorise_account_using_patch(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Re-authorise account request

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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Re-authorise account request
        api_response = api_instance.re_authorise_account_using_patch(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->re_authorise_account_using_patch: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Re-authorise account request
        api_response = api_instance.re_authorise_account_using_patch(consent, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->re_authorise_account_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pre_authorise_account_consent_using_put**
> ApiResponseOfAuthorisationRequestResponse update_pre_authorise_account_consent_using_put(consent, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Update pre authorize consent for user to authorise account

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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_auth_request = yapily.AccountAuthorisationRequest() # AccountAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Update pre authorize consent for user to authorise account
        api_response = api_instance.update_pre_authorise_account_consent_using_put(consent, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->update_pre_authorise_account_consent_using_put: %s\n" % e)
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
    api_instance = yapily.AccountsApi(api_client)
    consent = 'consent_example' # str | Consent Token
account_auth_request = yapily.AccountAuthorisationRequest() # AccountAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | Api Version (optional)
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Update pre authorize consent for user to authorise account
        api_response = api_instance.update_pre_authorise_account_consent_using_put(consent, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->update_pre_authorise_account_consent_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_auth_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)| accountAuthRequest | 
 **x_yapily_api_version** | **str**| Api Version | [optional] 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

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

