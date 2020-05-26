# yapily.InstitutionsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature_details_using_get**](InstitutionsApi.md#get_feature_details_using_get) | **GET** /features | Retrieve details for Yapily&#39;s institution features
[**get_institution_using_get**](InstitutionsApi.md#get_institution_using_get) | **GET** /institutions/{institutionId} | Retrieves details of a specific institution available in Yapily
[**get_institutions_using_get**](InstitutionsApi.md#get_institutions_using_get) | **GET** /institutions | Retrieves the list of institutions available in Yapily


# **get_feature_details_using_get**
> ApiListResponseOfFeatureDetails get_feature_details_using_get()

Retrieve details for Yapily's institution features

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
    api_instance = yapily.InstitutionsApi(api_client)
    
    try:
        # Retrieve details for Yapily's institution features
        api_response = api_instance.get_feature_details_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_feature_details_using_get: %s\n" % e)
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
    api_instance = yapily.InstitutionsApi(api_client)
    
    try:
        # Retrieve details for Yapily's institution features
        api_response = api_instance.get_feature_details_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_feature_details_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfFeatureDetails**](ApiListResponseOfFeatureDetails.md)

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

# **get_institution_using_get**
> Institution get_institution_using_get(institution_id)

Retrieves details of a specific institution available in Yapily

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
    api_instance = yapily.InstitutionsApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves details of a specific institution available in Yapily
        api_response = api_instance.get_institution_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_institution_using_get: %s\n" % e)
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
    api_instance = yapily.InstitutionsApi(api_client)
    institution_id = 'institution_id_example' # str | institutionId

    try:
        # Retrieves details of a specific institution available in Yapily
        api_response = api_instance.get_institution_using_get(institution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_institution_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **str**| institutionId | 

### Return type

[**Institution**](Institution.md)

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

# **get_institutions_using_get**
> ApiListResponseOfInstitution get_institutions_using_get()

Retrieves the list of institutions available in Yapily

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
    api_instance = yapily.InstitutionsApi(api_client)
    
    try:
        # Retrieves the list of institutions available in Yapily
        api_response = api_instance.get_institutions_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_institutions_using_get: %s\n" % e)
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
    api_instance = yapily.InstitutionsApi(api_client)
    
    try:
        # Retrieves the list of institutions available in Yapily
        api_response = api_instance.get_institutions_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstitutionsApi->get_institutions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfInstitution**](ApiListResponseOfInstitution.md)

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

