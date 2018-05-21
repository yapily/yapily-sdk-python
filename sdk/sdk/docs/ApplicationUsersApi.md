# yapily.ApplicationUsersApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_using_post**](ApplicationUsersApi.md#add_user_using_post) | **POST** /users | Add an application user
[**get_user_using_get**](ApplicationUsersApi.md#get_user_using_get) | **GET** /users/{uuid} | Get an application user
[**get_users_using_get**](ApplicationUsersApi.md#get_users_using_get) | **GET** /users | Get application users
[**update_user_using_put**](ApplicationUsersApi.md#update_user_using_put) | **PUT** /users/{uuid} | Update an application user


# **add_user_using_post**
> ApplicationUser add_user_using_post(application_user)

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

# create an instance of the API class
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
application_user = yapily.ApplicationUser() # ApplicationUser | applicationUser

try:
    # Add an application user
    api_response = api_instance.add_user_using_post(application_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->add_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_user** | [**ApplicationUser**](ApplicationUser.md)| applicationUser | 

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> ApplicationUser get_user_using_get(uuid)

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

# create an instance of the API class
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
uuid = 'uuid_example' # str | uuid

try:
    # Get an application user
    api_response = api_instance.get_user_using_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| uuid | 

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_put**
> ApplicationUser update_user_using_put(uuid, application_user)

Update an application user

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
api_instance = yapily.ApplicationUsersApi(yapily.ApiClient(configuration))
uuid = 'uuid_example' # str | uuid
application_user = yapily.ApplicationUser() # ApplicationUser | applicationUser

try:
    # Update an application user
    api_response = api_instance.update_user_using_put(uuid, application_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationUsersApi->update_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| uuid | 
 **application_user** | [**ApplicationUser**](ApplicationUser.md)| applicationUser | 

### Return type

[**ApplicationUser**](ApplicationUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

