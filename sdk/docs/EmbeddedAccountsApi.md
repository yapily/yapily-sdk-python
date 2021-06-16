# yapily.EmbeddedAccountsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiate_embedded_account_request_using_post**](EmbeddedAccountsApi.md#initiate_embedded_account_request_using_post) | **POST** /embedded-account-auth-requests | Initiate a new embedded account request for user to authorize
[**update_embedded_account_request_using_put**](EmbeddedAccountsApi.md#update_embedded_account_request_using_put) | **PUT** /embedded-account-auth-requests/{consentId} | Update an embedded account request with SCA info


# **initiate_embedded_account_request_using_post**
> ApiResponseOfAuthorisationEmbeddedRequestResponse initiate_embedded_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Initiate a new embedded account request for user to authorize

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
    api_instance = yapily.EmbeddedAccountsApi(api_client)
    account_auth_request = yapily.AccountEmbeddedAuthorisationRequest() # AccountEmbeddedAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)

    try:
        # Initiate a new embedded account request for user to authorize
        api_response = api_instance.initiate_embedded_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedAccountsApi->initiate_embedded_account_request_using_post: %s\n" % e)
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
    api_instance = yapily.EmbeddedAccountsApi(api_client)
    account_auth_request = yapily.AccountEmbeddedAuthorisationRequest() # AccountEmbeddedAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)

    try:
        # Initiate a new embedded account request for user to authorize
        api_response = api_instance.initiate_embedded_account_request_using_post(account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedAccountsApi->initiate_embedded_account_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_auth_request** | [**AccountEmbeddedAuthorisationRequest**](AccountEmbeddedAuthorisationRequest.md)| accountAuthRequest | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 

### Return type

[**ApiResponseOfAuthorisationEmbeddedRequestResponse**](ApiResponseOfAuthorisationEmbeddedRequestResponse.md)

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

# **update_embedded_account_request_using_put**
> ApiResponseOfAuthorisationEmbeddedRequestResponse update_embedded_account_request_using_put(consent_id, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)

Update an embedded account request with SCA info

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
    api_instance = yapily.EmbeddedAccountsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
account_auth_request = yapily.AccountEmbeddedAuthorisationRequest() # AccountEmbeddedAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)

    try:
        # Update an embedded account request with SCA info
        api_response = api_instance.update_embedded_account_request_using_put(consent_id, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedAccountsApi->update_embedded_account_request_using_put: %s\n" % e)
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
    api_instance = yapily.EmbeddedAccountsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
account_auth_request = yapily.AccountEmbeddedAuthorisationRequest() # AccountEmbeddedAuthorisationRequest | accountAuthRequest
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)

    try:
        # Update an embedded account request with SCA info
        api_response = api_instance.update_embedded_account_request_using_put(consent_id, account_auth_request, x_yapily_api_version=x_yapily_api_version, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmbeddedAccountsApi->update_embedded_account_request_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **account_auth_request** | [**AccountEmbeddedAuthorisationRequest**](AccountEmbeddedAuthorisationRequest.md)| accountAuthRequest | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 

### Return type

[**ApiResponseOfAuthorisationEmbeddedRequestResponse**](ApiResponseOfAuthorisationEmbeddedRequestResponse.md)

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

