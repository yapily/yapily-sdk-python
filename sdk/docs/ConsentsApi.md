# yapily.ConsentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_consent_using_post**](ConsentsApi.md#add_consent_using_post) | **POST** /users/{userUuid}/consents | Post consent
[**create_consent_with_code_using_post**](ConsentsApi.md#create_consent_with_code_using_post) | **POST** /consent-auth-code | Post auth-code and auth-state
[**delete_using_delete**](ConsentsApi.md#delete_using_delete) | **DELETE** /consents/{consentId} | Delete consent
[**get_consent_by_id_using_get**](ConsentsApi.md#get_consent_by_id_using_get) | **GET** /consents/{consentId} | Get consent
[**get_consent_by_single_access_consent_using_post**](ConsentsApi.md#get_consent_by_single_access_consent_using_post) | **POST** /consent-one-time-token | Post one time token
[**get_user_consents_using_get**](ConsentsApi.md#get_user_consents_using_get) | **GET** /users/{userUuid}/consents | Get user consents


# **add_consent_using_post**
> Consent add_consent_using_post(user_uuid, create_consent_access_token)

Post consent

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | userUuid
create_consent_access_token = yapily.CreateConsentAccessToken() # CreateConsentAccessToken | createConsentAccessToken

try:
    # Post consent
    api_response = api_instance.add_consent_using_post(user_uuid, create_consent_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->add_consent_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| userUuid | 
 **create_consent_access_token** | [**CreateConsentAccessToken**](CreateConsentAccessToken.md)| createConsentAccessToken | 

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_consent_with_code_using_post**
> Consent create_consent_with_code_using_post(consent_by_auth_code)

Post auth-code and auth-state

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
consent_by_auth_code = yapily.ConsentAuthCodeRequest() # ConsentAuthCodeRequest | consentByAuthCode

try:
    # Post auth-code and auth-state
    api_response = api_instance.create_consent_with_code_using_post(consent_by_auth_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->create_consent_with_code_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_by_auth_code** | [**ConsentAuthCodeRequest**](ConsentAuthCodeRequest.md)| consentByAuthCode | 

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> ApiResponseOfConsentDeleteResponse delete_using_delete(consent_id, force_delete=force_delete)

Delete consent

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
consent_id = 'consent_id_example' # str | consentId
force_delete = true # bool | forceDelete (optional)

try:
    # Delete consent
    api_response = api_instance.delete_using_delete(consent_id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| consentId | 
 **force_delete** | **bool**| forceDelete | [optional] 

### Return type

[**ApiResponseOfConsentDeleteResponse**](ApiResponseOfConsentDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_by_id_using_get**
> ApiResponseOfConsent get_consent_by_id_using_get(consent_id)

Get consent

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
consent_id = 'consent_id_example' # str | consentId

try:
    # Get consent
    api_response = api_instance.get_consent_by_id_using_get(consent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->get_consent_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| consentId | 

### Return type

[**ApiResponseOfConsent**](ApiResponseOfConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_by_single_access_consent_using_post**
> Consent get_consent_by_single_access_consent_using_post(one_time_token)

Post one time token

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
one_time_token = yapily.OneTimeTokenRequest() # OneTimeTokenRequest | oneTimeToken

try:
    # Post one time token
    api_response = api_instance.get_consent_by_single_access_consent_using_post(one_time_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->get_consent_by_single_access_consent_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **one_time_token** | [**OneTimeTokenRequest**](OneTimeTokenRequest.md)| oneTimeToken | 

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_consents_using_get**
> list[Consent] get_user_consents_using_get(user_uuid, institution_id=institution_id)

Get user consents

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
api_instance = yapily.ConsentsApi(yapily.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | userUuid
institution_id = 'institution_id_example' # str | institutionId (optional)

try:
    # Get user consents
    api_response = api_instance.get_user_consents_using_get(user_uuid, institution_id=institution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->get_user_consents_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| userUuid | 
 **institution_id** | **str**| institutionId | [optional] 

### Return type

[**list[Consent]**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

