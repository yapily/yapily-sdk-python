# yapily.StatementsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statement_file_using_get**](StatementsApi.md#get_statement_file_using_get) | **GET** /accounts/{accountId}/statements/{statementId}/file | Get account statement file
[**get_statement_using_get**](StatementsApi.md#get_statement_using_get) | **GET** /accounts/{accountId}/statements/{statementId} | Get account statement
[**get_statements_using_get**](StatementsApi.md#get_statements_using_get) | **GET** /accounts/{accountId}/statements | Get account statements


# **get_statement_file_using_get**
> str get_statement_file_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)

Get account statement file

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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get account statement file
        api_response = api_instance.get_statement_file_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statement_file_using_get: %s\n" % e)
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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get account statement file
        api_response = api_instance.get_statement_file_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statement_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **statement_id** | **str**| __Mandatory__. The statement Id of the statement file. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_using_get**
> ApiResponseOfAccountStatement get_statement_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)

Get account statement

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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get account statement
        api_response = api_instance.get_statement_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statement_using_get: %s\n" % e)
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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get account statement
        api_response = api_instance.get_statement_using_get(consent, account_id, statement_id, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statement_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **statement_id** | **str**| __Mandatory__. The statement Id of the statement file. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

[**ApiResponseOfAccountStatement**](ApiResponseOfAccountStatement.md)

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

# **get_statements_using_get**
> ApiListResponseOfAccountStatement get_statements_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, _from=_from, before=before, limit=limit, sort=sort, offset=offset)

Get account statements

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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
_from = '_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. (optional)
sort = 'sort_example' # str | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)

    try:
        # Get account statements
        api_response = api_instance.get_statements_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, _from=_from, before=before, limit=limit, sort=sort, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statements_using_get: %s\n" % e)
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
    api_instance = yapily.StatementsApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
_from = '_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. (optional)
sort = 'sort_example' # str | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)

    try:
        # Get account statements
        api_response = api_instance.get_statements_using_get(consent, account_id, x_yapily_api_version=x_yapily_api_version, _from=_from, before=before, limit=limit, sort=sort, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statements_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 
 **_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000. | [optional] 
 **sort** | **str**| __Optional__. Sort transaction records by date ascending with &#39;date&#39; or descending with &#39;-date&#39;. The default sort order is descending | [optional] 
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] 

### Return type

[**ApiListResponseOfAccountStatement**](ApiListResponseOfAccountStatement.md)

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

