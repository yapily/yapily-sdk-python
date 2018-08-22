# yapily.PaymentsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_initiation_using_post**](PaymentsApi.md#create_payment_initiation_using_post) | **POST** /initiate-payment-sortcode | Initiate a new single payment for user to authorise
[**create_payment_using_post**](PaymentsApi.md#create_payment_using_post) | **POST** /payment-sortcode | Create a new single payment
[**get_payment_initiation_status_using_get**](PaymentsApi.md#get_payment_initiation_status_using_get) | **GET** /payment-initiations/{paymentId} | Get status of a payment initiation
[**get_payment_status_using_get**](PaymentsApi.md#get_payment_status_using_get) | **GET** /payments/{paymentId} | Get status of a payment


# **create_payment_initiation_using_post**
> ApiResponseOfPaymentResponse create_payment_initiation_using_post(institution, payment_request=payment_request, user_uuid=user_uuid, param_callback=param_callback)

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
institution = 'institution_example' # str | institution
payment_request = yapily.SortCodePaymentRequest() # SortCodePaymentRequest | paymentRequest (optional)
user_uuid = 'user_uuid_example' # str | user-uuid (optional)
param_callback = 'param_callback_example' # str | callback (optional)

try:
    # Initiate a new single payment for user to authorise
    api_response = api_instance.create_payment_initiation_using_post(institution, payment_request=payment_request, user_uuid=user_uuid, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_initiation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution** | **str**| institution | 
 **payment_request** | [**SortCodePaymentRequest**](SortCodePaymentRequest.md)| paymentRequest | [optional] 
 **user_uuid** | **str**| user-uuid | [optional] 
 **param_callback** | **str**| callback | [optional] 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **get_payment_initiation_status_using_get**
> ApiResponseOfPaymentResponse get_payment_initiation_status_using_get(institution, payment_id)

Get status of a payment initiation

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
institution = 'institution_example' # str | institution
payment_id = 'payment_id_example' # str | paymentId

try:
    # Get status of a payment initiation
    api_response = api_instance.get_payment_initiation_status_using_get(institution, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_initiation_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution** | **str**| institution | 
 **payment_id** | **str**| paymentId | 

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

