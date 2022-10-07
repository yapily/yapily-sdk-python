# yapily.PaymentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_payment**](PaymentsApi.md#create_bulk_payment) | **POST** /bulk-payments | Create Bulk Payment
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /payments | Create Payment
[**get_payments**](PaymentsApi.md#get_payments) | **GET** /payments/{paymentId}/details | Get Payment Details


# **create_bulk_payment**
> ApiResponseOfPaymentResponse create_bulk_payment(consent, bulk_payment_request)

Create Bulk Payment

Used to initiate a bulk payment after obtaining the user's authorisation. <br><br>Feature: `CREATE_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import payments_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.api_response_of_payment_response import ApiResponseOfPaymentResponse
from yapily.model.bulk_payment_request import BulkPaymentRequest
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
    api_instance = payments_api.PaymentsApi(api_client)
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    bulk_payment_request = BulkPaymentRequest(
        payments=[
            PaymentRequest(
                payment_idempotency_id="04ab4536gaerfc0e1f93c4f4",
                payer=Payer(
                    name="John Doe",
                    account_identifications=[
                        AccountIdentification(
                            type=AccountIdentificationType("SORT_CODE"),
                            identification="401016",
                        ),
                    ],
                    address=Address(
                        address_lines=["Ardenham Court"],
                        street_name="Oxford Road",
                        building_number="45",
                        post_code="HP19 3EQ",
                        town_name="Aylesbury",
                        county=["Buckinghamshire"],
                        country="GB",
                        department="Unit 2",
                        sub_department="Floor 3",
                        address_type=AddressTypeEnum("BUSINESS"),
                    ),
                ),
                reference="Bill payment",
                context_type=PaymentContextType("OTHER"),
                type=PaymentType("DOMESTIC_PAYMENT"),
                payee=Payee(
                    name="Jane Doe",
                    account_identifications=[
                        AccountIdentification(
                            type=AccountIdentificationType("SORT_CODE"),
                            identification="401016",
                        ),
                    ],
                    address=Address(
                        address_lines=["Ardenham Court"],
                        street_name="Oxford Road",
                        building_number="45",
                        post_code="HP19 3EQ",
                        town_name="Aylesbury",
                        county=["Buckinghamshire"],
                        country="GB",
                        department="Unit 2",
                        sub_department="Floor 3",
                        address_type=AddressTypeEnum("BUSINESS"),
                    ),
                    merchant_id="24589303",
                    merchant_category_code="5551",
                ),
                periodic_payment=PeriodicPaymentRequest(
                    frequency=FrequencyRequest(
                        type=FrequencyEnumExtended("DAILY"),
                        interval_week=1,
                        interval_month=1,
                        execution_day=1,
                    ),
                    number_of_payments=5,
                    next_payment_date_time=dateutil_parser('2018-01-10T00:00:00Z'),
                    next_payment_amount=Amount(
                        amount=10,
                        currency="GBP",
                    ),
                    final_payment_date_time=dateutil_parser('2030-01-10T00:00:00Z'),
                    final_payment_amount=Amount(
                        amount=10,
                        currency="GBP",
                    ),
                ),
                international_payment=InternationalPaymentRequest(
                    currency_of_transfer="currency_of_transfer_example",
                    exchange_rate_information=ExchangeRateInformation(
                        unit_currency="unit_currency_example",
                        rate=3.14,
                        rate_type=RateTypeEnum("ACTUAL"),
                        foreign_exchange_contract_reference="foreign_exchange_contract_reference_example",
                    ),
                    purpose="purpose_example",
                    priority=PriorityCodeEnum("NORMAL"),
                    charge_bearer=ChargeBearerType("DEBT"),
                ),
                amount=Amount(
                    amount=10,
                    currency="GBP",
                ),
                payment_date_time=dateutil_parser('2021-07-21T17:32:28Z'),
                read_refund_account=False,
            ),
        ],
        originator_identification_number="originator_identification_number_example",
        execution_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # BulkPaymentRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Bulk Payment
        api_response = api_instance.create_bulk_payment(consent, bulk_payment_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Bulk Payment
        api_response = api_instance.create_bulk_payment(consent, bulk_payment_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->create_bulk_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **bulk_payment_request** | [**BulkPaymentRequest**](BulkPaymentRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **create_payment**
> ApiResponseOfPaymentResponse create_payment(consent, payment_request)

Create Payment

Used to initiate a payment after obtaining the user's authorisation. <br><br>Features:<ul><li>`INITIATE_DOMESTIC_PERIODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYMENT`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import payments_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.payment_request import PaymentRequest
from yapily.model.api_response_of_payment_response import ApiResponseOfPaymentResponse
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
    api_instance = payments_api.PaymentsApi(api_client)
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    payment_request = PaymentRequest(
        payment_idempotency_id="04ab4536gaerfc0e1f93c4f4",
        payer=Payer(
            name="John Doe",
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ],
            address=Address(
                address_lines=["Ardenham Court"],
                street_name="Oxford Road",
                building_number="45",
                post_code="HP19 3EQ",
                town_name="Aylesbury",
                county=["Buckinghamshire"],
                country="GB",
                department="Unit 2",
                sub_department="Floor 3",
                address_type=AddressTypeEnum("BUSINESS"),
            ),
        ),
        reference="Bill payment",
        context_type=PaymentContextType("OTHER"),
        type=PaymentType("DOMESTIC_PAYMENT"),
        payee=Payee(
            name="Jane Doe",
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ],
            address=Address(
                address_lines=["Ardenham Court"],
                street_name="Oxford Road",
                building_number="45",
                post_code="HP19 3EQ",
                town_name="Aylesbury",
                county=["Buckinghamshire"],
                country="GB",
                department="Unit 2",
                sub_department="Floor 3",
                address_type=AddressTypeEnum("BUSINESS"),
            ),
            merchant_id="24589303",
            merchant_category_code="5551",
        ),
        periodic_payment=PeriodicPaymentRequest(
            frequency=FrequencyRequest(
                type=FrequencyEnumExtended("DAILY"),
                interval_week=1,
                interval_month=1,
                execution_day=1,
            ),
            number_of_payments=5,
            next_payment_date_time=dateutil_parser('2018-01-10T00:00:00Z'),
            next_payment_amount=Amount(
                amount=10,
                currency="GBP",
            ),
            final_payment_date_time=dateutil_parser('2030-01-10T00:00:00Z'),
            final_payment_amount=Amount(
                amount=10,
                currency="GBP",
            ),
        ),
        international_payment=InternationalPaymentRequest(
            currency_of_transfer="currency_of_transfer_example",
            exchange_rate_information=ExchangeRateInformation(
                unit_currency="unit_currency_example",
                rate=3.14,
                rate_type=RateTypeEnum("ACTUAL"),
                foreign_exchange_contract_reference="foreign_exchange_contract_reference_example",
            ),
            purpose="purpose_example",
            priority=PriorityCodeEnum("NORMAL"),
            charge_bearer=ChargeBearerType("DEBT"),
        ),
        amount=Amount(
            amount=10,
            currency="GBP",
        ),
        payment_date_time=dateutil_parser('2021-07-21T17:32:28Z'),
        read_refund_account=False,
    ) # PaymentRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment
        api_response = api_instance.create_payment(consent, payment_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment
        api_response = api_instance.create_payment(consent, payment_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **payment_request** | [**PaymentRequest**](PaymentRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentResponse**](ApiResponseOfPaymentResponse.md)

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

# **get_payments**
> ApiResponseOfPaymentResponses get_payments(payment_id, consent)

Get Payment Details

Used to get the payment details of a payment. This is most commonly used to check for any updates to the payment status. <br><br>Feature: `EXISTING_PAYMENTS_DETAILS`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import payments_api
from yapily.model.api_response_error import ApiResponseError
from yapily.model.api_response_of_payment_responses import ApiResponseOfPaymentResponses
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
    api_instance = payments_api.PaymentsApi(api_client)
    payment_id = "paymentId_example" # str | __Mandatory__. The payment Id of the payment.
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payment Details
        api_response = api_instance.get_payments(payment_id, consent)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->get_payments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payment Details
        api_response = api_instance.get_payments(payment_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling PaymentsApi->get_payments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| __Mandatory__. The payment Id of the payment. |
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentResponses**](ApiResponseOfPaymentResponses.md)

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

