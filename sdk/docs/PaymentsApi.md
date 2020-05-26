# yapily.PaymentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_payment_authorisation_using_post**](PaymentsApi.md#create_bulk_payment_authorisation_using_post) | **POST** /bulk-payment-auth-requests | Initiate bulk payment for user to authorise
[**create_bulk_payment_using_post**](PaymentsApi.md#create_bulk_payment_using_post) | **POST** /bulk-payments | Create bulk payment
[**create_payment_authorisation_using_post**](PaymentsApi.md#create_payment_authorisation_using_post) | **POST** /payment-auth-requests | Initiate a payment for user to authorise
[**create_payment_authorisation_with_sort_code_using_post**](PaymentsApi.md#create_payment_authorisation_with_sort_code_using_post) | **POST** /payment-sortcode-auth-requests | Initiate a new single payment for user to authorise
[**create_payment_using_post**](PaymentsApi.md#create_payment_using_post) | **POST** /payments | Create a payment
[**create_payment_with_sort_code_using_post**](PaymentsApi.md#create_payment_with_sort_code_using_post) | **POST** /payment-sortcode | Create a new single payment
[**get_payment_status_using_get**](PaymentsApi.md#get_payment_status_using_get) | **GET** /payments/{paymentId} | Get status of a payment
[**get_payments_using_get**](PaymentsApi.md#get_payments_using_get) | **GET** /payments/{paymentId}/details | Get payments detail


# **create_bulk_payment_authorisation_using_post**
> ApiResponseOfPaymentAuthorisationRequestResponse create_bulk_payment_authorisation_using_post(payment_auth_request)

Initiate bulk payment for user to authorise

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.BulkPaymentAuthorisationRequest() # BulkPaymentAuthorisationRequest | paymentAuthRequest

    try:
        # Initiate bulk payment for user to authorise
        api_response = api_instance.create_bulk_payment_authorisation_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment_authorisation_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.BulkPaymentAuthorisationRequest() # BulkPaymentAuthorisationRequest | paymentAuthRequest

    try:
        # Initiate bulk payment for user to authorise
        api_response = api_instance.create_bulk_payment_authorisation_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment_authorisation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_auth_request** | [**BulkPaymentAuthorisationRequest**](BulkPaymentAuthorisationRequest.md)| paymentAuthRequest | 

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

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

# **create_bulk_payment_using_post**
> ApiResponseOfPaymentResponse create_bulk_payment_using_post(consent, payment_request)

Create bulk payment

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.BulkPaymentRequest() # BulkPaymentRequest | paymentRequest

    try:
        # Create bulk payment
        api_response = api_instance.create_bulk_payment_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.BulkPaymentRequest() # BulkPaymentRequest | paymentRequest

    try:
        # Create bulk payment
        api_response = api_instance.create_bulk_payment_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **payment_request** | [**BulkPaymentRequest**](BulkPaymentRequest.md)| paymentRequest | 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **create_payment_authorisation_using_post**
> ApiResponseOfPaymentAuthorisationRequestResponse create_payment_authorisation_using_post(payment_auth_request)

Initiate a payment for user to authorise

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.PaymentAuthorisationRequest() # PaymentAuthorisationRequest | paymentAuthRequest

    try:
        # Initiate a payment for user to authorise
        api_response = api_instance.create_payment_authorisation_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_authorisation_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.PaymentAuthorisationRequest() # PaymentAuthorisationRequest | paymentAuthRequest

    try:
        # Initiate a payment for user to authorise
        api_response = api_instance.create_payment_authorisation_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_authorisation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_auth_request** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)| paymentAuthRequest | 

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

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

# **create_payment_authorisation_with_sort_code_using_post**
> ApiResponseOfAuthorisationRequestResponse create_payment_authorisation_with_sort_code_using_post(payment_auth_request)

Initiate a new single payment for user to authorise

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.SortCodePaymentAuthRequest() # SortCodePaymentAuthRequest | paymentAuthRequest

    try:
        # Initiate a new single payment for user to authorise
        api_response = api_instance.create_payment_authorisation_with_sort_code_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_authorisation_with_sort_code_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_auth_request = yapily.SortCodePaymentAuthRequest() # SortCodePaymentAuthRequest | paymentAuthRequest

    try:
        # Initiate a new single payment for user to authorise
        api_response = api_instance.create_payment_authorisation_with_sort_code_using_post(payment_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_authorisation_with_sort_code_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_auth_request** | [**SortCodePaymentAuthRequest**](SortCodePaymentAuthRequest.md)| paymentAuthRequest | 

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

# **create_payment_using_post**
> ApiResponseOfPaymentResponse create_payment_using_post(consent, payment_request)

Create a payment

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.PaymentRequest() # PaymentRequest | paymentRequest

    try:
        # Create a payment
        api_response = api_instance.create_payment_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.PaymentRequest() # PaymentRequest | paymentRequest

    try:
        # Create a payment
        api_response = api_instance.create_payment_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **payment_request** | [**PaymentRequest**](PaymentRequest.md)| paymentRequest | 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **create_payment_with_sort_code_using_post**
> ApiResponseOfPaymentResponse create_payment_with_sort_code_using_post(consent, payment_request)

Create a new single payment

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.SortCodePaymentRequest() # SortCodePaymentRequest | paymentRequest

    try:
        # Create a new single payment
        api_response = api_instance.create_payment_with_sort_code_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_with_sort_code_using_post: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    consent = 'consent_example' # str | Consent Token
payment_request = yapily.SortCodePaymentRequest() # SortCodePaymentRequest | paymentRequest

    try:
        # Create a new single payment
        api_response = api_instance.create_payment_with_sort_code_using_post(consent, payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment_with_sort_code_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **payment_request** | [**SortCodePaymentRequest**](SortCodePaymentRequest.md)| paymentRequest | 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **get_payment_status_using_get**
> ApiResponseOfPaymentResponse get_payment_status_using_get(payment_id, consent)

Get status of a payment

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | paymentId
consent = 'consent_example' # str | Consent Token

    try:
        # Get status of a payment
        api_response = api_instance.get_payment_status_using_get(payment_id, consent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payment_status_using_get: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | paymentId
consent = 'consent_example' # str | Consent Token

    try:
        # Get status of a payment
        api_response = api_instance.get_payment_status_using_get(payment_id, consent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payment_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| paymentId | 
 **consent** | **str**| Consent Token | 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **get_payments_using_get**
> ApiResponseOfPaymentResponses get_payments_using_get(payment_id, consent)

Get payments detail

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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | paymentId
consent = 'consent_example' # str | Consent Token

    try:
        # Get payments detail
        api_response = api_instance.get_payments_using_get(payment_id, consent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payments_using_get: %s\n" % e)
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

# Defining host is optional and default to https://api.yapily.com
configuration.host = "https://api.yapily.com"

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | paymentId
consent = 'consent_example' # str | Consent Token

    try:
        # Get payments detail
        api_response = api_instance.get_payments_using_get(payment_id, consent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| paymentId | 
 **consent** | **str**| Consent Token | 

### Return type

[**ApiResponseOfPaymentResponses**](ApiResponseOfPaymentResponses.md)

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

