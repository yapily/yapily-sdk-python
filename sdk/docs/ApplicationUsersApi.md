# yapily.ApplicationUsersApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_using_post**](ApplicationUsersApi.md#add_user_using_post) | **POST** /users | Add an application user
[**delete_user_using_delete**](ApplicationUsersApi.md#delete_user_using_delete) | **DELETE** /users/{userUuid} | Delete an application user
[**get_user_using_get**](ApplicationUsersApi.md#get_user_using_get) | **GET** /users/{userUuid} | Get an application user
[**get_users_using_get**](ApplicationUsersApi.md#get_users_using_get) | **GET** /users | Get application users


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
> object delete_user_using_delete(user_uuid)

Delete an application user

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
    # Delete an application user
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

**object**

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
> list[ApplicationUser] get_users_using_get()

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

try:
    # Get application users
    api_response = api_instance.get_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->get_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApplicationUser]**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

