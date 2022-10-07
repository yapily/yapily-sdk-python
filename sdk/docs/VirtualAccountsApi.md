# yapily.VirtualAccountsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account**](VirtualAccountsApi.md#create_virtual_account) | **POST** /virtual-accounts/accounts | Create Account
[**create_virtual_account_beneficiary**](VirtualAccountsApi.md#create_virtual_account_beneficiary) | **POST** /virtual-accounts/beneficiaries | Create Beneficiary
[**create_virtual_account_client**](VirtualAccountsApi.md#create_virtual_account_client) | **POST** /virtual-accounts/clients | Create Virtual Account Client
[**create_virtual_account_pay_out**](VirtualAccountsApi.md#create_virtual_account_pay_out) | **POST** /virtual-accounts/payments/pay-outs | Create Pay Out
[**create_virtual_account_transfer**](VirtualAccountsApi.md#create_virtual_account_transfer) | **POST** /virtual-accounts/payments/transfers | Create Virtual Account Transfer
[**get_pay_in_details**](VirtualAccountsApi.md#get_pay_in_details) | **GET** /virtual-accounts/payments/{paymentId}/pay-in-details | Get Pay-In Details
[**get_payments_by_id**](VirtualAccountsApi.md#get_payments_by_id) | **GET** /virtual-accounts/payments/{id} | Get Payment
[**get_virtual_account_beneficiaries**](VirtualAccountsApi.md#get_virtual_account_beneficiaries) | **GET** /virtual-accounts/beneficiaries | Get List Of Beneficiaries
[**get_virtual_account_beneficiary**](VirtualAccountsApi.md#get_virtual_account_beneficiary) | **GET** /virtual-accounts/beneficiaries/{beneficiaryId} | Get Beneficiary
[**get_virtual_account_by_id**](VirtualAccountsApi.md#get_virtual_account_by_id) | **GET** /virtual-accounts/accounts/{accountId} | Get Account
[**get_virtual_account_clients**](VirtualAccountsApi.md#get_virtual_account_clients) | **GET** /virtual-accounts/clients | Get List of Virtual Account Clients
[**get_virtual_account_payments**](VirtualAccountsApi.md#get_virtual_account_payments) | **GET** /virtual-accounts/payments | Get Payments
[**get_virtual_accounts**](VirtualAccountsApi.md#get_virtual_accounts) | **GET** /virtual-accounts/accounts | Get Accounts
[**update_virtual_account_by_id**](VirtualAccountsApi.md#update_virtual_account_by_id) | **PATCH** /virtual-accounts/accounts/{accountId} | Update Account


# **create_virtual_account**
> ApiResponseOfVirtualAccount create_virtual_account(client_id, virtual_account_request)

Create Account

Create a new virtual account

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.model.virtual_account_request import VirtualAccountRequest
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    virtual_account_request = VirtualAccountRequest(
        nickname="MyAccount123",
        currency="GBP",
    ) # VirtualAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Account
        api_response = api_instance.create_virtual_account(client_id, virtual_account_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->create_virtual_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **virtual_account_request** | [**VirtualAccountRequest**](VirtualAccountRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_account_beneficiary**
> ApiResponseOfVirtualAccountBeneficiary create_virtual_account_beneficiary(client_id, virtual_account_beneficiary_request)

Create Beneficiary

Create a new beneficiary (individual or business account) to which a Pay Out can be made. The beneficiary can be used from any virtual account that is held

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account_beneficiary import ApiResponseOfVirtualAccountBeneficiary
from yapily.model.virtual_account_beneficiary_request import VirtualAccountBeneficiaryRequest
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    virtual_account_beneficiary_request = VirtualAccountBeneficiaryRequest(
        nickname="MyBeneficiary123",
        type="INDIVIDUAL",
        name="Mr Jack Williams",
        birth_date=dateutil_parser('Fri Oct 04 00:00:00 UTC 2019').date(),
        payment_schemes=[
            "payment_schemes_example",
        ],
        address=VirtualAccountBeneficiaryAddress(
            address_line="12 New Street",
            town_name="London",
            post_code="NE15 PLZ",
            country="GB",
        ),
        account=VirtualAccountBeneficiaryAccount(
            currency="GBP",
            bank_name="Lloyds Bank",
            bank_address="WE12 ABC",
            bank_country="GB",
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ],
        ),
    ) # VirtualAccountBeneficiaryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Beneficiary
        api_response = api_instance.create_virtual_account_beneficiary(client_id, virtual_account_beneficiary_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->create_virtual_account_beneficiary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **virtual_account_beneficiary_request** | [**VirtualAccountBeneficiaryRequest**](VirtualAccountBeneficiaryRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccountBeneficiary**](ApiResponseOfVirtualAccountBeneficiary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_account_client**
> ApiResponseOfVirtualAccountClient create_virtual_account_client(client_id, virtual_account_client_request)

Create Virtual Account Client

Create a new virtual account client (individual or business client). Available for clients who have direct onboarding permissions only. Please contact your CSM to enquire about access

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_error_response import ApiErrorResponse
from yapily.model.api_response_of_virtual_account_client import ApiResponseOfVirtualAccountClient
from yapily.model.virtual_account_client_request import VirtualAccountClientRequest
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. This must be your master / parent client-id (and not one associated with one of your clients)
    virtual_account_client_request = VirtualAccountClientRequest(
        type=VirtualAccountClientType("INDIVIDUAL"),
        individual=VirtualAccountIndividualClient(
            first_name="first_name_example",
            middle_name="middle_name_example",
            last_name="last_name_example",
            address=VirtualAccountAddress(
                address_line1="12 New Street",
                address_line2="Barcelona CA 08005",
                town_name="Barcelona ",
                post_code="08005",
                country="ES",
            ),
            birth_date=dateutil_parser('1970-01-01').date(),
            email="email_example",
            phone="phone_example",
        ),
        business=VirtualAccountBusinessClient(
            name="name_example",
            type=VirtualAccountClientBusinessType("SOLE_TRADER"),
            registration_number="registration_number_example",
            registered_address=VirtualAccountAddress(
                address_line1="12 New Street",
                address_line2="Barcelona CA 08005",
                town_name="Barcelona ",
                post_code="08005",
                country="ES",
            ),
            trading_address=VirtualAccountAddress(
                address_line1="12 New Street",
                address_line2="Barcelona CA 08005",
                town_name="Barcelona ",
                post_code="08005",
                country="ES",
            ),
            contact_name="contact_name_example",
            email="email_example",
            phone="phone_example",
        ),
    ) # VirtualAccountClientRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Virtual Account Client
        api_response = api_instance.create_virtual_account_client(client_id, virtual_account_client_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->create_virtual_account_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. This must be your master / parent client-id (and not one associated with one of your clients) |
 **virtual_account_client_request** | [**VirtualAccountClientRequest**](VirtualAccountClientRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccountClient**](ApiResponseOfVirtualAccountClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_account_pay_out**
> ApiResponseOfVirtualAccountPayment create_virtual_account_pay_out(idempotency_key, client_id, virtual_account_pay_out_request)

Create Pay Out

Initiate a payment from a specified virtual account to a previously added beneficiary using any of the schemes that it supports <br> When subscribed to virtualAccount.payOut.status notifications, further updates on payment processing status will be develivered asynchronously 

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.model.virtual_account_pay_out_request import VirtualAccountPayOutRequest
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    idempotency_key = "a346fe67-1d81-4ccd-8409-bf9d6c07980f" # str | Uniquely identifies a request, such that requests made with a same value are considered retries <br> We recommend that a v4 UUID is supplied 
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    virtual_account_pay_out_request = VirtualAccountPayOutRequest(
        account_id="eb2ad083-a111-4143-8756-a3a3cef4031c",
        amount=None,
        reference="Invoice 1267765",
        beneficiary_id="sd6ad034-a111-4143-8756-a3a3cef4045v",
        payment_scheme="FASTER_PAYMENTS",
        payment_date=dateutil_parser('Tue Oct 04 00:00:00 UTC 2022').date(),
    ) # VirtualAccountPayOutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Pay Out
        api_response = api_instance.create_virtual_account_pay_out(idempotency_key, client_id, virtual_account_pay_out_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->create_virtual_account_pay_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Uniquely identifies a request, such that requests made with a same value are considered retries &lt;br&gt; We recommend that a v4 UUID is supplied  |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **virtual_account_pay_out_request** | [**VirtualAccountPayOutRequest**](VirtualAccountPayOutRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_account_transfer**
> ApiResponseOfVirtualAccountPayment create_virtual_account_transfer(idempotency_key, client_id, virtual_account_transfer_request)

Create Virtual Account Transfer

Create a transfer between two virtual accounts

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.virtual_account_transfer_request import VirtualAccountTransferRequest
from yapily.model.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    idempotency_key = "a346fe67-1d81-4ccd-8409-bf9d6c07980f" # str | Uniquely identifies a request, such that requests made with a same value are considered retries <br> We recommend that a v4 UUID is supplied 
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    virtual_account_transfer_request = VirtualAccountTransferRequest(
        amount=None,
        reference="Ref 86543",
        source=VirtualAccountTransferSource(
            account_id="eb2ad083-a111-4143-8756-a3a3cef4031c",
        ),
        destination=VirtualAccountTransferDestination(
            account_id="eb2ad083-a111-4143-8756-a3a3cef4031c",
        ),
    ) # VirtualAccountTransferRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Virtual Account Transfer
        api_response = api_instance.create_virtual_account_transfer(idempotency_key, client_id, virtual_account_transfer_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->create_virtual_account_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Uniquely identifies a request, such that requests made with a same value are considered retries &lt;br&gt; We recommend that a v4 UUID is supplied  |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **virtual_account_transfer_request** | [**VirtualAccountTransferRequest**](VirtualAccountTransferRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_in_details**
> ApiResponseOfVirtualAccountPayInDetails get_pay_in_details(payment_id)

Get Pay-In Details

Get the details of a pay-in transaction

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account_pay_in_details import ApiResponseOfVirtualAccountPayInDetails
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    payment_id = "8b66abb5-5412-4454-aa7b-4e693ada6321" # str | Uniquely identifies a transaction

    # example passing only required values which don't have defaults set
    try:
        # Get Pay-In Details
        api_response = api_instance.get_pay_in_details(payment_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_pay_in_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Uniquely identifies a transaction |

### Return type

[**ApiResponseOfVirtualAccountPayInDetails**](ApiResponseOfVirtualAccountPayInDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Requested beneficiary is not found. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_by_id**
> ApiResponseOfVirtualAccountPayment get_payments_by_id(id, client_id)

Get Payment

Get the details of a specific payment using its Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    id = "id_example" # str | __Mandatory__. The id of the payment
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done

    # example passing only required values which don't have defaults set
    try:
        # Get Payment
        api_response = api_instance.get_payments_by_id(id, client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_payments_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| __Mandatory__. The id of the payment |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Requested payment is not found. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_beneficiaries**
> ApiListResponseOfVirtualAccountBeneficiary get_virtual_account_beneficiaries(client_id)

Get List Of Beneficiaries

Gets the list of beneficiaries (individual or business account) to which a Pay Out can be made.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_list_response_of_virtual_account_beneficiary import ApiListResponseOfVirtualAccountBeneficiary
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    cursor = "cursor_example" # str | __Optional__. Data required to provide pagination (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get List Of Beneficiaries
        api_response = api_instance.get_virtual_account_beneficiaries(client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_beneficiaries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get List Of Beneficiaries
        api_response = api_instance.get_virtual_account_beneficiaries(client_id, cursor=cursor)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_beneficiaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional]

### Return type

[**ApiListResponseOfVirtualAccountBeneficiary**](ApiListResponseOfVirtualAccountBeneficiary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_beneficiary**
> ApiResponseOfVirtualAccountBeneficiary get_virtual_account_beneficiary(beneficiary_id, client_id)

Get Beneficiary

Get the details of a specific beneficiary (individual or business account) to which a Pay Out can be made from its id.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account_beneficiary import ApiResponseOfVirtualAccountBeneficiary
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    beneficiary_id = "beneficiaryId_example" # str | __Mandatory__. The Id of the requested beneficiary.
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done

    # example passing only required values which don't have defaults set
    try:
        # Get Beneficiary
        api_response = api_instance.get_virtual_account_beneficiary(beneficiary_id, client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_beneficiary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_id** | **str**| __Mandatory__. The Id of the requested beneficiary. |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |

### Return type

[**ApiResponseOfVirtualAccountBeneficiary**](ApiResponseOfVirtualAccountBeneficiary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Requested beneficiary is not found. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_by_id**
> ApiResponseOfVirtualAccount get_virtual_account_by_id(account_id, client_id)

Get Account

Get the details of a specific account using its Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    account_id = "accountId_example" # str | __Mandatory__. The Id of the account.
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done

    # example passing only required values which don't have defaults set
    try:
        # Get Account
        api_response = api_instance.get_virtual_account_by_id(account_id, client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The Id of the account. |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Resource requested is not found. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_clients**
> ApiListResponseOfVirtualAccountClient get_virtual_account_clients(client_id)

Get List of Virtual Account Clients

Get Virtual Account Clients (individual or business client).

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_list_response_of_virtual_account_client import ApiListResponseOfVirtualAccountClient
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. This must be your master / parent client-id (and not one associated with one of your clients)
    type = "BUSINESS" # str | __Optional__.  Filter clients based on client type. One of BUSINESS or INDIVIDUAL (optional)
    status = "ACTIVE" # str | __Optional__.  Filter clients based on client status. One of ACTIVE, PENDING or SUSPENDED (optional)
    cursor = "cursor_example" # str | __Optional__. Data required to provide pagination (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get List of Virtual Account Clients
        api_response = api_instance.get_virtual_account_clients(client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_clients: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get List of Virtual Account Clients
        api_response = api_instance.get_virtual_account_clients(client_id, type=type, status=status, cursor=cursor)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. This must be your master / parent client-id (and not one associated with one of your clients) |
 **type** | **str**| __Optional__.  Filter clients based on client type. One of BUSINESS or INDIVIDUAL | [optional]
 **status** | **str**| __Optional__.  Filter clients based on client status. One of ACTIVE, PENDING or SUSPENDED | [optional]
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional]

### Return type

[**ApiListResponseOfVirtualAccountClient**](ApiListResponseOfVirtualAccountClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_payments**
> ApiListResponseOfVirtualAccountPayment get_virtual_account_payments(client_id)

Get Payments

Retrieve a list of virtual account payments

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_error_response import ApiErrorResponse
from yapily.model.api_list_response_of_virtual_account_payment import ApiListResponseOfVirtualAccountPayment
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    account_id = "eb2ad083-a111-4143-8756-a3a3cef4031c" # str | __Optional__. Filter payments based on accountId (optional)
    created_date_time_from = dateutil_parser('2022-04-24T00:30:19.951Z') # datetime | __Optional__. Filter payments based on the createdDateTime (optional)
    created_date_time_to = dateutil_parser('2022-04-24T00:30:19.951Z') # datetime | __Optional__. Filter payments based on the createdDateTime (optional)
    status = ["INITIATED","COMPLETED"] # [str] | __Optional__. Filter payments based on the payment status. One of INITIATED, PROCESSING, COMPLETED, FAILED (optional)
    type = ["PAY_IN","PAY_OUT"] # [str] | __Optional__. Filter payments based on the payment type. One of PAY_IN, PAY_OUT, RETURN_IN, RETURN_OUT (optional)
    cursor = "cursor_example" # str | __Optional__. Data required to provide pagination (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payments
        api_response = api_instance.get_virtual_account_payments(client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_payments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payments
        api_response = api_instance.get_virtual_account_payments(client_id, account_id=account_id, created_date_time_from=created_date_time_from, created_date_time_to=created_date_time_to, status=status, type=type, cursor=cursor)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_account_payments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **account_id** | **str**| __Optional__. Filter payments based on accountId | [optional]
 **created_date_time_from** | **datetime**| __Optional__. Filter payments based on the createdDateTime | [optional]
 **created_date_time_to** | **datetime**| __Optional__. Filter payments based on the createdDateTime | [optional]
 **status** | **[str]**| __Optional__. Filter payments based on the payment status. One of INITIATED, PROCESSING, COMPLETED, FAILED | [optional]
 **type** | **[str]**| __Optional__. Filter payments based on the payment type. One of PAY_IN, PAY_OUT, RETURN_IN, RETURN_OUT | [optional]
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional]

### Return type

[**ApiListResponseOfVirtualAccountPayment**](ApiListResponseOfVirtualAccountPayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_accounts**
> ApiListResponseOfVirtualAccount get_virtual_accounts(client_id)

Get Accounts

Retrieve a list of all virtual accounts held

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_list_response_of_virtual_account import ApiListResponseOfVirtualAccount
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    nickname = "nickname_example" # str | __Optional__. Filter accounts based on reference provided in order to help with identification of the account (optional)
    currency = "AEI" # str | __Optional__. Filter accounts based on three-letter ISO 4217 currency code (optional)
    status = "status_example" # str | __Optional__. Filter accounts based on their current state. One of PENDING, ACTIVE, FAILED, SUSPENDED or CLOSED (optional)
    cursor = "cursor_example" # str | __Optional__. Data required to provide pagination (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Accounts
        api_response = api_instance.get_virtual_accounts(client_id)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Accounts
        api_response = api_instance.get_virtual_accounts(client_id, nickname=nickname, currency=currency, status=status, cursor=cursor)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->get_virtual_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **nickname** | **str**| __Optional__. Filter accounts based on reference provided in order to help with identification of the account | [optional]
 **currency** | **str**| __Optional__. Filter accounts based on three-letter ISO 4217 currency code | [optional]
 **status** | **str**| __Optional__. Filter accounts based on their current state. One of PENDING, ACTIVE, FAILED, SUSPENDED or CLOSED | [optional]
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional]

### Return type

[**ApiListResponseOfVirtualAccount**](ApiListResponseOfVirtualAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_account_by_id**
> ApiResponseOfVirtualAccount update_virtual_account_by_id(account_id, client_id, update_virtual_account_request)

Update Account

Update the details of a specific account using its Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import virtual_accounts_api
from yapily.model.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.model.update_virtual_account_request import UpdateVirtualAccountRequest
from yapily.model.api_error_response import ApiErrorResponse
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
    api_instance = virtual_accounts_api.VirtualAccountsApi(api_client)
    account_id = "accountId_example" # str | __Mandatory__. The Id of the account.
    client_id = "5a7294ab-6b7d-4681-835a-f9b9775c75db" # str | __Mandatory__. The customer or sub-customer id for which the request will be done
    update_virtual_account_request = UpdateVirtualAccountRequest(
        nickname="MyAccount123",
        status="CLOSED",
    ) # UpdateVirtualAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Account
        api_response = api_instance.update_virtual_account_by_id(account_id, client_id, update_virtual_account_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling VirtualAccountsApi->update_virtual_account_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The Id of the account. |
 **client_id** | **str**| __Mandatory__. The customer or sub-customer id for which the request will be done |
 **update_virtual_account_request** | [**UpdateVirtualAccountRequest**](UpdateVirtualAccountRequest.md)|  |

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Resource requested is not found. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

