# yapily.InstitutionsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_institution_using_get**](InstitutionsApi.md#get_institution_using_get) | **GET** /institutions/{institutionId} | Retrieves details of a specific institution available in Yapily
[**get_institutions_using_get**](InstitutionsApi.md#get_institutions_using_get) | **GET** /institutions | Retrieves the list of institutions available in Yapily


# **get_institution_using_get**
> Institution get_institution_using_get(institution_id)

Retrieves details of a specific institution available in Yapily

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
api_instance = yapily.InstitutionsApi(yapily.ApiClient(configuration))
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institutions_using_get**
> list[Institution] get_institutions_using_get()

Retrieves the list of institutions available in Yapily

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
api_instance = yapily.InstitutionsApi(yapily.ApiClient(configuration))

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

[**list[Institution]**](Institution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

