# yapily.AccountsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_direct_debits_using_get**](AccountsApi.md#get_account_direct_debits_using_get) | **GET** /accounts/{accountId}/direct-debits | Get account direct debits
[**get_account_periodic_payments_using_get**](AccountsApi.md#get_account_periodic_payments_using_get) | **GET** /accounts/{accountId}/periodic-payments | Get account payments detail
[**get_account_scheduled_payments_using_get**](AccountsApi.md#get_account_scheduled_payments_using_get) | **GET** /accounts/{accountId}/scheduled-payments | Get account scheduled payments
[**get_account_using_get**](AccountsApi.md#get_account_using_get) | **GET** /accounts/{accountId} | Get account
[**get_accounts_using_get**](AccountsApi.md#get_accounts_using_get) | **GET** /accounts | Get accounts
[**initiate_account_request_using_post**](AccountsApi.md#initiate_account_request_using_post) | **POST** /account-auth-requests | Initiate a new account request for user to authorize
[**re_authorise_account_using_patch**](AccountsApi.md#re_authorise_account_using_patch) | **PATCH** /account-auth-requests | Re-authorize account request


# **get_account_direct_debits_using_get**
> ApiListResponseOfPaymentResponse get_account_direct_debits_using_get(account_id, consent, limit=limit)

Get account direct debits

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
consent = 'consent_example' # str | Consent Token
limit = 56 # int | Use this parameter to limit account's direct debit results (optional)

try:
    # Get account direct debits
    api_response = api_instance.get_account_direct_debits_using_get(account_id, consent, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_direct_debits_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **consent** | **str**| Consent Token | 
 **limit** | **int**| Use this parameter to limit account&#39;s direct debit results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_periodic_payments_using_get**
> ApiListResponseOfPaymentResponse get_account_periodic_payments_using_get(account_id, consent, limit=limit)

Get account payments detail

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
consent = 'consent_example' # str | Consent Token
limit = 56 # int | Use this parameter to limit account's periodic payment order results (optional)

try:
    # Get account payments detail
    api_response = api_instance.get_account_periodic_payments_using_get(account_id, consent, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_periodic_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **consent** | **str**| Consent Token | 
 **limit** | **int**| Use this parameter to limit account&#39;s periodic payment order results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_scheduled_payments_using_get**
> ApiListResponseOfPaymentResponse get_account_scheduled_payments_using_get(account_id, consent, limit=limit)

Get account scheduled payments

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
consent = 'consent_example' # str | Consent Token
limit = 56 # int | Use this parameter to limit account's scheduled payment results (optional)

try:
    # Get account scheduled payments
    api_response = api_instance.get_account_scheduled_payments_using_get(account_id, consent, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_scheduled_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **consent** | **str**| Consent Token | 
 **limit** | **int**| Use this parameter to limit account&#39;s scheduled payment results | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_using_get**
> ApiResponseOfAccount get_account_using_get(consent, account_id)

Get account

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId

try:
    # Get account
    api_response = api_instance.get_account_using_get(consent, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| accountId | 

### Return type

[**ApiResponseOfAccount**](ApiResponseOfAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_using_get**
> ApiListResponseOfAccount get_accounts_using_get(consent)

Get accounts

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token

try:
    # Get accounts
    api_response = api_instance.get_accounts_using_get(consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 

### Return type

[**ApiListResponseOfAccount**](ApiListResponseOfAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_account_request_using_post**
> ApiResponseOfAuthorisationRequestResponse initiate_account_request_using_post(account_auth_request)

Initiate a new account request for user to authorize

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
account_auth_request = yapily.AccountAuthorisationRequest() # AccountAuthorisationRequest | accountAuthRequest

try:
    # Initiate a new account request for user to authorize
    api_response = api_instance.initiate_account_request_using_post(account_auth_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->initiate_account_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_auth_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)| accountAuthRequest | 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_authorise_account_using_patch**
> ApiResponseOfAuthorisationRequestResponse re_authorise_account_using_patch(consent)

Re-authorize account request

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
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token

try:
    # Re-authorize account request
    api_response = api_instance.re_authorise_account_using_patch(consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->re_authorise_account_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

