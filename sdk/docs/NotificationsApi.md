# yapily.NotificationsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_subscription**](NotificationsApi.md#create_event_subscription) | **POST** /notifications/event-subscriptions | Create Event Subscription
[**delete_event_subscription_by_id**](NotificationsApi.md#delete_event_subscription_by_id) | **DELETE** /notifications/event-subscriptions/{eventTypeId} | Delete Event Subscription
[**get_event_subscription_by_id**](NotificationsApi.md#get_event_subscription_by_id) | **GET** /notifications/event-subscriptions/{eventTypeId} | Get Event Subscription
[**get_event_subscriptions**](NotificationsApi.md#get_event_subscriptions) | **GET** /notifications/event-subscriptions | Get Event Subscriptions


# **create_event_subscription**
> ApiResponseOfEventSubscriptionResponse create_event_subscription(event_subscription_request)

Create Event Subscription

Used to subscribe to notifications relating to a specified event type.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import notifications_api
from yapily.model.event_subscription_request import EventSubscriptionRequest
from yapily.model.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
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
    api_instance = notifications_api.NotificationsApi(api_client)
    event_subscription_request = EventSubscriptionRequest(
        event_type_id="payment.status.completed",
        notification=Notification(
            type="WEBHOOK",
            url="https://httpbin.com/new_endpoint",
        ),
    ) # EventSubscriptionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Event Subscription
        api_response = api_instance.create_event_subscription(event_subscription_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling NotificationsApi->create_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_request** | [**EventSubscriptionRequest**](EventSubscriptionRequest.md)|  |

### Return type

[**ApiResponseOfEventSubscriptionResponse**](ApiResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event subscription created successfully |  -  |
**400** | Bad request for missing required properties |  -  |
**401** | Unauthorized |  -  |
**409** | Event subscription already exist for the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_subscription_by_id**
> ApiResponseOfEventSubscriptionDeleteResponse delete_event_subscription_by_id(event_type_id)

Delete Event Subscription

Used to unsubscribe to notifications relating to a specified event type.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import notifications_api
from yapily.model.api_response_of_event_subscription_delete_response import ApiResponseOfEventSubscriptionDeleteResponse
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
    api_instance = notifications_api.NotificationsApi(api_client)
    event_type_id = "eventTypeId_example" # str | Unique identifier of the event type (for which notifications will be sent)

    # example passing only required values which don't have defaults set
    try:
        # Delete Event Subscription
        api_response = api_instance.delete_event_subscription_by_id(event_type_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling NotificationsApi->delete_event_subscription_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **str**| Unique identifier of the event type (for which notifications will be sent) |

### Return type

[**ApiResponseOfEventSubscriptionDeleteResponse**](ApiResponseOfEventSubscriptionDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscription deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Event subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_subscription_by_id**
> ApiResponseOfEventSubscriptionResponse get_event_subscription_by_id(event_type_id)

Get Event Subscription

Used to get details of your subscription to a specified event type.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import notifications_api
from yapily.model.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
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
    api_instance = notifications_api.NotificationsApi(api_client)
    event_type_id = "eventTypeId_example" # str | Unique identifier of the event type (for which notifications will be sent)

    # example passing only required values which don't have defaults set
    try:
        # Get Event Subscription
        api_response = api_instance.get_event_subscription_by_id(event_type_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling NotificationsApi->get_event_subscription_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **str**| Unique identifier of the event type (for which notifications will be sent) |

### Return type

[**ApiResponseOfEventSubscriptionResponse**](ApiResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscription data found |  -  |
**401** | Unauthorized |  -  |
**404** | Event subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_subscriptions**
> ApiListResponseOfEventSubscriptionResponse get_event_subscriptions()

Get Event Subscriptions

Get all event subscriptions that your application is subscribed to

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import notifications_api
from yapily.model.api_list_response_of_event_subscription_response import ApiListResponseOfEventSubscriptionResponse
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
    api_instance = notifications_api.NotificationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Event Subscriptions
        api_response = api_instance.get_event_subscriptions()
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling NotificationsApi->get_event_subscriptions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfEventSubscriptionResponse**](ApiListResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscriptions for the application |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

