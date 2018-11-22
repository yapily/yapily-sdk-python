# yapily.PaymentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_initiation_using_post**](PaymentsApi.md#create_payment_initiation_using_post) | **POST** /payment-sortcode-auth-requests | Initiate a new single payment for user to authorise
[**create_payment_using_post**](PaymentsApi.md#create_payment_using_post) | **POST** /payment-sortcode | Create a new single payment
[**get_payment_status_using_get**](PaymentsApi.md#get_payment_status_using_get) | **GET** /payments/{paymentId} | Get status of a payment


# **create_payment_initiation_using_post**
> ApiResponseOfAuthorisationRequestResponse create_payment_initiation_using_post(payment_auth_request=payment_auth_request)

Initiate a new single payment for user to authorise

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
api_instance = yapily.PaymentsApi(yapily.ApiClient(configuration))
payment_auth_request = yapily.SortCodePaymentAuthRequest() # SortCodePaymentAuthRequest | paymentAuthRequest (optional)

try:
    # Initiate a new single payment for user to authorise
    api_response = api_instance.create_payment_initiation_using_post(payment_auth_request=payment_auth_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_initiation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_auth_request** | [**SortCodePaymentAuthRequest**](SortCodePaymentAuthRequest.md)| paymentAuthRequest | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_using_post**
> ApiResponseOfPaymentResponse create_payment_using_post(consent, payment_request=payment_request)

Create a new single payment

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
api_instance = yapily.PaymentsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
payment_request = yapily.SortCodePaymentRequest() # SortCodePaymentRequest | paymentRequest (optional)

try:
    # Create a new single payment
    api_response = api_instance.create_payment_using_post(consent, payment_request=payment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **payment_request** | [**SortCodePaymentRequest**](SortCodePaymentRequest.md)| paymentRequest | [optional] 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_status_using_get**
> ApiResponseOfPaymentResponse get_payment_status_using_get(payment_id, consent)

Get status of a payment

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
api_instance = yapily.PaymentsApi(yapily.ApiClient(configuration))
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

