# yapily.UsersApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /users | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{userUuid} | Delete User
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userUuid} | Get User
[**get_users**](UsersApi.md#get_users) | **GET** /users | Get Users


# **add_user**
> ApplicationUser add_user(new_application_user)

Create User

Create a new user in your application

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import users_api
from yapily.model.application_user import ApplicationUser
from yapily.model.new_application_user import NewApplicationUser
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
    api_instance = users_api.UsersApi(api_client)
    new_application_user = NewApplicationUser(
        application_user_id="user-234562290",
        reference_id="reference_id_example",
    ) # NewApplicationUser | 

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.add_user(new_application_user)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling UsersApi->add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_application_user** | [**NewApplicationUser**](NewApplicationUser.md)|  |

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> ApiResponseOfUserDeleteResponse delete_user(user_uuid)

Delete User

Delete a user from your application along with any sub-resources (including consent resources on institution APIs if they exist)

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import users_api
from yapily.model.api_response_of_user_delete_response import ApiResponseOfUserDeleteResponse
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
    api_instance = users_api.UsersApi(api_client)
    user_uuid = "userUuid_example" # str | __Mandatory__. The Yapily generated UUID for the user.

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_response = api_instance.delete_user(user_uuid)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. |

### Return type

[**ApiResponseOfUserDeleteResponse**](ApiResponseOfUserDeleteResponse.md)

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

# **get_user**
> ApplicationUser get_user(user_uuid)

Get User

Get a specific user using the user UUID

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import users_api
from yapily.model.application_user import ApplicationUser
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
    api_instance = users_api.UsersApi(api_client)
    user_uuid = "userUuid_example" # str | __Mandatory__. The Yapily generated UUID for the user.

    # example passing only required values which don't have defaults set
    try:
        # Get User
        api_response = api_instance.get_user(user_uuid)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. |

### Return type

[**ApplicationUser**](ApplicationUser.md)

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

# **get_users**
> [ApplicationUser] get_users()

Get Users

Get all the users configured in your application

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import users_api
from yapily.model.application_user import ApplicationUser
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
    api_instance = users_api.UsersApi(api_client)
    filter_application_user_id = [
        "filter[applicationUserId]_example",
    ] # [str] | __Optional__. Filter records based on the list of `applicationUserId` users provided. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Users
        api_response = api_instance.get_users(filter_application_user_id=filter_application_user_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application_user_id** | **[str]**| __Optional__. Filter records based on the list of &#x60;applicationUserId&#x60; users provided. | [optional]

### Return type

[**[ApplicationUser]**](ApplicationUser.md)

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

