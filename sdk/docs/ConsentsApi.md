# yapily.ConsentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consent_with_code**](ConsentsApi.md#create_consent_with_code) | **POST** /consent-auth-code | Exchange OAuth2 Code
[**delete**](ConsentsApi.md#delete) | **DELETE** /consents/{consentId} | Delete Consent
[**extend_consent**](ConsentsApi.md#extend_consent) | **POST** /consents/{consentId}/extend | Extend Consent
[**get_consent_by_id**](ConsentsApi.md#get_consent_by_id) | **GET** /consents/{consentId} | Get Consent
[**get_consent_by_single_access_consent**](ConsentsApi.md#get_consent_by_single_access_consent) | **POST** /consent-one-time-token | Exchange One Time Token
[**get_consents**](ConsentsApi.md#get_consents) | **GET** /consents | Get Consents


# **create_consent_with_code**
> Consent create_consent_with_code(consent_auth_code_request)

Exchange OAuth2 Code

Used to obtain a Yapily Consent object containing the `consentToken` once the user has authenticated and you have an OAuth2 authorisation code `auth-code` and state `auth-state`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.consent import Consent
from yapily.model.consent_auth_code_request import ConsentAuthCodeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    consent_auth_code_request = ConsentAuthCodeRequest(
        auth_code="6b965fbb-ff09-4afa-b897-90c34797cb8f&id_token=eyJhbGciOiJQUzI1NiIsImtpZCI6InprYm9LRmpRUndCZDlVRW5QQzV3bHY1N2lnNCJ9.eyJzdWIiOiJzZHAtNi0xZjA1MjBiNC1mZmNkLTQ4OTgtYWVkMC0wYjU0Y2I2ZDkwM2QiLCJvcGVuYmFua2luZ19pbnRlbnRfaWQiOiJzZHAtNi0xZjA1MjBiNC1mZmNkLTQ4OTgtYWVkMC0wYjU0Y2I2ZDkwM2QiLCJwc3VfaWRlbnRpZmllcnMiOnsidXNlcklkIjoiNzAwMDAxMDAwMDAwMDAwMDAwMDAwMDAyIiwiY29tcGFueUlkIjoiMTIzNDUifSwiaXNzIjoiaHR0cHM6Ly9vYjE5LWF1dGgxLXVpLm8zYmFuay5jby51ayIsImF1ZCI6IjA0ZmJjMGQ5LTlmMDgtNGIyOC1iNjY2LWFkNmEwYmMzM2NjZSIsImlhdCI6MTYxMTIyMjgzNywiZXhwIjoxNjExMjI2NDM3LCJub25jZSI6IjEyNzBjYjJmZmM0ODQyYjc4OTUzYWZhMjIyOGUwYTg5IiwiYXV0aF90aW1lIjoxNjExMjIyODM3LCJhenAiOiIwNGZiYzBkOS05ZjA4LTRiMjgtYjY2Ni1hZDZhMGJjMzNjY2UiLCJyZWZyZXNoX3Rva2VuX2V4cGlyZXNfYXQiOjE2MTE2MTE2MzcsImNfaGFzaCI6Inc5NG9pTkg1RWlBdVNKdWJfUHAxSlEiLCJzX2hhc2giOiJhRmxHY3dJY1EtdTVHYnBmcXRCR293IiwiYWNyIjoidXJuOm9wZW5iYW5raW5nOnBzZDI6c2NhIn0.nfaJ-llxVVa4HS7oii2oGgAV6k3MPwtQLFaOAZ2RY8VcxoWBkXKnrPkwf2jRHvE4aJnnfD3BcDAfJNeDBFEt5YQcujl0NxQm3XpOVkhjUVvINjmi9zbDMz2WFDpz8hSZZxvzxQ29h5nFSFcvXxE-0d2i10nX87OVlophc5GabHt3mnP3UbFIy-k0i9a9JGodheF9Qu3J-q2bgNJpLww8jj-gNH1LekG3qu8fxaB1c5-MuERfSWvrgwrJKKUe_yIxXVpL4zMMXw3B6JGIeUgPHKtAZxiAA9YA6dTlA1yPQwOfh4B-qvAZDmuGBnoB3iUXKLIUqBUA8j3rzLkQj51ORg",
        auth_state="1270cb2ffc4842b78953afa2228e0a87",
    ) # ConsentAuthCodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Exchange OAuth2 Code
        api_response = api_instance.create_consent_with_code(consent_auth_code_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->create_consent_with_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_auth_code_request** | [**ConsentAuthCodeRequest**](ConsentAuthCodeRequest.md)|  |

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiResponseOfConsentDeleteResponse delete(consent_id)

Delete Consent

Delete a consent using the consent Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.api_response_of_consent_delete_response import ApiResponseOfConsentDeleteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.
    force_delete = True # bool | __Optional__. Whether to force the deletion. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Delete Consent
        api_response = api_instance.delete(consent_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Consent
        api_response = api_instance.delete(consent_id, force_delete=force_delete)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |
 **force_delete** | **bool**| __Optional__. Whether to force the deletion. | [optional] if omitted the server will use the default value of True

### Return type

[**ApiResponseOfConsentDeleteResponse**](ApiResponseOfConsentDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_consent**
> ApiResponseOfConsent extend_consent(consent_id, extend_consent_request)

Extend Consent

Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.api_response_of_consent import ApiResponseOfConsent
from yapily.model.extend_consent_request import ExtendConsentRequest
from yapily.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.
    extend_consent_request = ExtendConsentRequest(
        last_confirmed_at=dateutil_parser('2022-08-16T10:59:53.288Z'),
    ) # ExtendConsentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Extend Consent
        api_response = api_instance.extend_consent(consent_id, extend_consent_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->extend_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |
 **extend_consent_request** | [**ExtendConsentRequest**](ExtendConsentRequest.md)|  |

### Return type

[**ApiResponseOfConsent**](ApiResponseOfConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Error Response. The supplied lastConfirmedAt date, Consent type, or Consent status is invalid. |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_by_id**
> ApiResponseOfConsent get_consent_by_id(consent_id)

Get Consent

Get consent using the consent Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.api_response_of_consent import ApiResponseOfConsent
from yapily.model.api_response_error import ApiResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.

    # example passing only required values which don't have defaults set
    try:
        # Get Consent
        api_response = api_instance.get_consent_by_id(consent_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->get_consent_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |

### Return type

[**ApiResponseOfConsent**](ApiResponseOfConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_by_single_access_consent**
> Consent get_consent_by_single_access_consent(one_time_token_request)

Exchange One Time Token

Exchange a One-time-token for the consent token

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.one_time_token_request import OneTimeTokenRequest
from yapily.model.api_response_error import ApiResponseError
from yapily.model.consent import Consent
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    one_time_token_request = OneTimeTokenRequest(
        one_time_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJJTlNUSVRVVElPTiI6ImJidmEtc2FuZGJveCIsIlVVSUQiOiJmMzNmNGU4ZC1jMDQ0LTQ2YTktOTlkMC0wYmRlMzIyYTJjOTIifQ.4Qv3NJI6av2nKi1U3aNmm71cIwJ3TvRsIlYDafQUVv_Khy_e-8oEpV_BoP4V1CII12oT-Yq4cPveHILz8BOwjg",
    ) # OneTimeTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Exchange One Time Token
        api_response = api_instance.get_consent_by_single_access_consent(one_time_token_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->get_consent_by_single_access_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **one_time_token_request** | [**OneTimeTokenRequest**](OneTimeTokenRequest.md)|  |

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> ApiListResponseOfConsent get_consents()

Get Consents

Used to retrieve all the consents created for each user within an application

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import consents_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.api_list_response_of_consent import ApiListResponseOfConsent
from pprint import pprint
# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consents_api.ConsentsApi(api_client)
    filter_application_user_id = [
        "filter[applicationUserId]_example",
    ] # [str] | __Optional__. Filter records based on the list of `applicationUserId` users provided. (optional)
    filter_user_uuid = [
        "filter[userUuid]_example",
    ] # [str] | __Optional__. Filter records based on the list of `userUuid` users provided. (optional)
    filter_institution = [
        "filter[institution]_example",
    ] # [str] | __Optional__. Filter records based on the list of `Institution` provided. (optional)
    filter_status = [
        "filter[status]_example",
    ] # [str] | __Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response). (optional)
    _from = "from_example" # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
    before = "before_example" # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    limit = 1 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. (optional)
    offset = 0 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Consents
        api_response = api_instance.get_consents(filter_application_user_id=filter_application_user_id, filter_user_uuid=filter_user_uuid, filter_institution=filter_institution, filter_status=filter_status, _from=_from, before=before, limit=limit, offset=offset)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling ConsentsApi->get_consents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application_user_id** | **[str]**| __Optional__. Filter records based on the list of &#x60;applicationUserId&#x60; users provided. | [optional]
 **filter_user_uuid** | **[str]**| __Optional__. Filter records based on the list of &#x60;userUuid&#x60; users provided. | [optional]
 **filter_institution** | **[str]**| __Optional__. Filter records based on the list of &#x60;Institution&#x60; provided. | [optional]
 **filter_status** | **[str]**| __Optional__. Filter records based on the list of &#x60;Consent&#x60; [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c&#x3D;200&amp;path&#x3D;data/status&amp;t&#x3D;response). | [optional]
 **_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional]
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional]
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. | [optional]
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] if omitted the server will use the default value of 0

### Return type

[**ApiListResponseOfConsent**](ApiListResponseOfConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

