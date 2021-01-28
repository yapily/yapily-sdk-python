# yapily.EmbeddedPaymentsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embedded_payment_authorisation_using_post**](EmbeddedPaymentsApi.md#create_embedded_payment_authorisation_using_post) | **POST** /embedded-payment-auth-requests | Initiate an embedded payment for user to authorise
[**update_embedded_payment_authorisation_using_put**](EmbeddedPaymentsApi.md#update_embedded_payment_authorisation_using_put) | **PUT** /embedded-payment-auth-requests/{consentId} | Update an embedded payment initiation with SCA info


# **create_embedded_payment_authorisation_using_post**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse create_embedded_payment_authorisation_using_post(payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Initiate an embedded payment for user to authorise

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
    api_instance = yapily.EmbeddedPaymentsApi(api_client)
    payment_auth_request = yapily.PaymentEmbeddedAuthorisationRequest() # PaymentEmbeddedAuthorisationRequest | paymentAuthRequest
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Initiate an embedded payment for user to authorise
        api_response = api_instance.create_embedded_payment_authorisation_using_post(payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedPaymentsApi->create_embedded_payment_authorisation_using_post: %s\n" % e)
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
    api_instance = yapily.EmbeddedPaymentsApi(api_client)
    payment_auth_request = yapily.PaymentEmbeddedAuthorisationRequest() # PaymentEmbeddedAuthorisationRequest | paymentAuthRequest
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Initiate an embedded payment for user to authorise
        api_response = api_instance.create_embedded_payment_authorisation_using_post(payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedPaymentsApi->create_embedded_payment_authorisation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_auth_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)| paymentAuthRequest | 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

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

# **update_embedded_payment_authorisation_using_put**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse update_embedded_payment_authorisation_using_put(consent_id, payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Update an embedded payment initiation with SCA info

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
    api_instance = yapily.EmbeddedPaymentsApi(api_client)
    consent_id = 'consent_id_example' # str | consentId
payment_auth_request = yapily.PaymentEmbeddedAuthorisationRequest() # PaymentEmbeddedAuthorisationRequest | paymentAuthRequest
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Update an embedded payment initiation with SCA info
        api_response = api_instance.update_embedded_payment_authorisation_using_put(consent_id, payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedPaymentsApi->update_embedded_payment_authorisation_using_put: %s\n" % e)
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
    api_instance = yapily.EmbeddedPaymentsApi(api_client)
    consent_id = 'consent_id_example' # str | consentId
payment_auth_request = yapily.PaymentEmbeddedAuthorisationRequest() # PaymentEmbeddedAuthorisationRequest | paymentAuthRequest
psu_id = 'psu_id_example' # str | PSU ID (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | PSU ID CORPORATE (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU IP ADDRESS (optional)

    try:
        # Update an embedded payment initiation with SCA info
        api_response = api_instance.update_embedded_payment_authorisation_using_put(consent_id, payment_auth_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedPaymentsApi->update_embedded_payment_authorisation_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| consentId | 
 **payment_auth_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)| paymentAuthRequest | 
 **psu_id** | **str**| PSU ID | [optional] 
 **psu_corporate_id** | **str**| PSU ID CORPORATE | [optional] 
 **psu_ip_address** | **str**| PSU IP ADDRESS | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

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

