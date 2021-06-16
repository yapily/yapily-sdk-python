# yapily.ApplicationUsersApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_using_post**](ApplicationUsersApi.md#add_user_using_post) | **POST** /users | Add an application user
[**delete_user_using_delete**](ApplicationUsersApi.md#delete_user_using_delete) | **DELETE** /users/{userUuid} | Delete an application user and sub-resources (including consent resources on institution APIs if they exist)
[**get_delete_users_job_using_get**](ApplicationUsersApi.md#get_delete_users_job_using_get) | **GET** /delete-users/{job-id} | Get details of a user deletion job
[**get_delete_users_jobs_using_get**](ApplicationUsersApi.md#get_delete_users_jobs_using_get) | **GET** /delete-users | Get details of all user deletion jobs
[**get_user_using_get**](ApplicationUsersApi.md#get_user_using_get) | **GET** /users/{userUuid} | Get an application user
[**get_users_using_get**](ApplicationUsersApi.md#get_users_using_get) | **GET** /users | Get application users
[**start_delete_users_job_using_post**](ApplicationUsersApi.md#start_delete_users_job_using_post) | **POST** /delete-users | Start a job to delete application users by specifying their identifiers


# **add_user_using_post**
> ApplicationUser add_user_using_post(new_application_user, x_yapily_api_version=x_yapily_api_version)

Add an application user

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    new_application_user = yapily.NewApplicationUser() # NewApplicationUser | newApplicationUser
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Add an application user
        api_response = api_instance.add_user_using_post(new_application_user, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->add_user_using_post: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    new_application_user = yapily.NewApplicationUser() # NewApplicationUser | newApplicationUser
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Add an application user
        api_response = api_instance.add_user_using_post(new_application_user, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->add_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_application_user** | [**NewApplicationUser**](NewApplicationUser.md)| newApplicationUser | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

[**ApplicationUser**](ApplicationUser.md)

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

# **delete_user_using_delete**
> ApiResponseOfUserDeleteResponse delete_user_using_delete(user_uuid, x_yapily_api_version=x_yapily_api_version)

Delete an application user and sub-resources (including consent resources on institution APIs if they exist)

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Delete an application user and sub-resources (including consent resources on institution APIs if they exist)
        api_response = api_instance.delete_user_using_delete(user_uuid, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->delete_user_using_delete: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Delete an application user and sub-resources (including consent resources on institution APIs if they exist)
        api_response = api_instance.delete_user_using_delete(user_uuid, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

[**ApiResponseOfUserDeleteResponse**](ApiResponseOfUserDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delete_users_job_using_get**
> ApiResponseOfBulkUserDeleteDetails get_delete_users_job_using_get(job_id)

Get details of a user deletion job

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    job_id = 'job_id_example' # str | job-id

    try:
        # Get details of a user deletion job
        api_response = api_instance.get_delete_users_job_using_get(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_delete_users_job_using_get: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    job_id = 'job_id_example' # str | job-id

    try:
        # Get details of a user deletion job
        api_response = api_instance.get_delete_users_job_using_get(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_delete_users_job_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| job-id | 

### Return type

[**ApiResponseOfBulkUserDeleteDetails**](ApiResponseOfBulkUserDeleteDetails.md)

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

# **get_delete_users_jobs_using_get**
> ApiListResponseOfBulkUserDelete get_delete_users_jobs_using_get()

Get details of all user deletion jobs

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    
    try:
        # Get details of all user deletion jobs
        api_response = api_instance.get_delete_users_jobs_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_delete_users_jobs_using_get: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    
    try:
        # Get details of all user deletion jobs
        api_response = api_instance.get_delete_users_jobs_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_delete_users_jobs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfBulkUserDelete**](ApiListResponseOfBulkUserDelete.md)

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

# **get_user_using_get**
> ApplicationUser get_user_using_get(user_uuid, x_yapily_api_version=x_yapily_api_version)

Get an application user

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get an application user
        api_response = api_instance.get_user_using_get(user_uuid, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_user_using_get: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)

    try:
        # Get an application user
        api_response = api_instance.get_user_using_get(user_uuid, x_yapily_api_version=x_yapily_api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 

### Return type

[**ApplicationUser**](ApplicationUser.md)

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

# **get_users_using_get**
> list[ApplicationUser] get_users_using_get(x_yapily_api_version=x_yapily_api_version, filter_application_user_id=filter_application_user_id)

Get application users

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
filter_application_user_id = ['filter_application_user_id_example'] # list[str] | __Optional__. Filter records based on the list of `applicationUserId` users provided. (optional)

    try:
        # Get application users
        api_response = api_instance.get_users_using_get(x_yapily_api_version=x_yapily_api_version, filter_application_user_id=filter_application_user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_users_using_get: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    x_yapily_api_version = 'x_yapily_api_version_example' # str | __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0` (optional)
filter_application_user_id = ['filter_application_user_id_example'] # list[str] | __Optional__. Filter records based on the list of `applicationUserId` users provided. (optional)

    try:
        # Get application users
        api_response = api_instance.get_users_using_get(x_yapily_api_version=x_yapily_api_version, filter_application_user_id=filter_application_user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->get_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_yapily_api_version** | **str**| __Optional__. Determines the API version to use. Valid values are &#x60;1.0&#x60; or &#x60;2.0-ALPHA&#x60;. Defaults to &#x60;1.0&#x60; | [optional] 
 **filter_application_user_id** | [**list[str]**](str.md)| __Optional__. Filter records based on the list of &#x60;applicationUserId&#x60; users provided. | [optional] 

### Return type

[**list[ApplicationUser]**](ApplicationUser.md)

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

# **start_delete_users_job_using_post**
> ApiResponseOfBulkUserDeleteDetails start_delete_users_job_using_post(user_delete_request)

Start a job to delete application users by specifying their identifiers

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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_delete_request = yapily.UserDeleteRequest() # UserDeleteRequest | userDeleteRequest

    try:
        # Start a job to delete application users by specifying their identifiers
        api_response = api_instance.start_delete_users_job_using_post(user_delete_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->start_delete_users_job_using_post: %s\n" % e)
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
    api_instance = yapily.ApplicationUsersApi(api_client)
    user_delete_request = yapily.UserDeleteRequest() # UserDeleteRequest | userDeleteRequest

    try:
        # Start a job to delete application users by specifying their identifiers
        api_response = api_instance.start_delete_users_job_using_post(user_delete_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationUsersApi->start_delete_users_job_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_delete_request** | [**UserDeleteRequest**](UserDeleteRequest.md)| userDeleteRequest | 

### Return type

[**ApiResponseOfBulkUserDeleteDetails**](ApiResponseOfBulkUserDeleteDetails.md)

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
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

