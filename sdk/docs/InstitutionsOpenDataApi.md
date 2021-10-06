# yapily.InstitutionsOpenDataApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_atm_data_using_get**](InstitutionsOpenDataApi.md#get_atm_data_using_get) | **GET** /institutions/{institutionId}/atms | Retrieves data about all ATMs of the selected institution
[**get_personal_current_accounts_using_get**](InstitutionsOpenDataApi.md#get_personal_current_accounts_using_get) | **GET** /institutions/{institutionId}/personal-current-accounts | Retrieves details of personal current accounts for an institution


# **get_atm_data_using_get**
> ApiResponseOfListOfATMOpenDataResponse get_atm_data_using_get(institution_id)

Retrieves data about all ATMs of the selected institution

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
    api_instance = yapily.InstitutionsOpenDataApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves data about all ATMs of the selected institution
        api_response = api_instance.get_atm_data_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsOpenDataApi->get_atm_data_using_get: %s\n" % e)
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
    api_instance = yapily.InstitutionsOpenDataApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves data about all ATMs of the selected institution
        api_response = api_instance.get_atm_data_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsOpenDataApi->get_atm_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **str**| institutionId | 

### Return type

[**ApiResponseOfListOfATMOpenDataResponse**](ApiResponseOfListOfATMOpenDataResponse.md)

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

# **get_personal_current_accounts_using_get**
> ApiResponseOfListOfPersonalCurrentAccountData get_personal_current_accounts_using_get(institution_id)

Retrieves details of personal current accounts for an institution

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
    api_instance = yapily.InstitutionsOpenDataApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves details of personal current accounts for an institution
        api_response = api_instance.get_personal_current_accounts_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsOpenDataApi->get_personal_current_accounts_using_get: %s\n" % e)
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
    api_instance = yapily.InstitutionsOpenDataApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves details of personal current accounts for an institution
        api_response = api_instance.get_personal_current_accounts_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsOpenDataApi->get_personal_current_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **str**| institutionId | 

### Return type

[**ApiResponseOfListOfPersonalCurrentAccountData**](ApiResponseOfListOfPersonalCurrentAccountData.md)

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

