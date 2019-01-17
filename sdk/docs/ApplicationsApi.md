# yapily.ApplicationsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_me_using_get**](ApplicationsApi.md#get_application_me_using_get) | **GET** /me | Returns the details of the application that owns the request credentials
[**get_jwks_using_get**](ApplicationsApi.md#get_jwks_using_get) | **GET** /jwks | JSON Web Key Set (JWKS) for authenticated application
[**revoke_tokens_using_post**](ApplicationsApi.md#revoke_tokens_using_post) | **POST** /revoke-tokens | Revoke existing access tokens for application, which will also generate a new public key discoverable via /jwks


# **get_application_me_using_get**
> Application get_application_me_using_get()

Returns the details of the application that owns the request credentials

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
api_instance = yapily.ApplicationsApi(yapily.ApiClient(configuration))

try:
    # Returns the details of the application that owns the request credentials
    api_response = api_instance.get_application_me_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_application_me_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Application**](Application.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwks_using_get**
> object get_jwks_using_get()

JSON Web Key Set (JWKS) for authenticated application

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
api_instance = yapily.ApplicationsApi(yapily.ApiClient(configuration))

try:
    # JSON Web Key Set (JWKS) for authenticated application
    api_response = api_instance.get_jwks_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_jwks_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_tokens_using_post**
> ResponseEntity revoke_tokens_using_post()

Revoke existing access tokens for application, which will also generate a new public key discoverable via /jwks

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
api_instance = yapily.ApplicationsApi(yapily.ApiClient(configuration))

try:
    # Revoke existing access tokens for application, which will also generate a new public key discoverable via /jwks
    api_response = api_instance.revoke_tokens_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->revoke_tokens_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

