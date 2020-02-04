# yapily.ApplicationUsersApi

All URIs are relative to *https://api.yapily.com*

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
> ApplicationUser add_user_using_post(new_application_user)

Add an application user

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
new_application_user = yapily.NewApplicationUser() # NewApplicationUser | newApplicationUser

try:
    # Add an application user
    api_response = api_instance.add_user_using_post(new_application_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->add_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_application_user** | [**NewApplicationUser**](NewApplicationUser.md)| newApplicationUser | 

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> ApiResponseOfUserDeleteResponse delete_user_using_delete(user_uuid)

Delete an application user and sub-resources (including consent resources on institution APIs if they exist)

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | userUuid

try:
    # Delete an application user and sub-resources (including consent resources on institution APIs if they exist)
    api_response = api_instance.delete_user_using_delete(user_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| userUuid | 

### Return type

[**ApiResponseOfUserDeleteResponse**](ApiResponseOfUserDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delete_users_job_using_get**
> ApiResponseOfBulkUserDeleteDetails get_delete_users_job_using_get(job_id)

Get details of a user deletion job

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delete_users_jobs_using_get**
> ApiListResponseOfBulkUserDelete get_delete_users_jobs_using_get()

Get details of all user deletion jobs

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))

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

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> ApplicationUser get_user_using_get(user_uuid)

Get an application user

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | userUuid

try:
    # Get an application user
    api_response = api_instance.get_user_using_get(user_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| userUuid | 

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_using_get**
> list[ApplicationUser] get_users_using_get(filter_application_user_id=filter_application_user_id)

Get application users

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
filter_application_user_id = ['filter_application_user_id_example'] # list[str] | Filter users by the provided application user Id (applicationUserId) when the user was created. (optional)

try:
    # Get application users
    api_response = api_instance.get_users_using_get(filter_application_user_id=filter_application_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->get_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application_user_id** | [**list[str]**](str.md)| Filter users by the provided application user Id (applicationUserId) when the user was created. | [optional] 

### Return type

[**list[ApplicationUser]**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_delete_users_job_using_post**
> ApiResponseOfBulkUserDeleteDetails start_delete_users_job_using_post(user_delete_request)

Start a job to delete application users by specifying their identifiers

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

