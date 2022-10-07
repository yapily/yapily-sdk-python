# yapily.AuthorisationsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_payment_authorisation**](AuthorisationsApi.md#create_bulk_payment_authorisation) | **POST** /bulk-payment-auth-requests | Create Bulk Payment Authorisation
[**create_embedded_bulk_payment_authorisation**](AuthorisationsApi.md#create_embedded_bulk_payment_authorisation) | **POST** /embedded-bulk-payment-auth-requests | Create Embedded Bulk Payment Authorisation
[**create_embedded_payment_authorisation**](AuthorisationsApi.md#create_embedded_payment_authorisation) | **POST** /embedded-payment-auth-requests | Create Embedded Payment Authorisation
[**create_payment_authorisation**](AuthorisationsApi.md#create_payment_authorisation) | **POST** /payment-auth-requests | Create Payment Authorisation
[**create_payment_pre_authorisation_request**](AuthorisationsApi.md#create_payment_pre_authorisation_request) | **POST** /payment-pre-auth-requests | Create Payment Pre-authorisation
[**create_pre_authorisation_request**](AuthorisationsApi.md#create_pre_authorisation_request) | **POST** /pre-auth-requests | Create Pre-authorisation
[**initiate_account_request**](AuthorisationsApi.md#initiate_account_request) | **POST** /account-auth-requests | Create Account Authorisation
[**initiate_embedded_account_request**](AuthorisationsApi.md#initiate_embedded_account_request) | **POST** /embedded-account-auth-requests | Create Embedded Account Authorisation
[**re_authorise_account**](AuthorisationsApi.md#re_authorise_account) | **PATCH** /account-auth-requests | Re-authorise Account Consent
[**update_embedded_account_request**](AuthorisationsApi.md#update_embedded_account_request) | **PUT** /embedded-account-auth-requests/{consentId} | Update Embedded Account Authorisation
[**update_embedded_bulk_payment_authorisation**](AuthorisationsApi.md#update_embedded_bulk_payment_authorisation) | **PUT** /embedded-bulk-payment-auth-requests/{consentId} | Update Embedded Bulk Payment Authorisation
[**update_embedded_payment_authorisation**](AuthorisationsApi.md#update_embedded_payment_authorisation) | **PUT** /embedded-payment-auth-requests/{consentId} | Update Embedded Payment Authorisation
[**update_payment_authorisation**](AuthorisationsApi.md#update_payment_authorisation) | **PUT** /payment-auth-requests | Update Payment Pre-authorisation
[**update_pre_authorise_account_consent**](AuthorisationsApi.md#update_pre_authorise_account_consent) | **PUT** /account-auth-requests | Update Account Pre-authorisation


# **create_bulk_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse create_bulk_payment_authorisation(bulk_payment_authorisation_request)

Create Bulk Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Redirect Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-flows/) for more information about this flow.<br><br>Feature: `INITIATE_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_payment_authorisation_request_response import ApiResponseOfPaymentAuthorisationRequestResponse
from yapily.model.api_response_error import ApiResponseError
from yapily.model.bulk_payment_authorisation_request import BulkPaymentAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    bulk_payment_authorisation_request = BulkPaymentAuthorisationRequest(
        user_uuid="e006a012-c306-4355-a6a1-99bf69ae5171",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=BulkPaymentRequest(
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
        ),
    ) # BulkPaymentAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Bulk Payment Authorisation
        api_response = api_instance.create_bulk_payment_authorisation(bulk_payment_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_bulk_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Bulk Payment Authorisation
        api_response = api_instance.create_bulk_payment_authorisation(bulk_payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_bulk_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_payment_authorisation_request** | [**BulkPaymentAuthorisationRequest**](BulkPaymentAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

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

# **create_embedded_bulk_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse create_embedded_bulk_payment_authorisation(bulk_payment_embedded_authorisation_request)

Create Embedded Bulk Payment Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_BULK_PAYMENT` feature in order to obtain the the user's authorisation for a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/bulk-payments/) for more information. <br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest
from yapily.model.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    bulk_payment_embedded_authorisation_request = BulkPaymentEmbeddedAuthorisationRequest(
        user_uuid="e006a012-c306-4355-a6a1-99bf69ae5171",
        application_user_id="user-234562290",
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=BulkPaymentRequest(
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
        ),
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
    ) # BulkPaymentEmbeddedAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Embedded Bulk Payment Authorisation
        api_response = api_instance.create_embedded_bulk_payment_authorisation(bulk_payment_embedded_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_bulk_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Embedded Bulk Payment Authorisation
        api_response = api_instance.create_embedded_bulk_payment_authorisation(bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_bulk_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_payment_embedded_authorisation_request** | [**BulkPaymentEmbeddedAuthorisationRequest**](BulkPaymentEmbeddedAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

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

# **create_embedded_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse create_embedded_payment_authorisation(payment_embedded_authorisation_request)

Create Embedded Payment Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.payment_embedded_authorisation_request import PaymentEmbeddedAuthorisationRequest
from yapily.model.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    payment_embedded_authorisation_request = PaymentEmbeddedAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=PaymentRequest(
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
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
    ) # PaymentEmbeddedAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Embedded Payment Authorisation
        api_response = api_instance.create_embedded_payment_authorisation(payment_embedded_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Embedded Payment Authorisation
        api_response = api_instance.create_embedded_payment_authorisation(payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_embedded_authorisation_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

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

# **create_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse create_payment_authorisation(payment_authorisation_request)

Create Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for a payment. This endpoint is used to initiate all the different payment listed below. Based on the type of payment you wish to make, you may be required to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/reference/#operation/createPaymentAuthorisation!path=paymentRequest&t=request). First make sure that the payment feature you wish to execute is supported by the bank by checking the features array in [GET Institution](https://docs.yapily.com/api/reference/#operation/getInstitution). <br><br>See [Redirect Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-flows/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PERIODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYMENT`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_payment_authorisation_request_response import ApiResponseOfPaymentAuthorisationRequestResponse
from yapily.model.payment_authorisation_request import PaymentAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    payment_authorisation_request = PaymentAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=PaymentRequest(
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
    ) # PaymentAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment Authorisation
        api_response = api_instance.create_payment_authorisation(payment_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment Authorisation
        api_response = api_instance.create_payment_authorisation(payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_authorisation_request** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

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

# **create_payment_pre_authorisation_request**
> ApiResponseOfAccountAuthorisationResponse create_payment_pre_authorisation_request(payment_pre_authorisation_request)

Create Payment Pre-authorisation

Used to initiate the pre-authorisation process for payments for CbiGlobe `Institution` that contains the `INITIATE_ONETIME_PRE_AUTHORISATION_PAYMENTS` feature to authenticate the user. <br><br>Feature: `INITIATE_ONETIME_PRE_AUTHORISATION_PAYMENTS`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
from yapily.model.payment_pre_authorisation_request import PaymentPreAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    payment_pre_authorisation_request = PaymentPreAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        scope="AIS",
        payee=PayeeDetails(
            name="Jane Doe",
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ],
            country="GB",
        ),
        payer=PayerDetails(
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ],
        ),
        amount=Amount(
            amount=10,
            currency="GBP",
        ),
        reference="Bill payment",
    ) # PaymentPreAuthorisationRequest | 
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment Pre-authorisation
        api_response = api_instance.create_payment_pre_authorisation_request(payment_pre_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_pre_authorisation_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment Pre-authorisation
        api_response = api_instance.create_payment_pre_authorisation_request(payment_pre_authorisation_request, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_pre_authorisation_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_pre_authorisation_request** | [**PaymentPreAuthorisationRequest**](PaymentPreAuthorisationRequest.md)|  |
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfAccountAuthorisationResponse**](ApiResponseOfAccountAuthorisationResponse.md)

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

# **create_pre_authorisation_request**
> ApiResponseOfAccountAuthorisationResponse create_pre_authorisation_request(pre_authorisation_request)

Create Pre-authorisation

Used to initiate the pre-authorisation process for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature to authenticate the user. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
from yapily.model.pre_authorisation_request import PreAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    pre_authorisation_request = PreAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        scope="AIS",
    ) # PreAuthorisationRequest | 
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Pre-authorisation
        api_response = api_instance.create_pre_authorisation_request(pre_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_pre_authorisation_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Pre-authorisation
        api_response = api_instance.create_pre_authorisation_request(pre_authorisation_request, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->create_pre_authorisation_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_authorisation_request** | [**PreAuthorisationRequest**](PreAuthorisationRequest.md)|  |
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfAccountAuthorisationResponse**](ApiResponseOfAccountAuthorisationResponse.md)

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

# **initiate_account_request**
> ApiResponseOfAccountAuthorisationResponse initiate_account_request(account_authorisation_request)

Create Account Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial institution in order to give consent to access account data.<br><br>See [Redirect Account Flows](https://docs.yapily.com/pages/key-concepts/account-data/account-authorisation/redirect-account-flows/) for more information about this flow.<br><br>Feature: `INITIATE_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
from yapily.model.account_authorisation_request import AccountAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    account_authorisation_request = AccountAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        account_request=AccountRequest(
            transaction_from=dateutil_parser('2020-01-01T00:00:00Z'),
            transaction_to=dateutil_parser('2021-01-01T00:00:00Z'),
            expires_at=dateutil_parser('2025-01-01T00:00:00Z'),
            account_identifiers=AccountInfo(
                account_id="500000000000000000000001",
                account_identification=AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ),
            account_identifiers_for_transaction=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            account_identifiers_for_balance=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            feature_scope=[
                FeatureEnum("INITIATE_PRE_AUTHORISATION"),
            ],
        ),
    ) # AccountAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Account Authorisation
        api_response = api_instance.initiate_account_request(account_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_account_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Account Authorisation
        api_response = api_instance.initiate_account_request(account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_account_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_authorisation_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfAccountAuthorisationResponse**](ApiResponseOfAccountAuthorisationResponse.md)

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

# **initiate_embedded_account_request**
> ApiResponseOfEmbeddedAccountAuthorisationResponse initiate_embedded_account_request(embedded_account_authorisation_request)

Create Embedded Account Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_ACCOUNT_REQUEST` feature in order to obtain the the user's authorisation to access their account information. <br><br>See [Embedded Account Flows](https://docs.yapily.com/pages/key-concepts/account-data/account-authorisation/embedded-account-flows/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_embedded_account_authorisation_response import ApiResponseOfEmbeddedAccountAuthorisationResponse
from yapily.model.embedded_account_authorisation_request import EmbeddedAccountAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    embedded_account_authorisation_request = EmbeddedAccountAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
        account_request=AccountRequest(
            transaction_from=dateutil_parser('2020-01-01T00:00:00Z'),
            transaction_to=dateutil_parser('2021-01-01T00:00:00Z'),
            expires_at=dateutil_parser('2025-01-01T00:00:00Z'),
            account_identifiers=AccountInfo(
                account_id="500000000000000000000001",
                account_identification=AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ),
            account_identifiers_for_transaction=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            account_identifiers_for_balance=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            feature_scope=[
                FeatureEnum("INITIATE_PRE_AUTHORISATION"),
            ],
        ),
    ) # EmbeddedAccountAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Embedded Account Authorisation
        api_response = api_instance.initiate_embedded_account_request(embedded_account_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_embedded_account_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Embedded Account Authorisation
        api_response = api_instance.initiate_embedded_account_request(embedded_account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_embedded_account_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedded_account_authorisation_request** | [**EmbeddedAccountAuthorisationRequest**](EmbeddedAccountAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfEmbeddedAccountAuthorisationResponse**](ApiResponseOfEmbeddedAccountAuthorisationResponse.md)

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

# **re_authorise_account**
> ApiResponseOfAccountAuthorisationResponse re_authorise_account(consent)

Re-authorise Account Consent

Used to prompt the account holder for continued access to their financial data. This endpoint should be used when a `Consent` that was previously `AUTHORIZED` can no longer be used to retrieve data.<br><br>See [Re-Authorisation](https://docs.yapily.com/pages/key-concepts/account-data/account-consents/#re-authorisation) for more information.

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Re-authorise Account Consent
        api_response = api_instance.re_authorise_account(consent)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->re_authorise_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Re-authorise Account Consent
        api_response = api_instance.re_authorise_account(consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->re_authorise_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfAccountAuthorisationResponse**](ApiResponseOfAccountAuthorisationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embedded_account_request**
> ApiResponseOfEmbeddedAccountAuthorisationResponse update_embedded_account_request(consent_id, embedded_account_authorisation_request)

Update Embedded Account Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to access the user's financial data. <br><br>See [Embedded Account Flows](https://docs.yapily.com/pages/key-concepts/account-data/account-authorisation/embedded-account-flows/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_embedded_account_authorisation_response import ApiResponseOfEmbeddedAccountAuthorisationResponse
from yapily.model.embedded_account_authorisation_request import EmbeddedAccountAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.
    embedded_account_authorisation_request = EmbeddedAccountAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
        account_request=AccountRequest(
            transaction_from=dateutil_parser('2020-01-01T00:00:00Z'),
            transaction_to=dateutil_parser('2021-01-01T00:00:00Z'),
            expires_at=dateutil_parser('2025-01-01T00:00:00Z'),
            account_identifiers=AccountInfo(
                account_id="500000000000000000000001",
                account_identification=AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ),
            account_identifiers_for_transaction=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            account_identifiers_for_balance=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            feature_scope=[
                FeatureEnum("INITIATE_PRE_AUTHORISATION"),
            ],
        ),
    ) # EmbeddedAccountAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Embedded Account Authorisation
        api_response = api_instance.update_embedded_account_request(consent_id, embedded_account_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_account_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Embedded Account Authorisation
        api_response = api_instance.update_embedded_account_request(consent_id, embedded_account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_account_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |
 **embedded_account_authorisation_request** | [**EmbeddedAccountAuthorisationRequest**](EmbeddedAccountAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfEmbeddedAccountAuthorisationResponse**](ApiResponseOfEmbeddedAccountAuthorisationResponse.md)

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

# **update_embedded_bulk_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse update_embedded_bulk_payment_authorisation(consent_id, bulk_payment_embedded_authorisation_request)

Update Embedded Bulk Payment Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Embedded Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest
from yapily.model.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.
    bulk_payment_embedded_authorisation_request = BulkPaymentEmbeddedAuthorisationRequest(
        user_uuid="e006a012-c306-4355-a6a1-99bf69ae5171",
        application_user_id="user-234562290",
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=BulkPaymentRequest(
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
        ),
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
    ) # BulkPaymentEmbeddedAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Embedded Bulk Payment Authorisation
        api_response = api_instance.update_embedded_bulk_payment_authorisation(consent_id, bulk_payment_embedded_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_bulk_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Embedded Bulk Payment Authorisation
        api_response = api_instance.update_embedded_bulk_payment_authorisation(consent_id, bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_bulk_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |
 **bulk_payment_embedded_authorisation_request** | [**BulkPaymentEmbeddedAuthorisationRequest**](BulkPaymentEmbeddedAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embedded_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse update_embedded_payment_authorisation(consent_id, payment_embedded_authorisation_request)

Update Embedded Payment Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to initiate a payment. <br><br> See [Embedded Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.payment_embedded_authorisation_request import PaymentEmbeddedAuthorisationRequest
from yapily.model.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent_id = "consentId_example" # str | __Mandatory__. The consent Id of the `Consent` to update.
    payment_embedded_authorisation_request = PaymentEmbeddedAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=PaymentRequest(
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
        user_credentials=UserCredentials(
            id="6154057725",
            corporate_id="6345898763",
            password="PISPWD12",
        ),
        selected_sca_method=ScaMethod(
            id="258211#OPTICAL",
            type=Type("SMS_OTP"),
            description="Testkarte Hr. Haubach_1, optisch",
        ),
        sca_code="325614",
    ) # PaymentEmbeddedAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Embedded Payment Authorisation
        api_response = api_instance.update_embedded_payment_authorisation(consent_id, payment_embedded_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Embedded Payment Authorisation
        api_response = api_instance.update_embedded_payment_authorisation(consent_id, payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. |
 **payment_embedded_authorisation_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse update_payment_authorisation(consent, payment_authorisation_request)

Update Payment Pre-authorisation

Used to continue the authorisation process and for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-flows/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_payment_authorisation_request_response import ApiResponseOfPaymentAuthorisationRequestResponse
from yapily.model.payment_authorisation_request import PaymentAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    payment_authorisation_request = PaymentAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        payment_request=PaymentRequest(
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
    ) # PaymentAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Payment Pre-authorisation
        api_response = api_instance.update_payment_authorisation(consent, payment_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_payment_authorisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Payment Pre-authorisation
        api_response = api_instance.update_payment_authorisation(consent, payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_payment_authorisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **payment_authorisation_request** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pre_authorise_account_consent**
> ApiResponseOfAccountAuthorisationResponse update_pre_authorise_account_consent(consent, account_authorisation_request)

Update Account Pre-authorisation

Used to continue the authorisation process and for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial institution in order to give consent to access account data. <br><br>See [Redirect Account Flows](https://docs.yapily.com/pages/key-concepts/account-data/account-authorisation/redirect-account-flows/) for more information about this flow. <br><br>Features: <ul><li>`INITIATE_ACCOUNT_REQUEST`</li><li>`INITIATE_PRE_AUTHORISATION`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import yapily
from yapily.api import authorisations_api
from yapily.model.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
from yapily.model.account_authorisation_request import AccountAuthorisationRequest
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
    api_instance = authorisations_api.AuthorisationsApi(api_client)
    consent = "{consentToken}" # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_authorisation_request = AccountAuthorisationRequest(
        user_uuid="user_uuid_example",
        application_user_id="user-234562290",
        forward_parameters=[
            "forward_parameters_example",
        ],
        institution_id="yapily-mock",
        callback="https://display-parameters.com",
        redirect=RedirectRequest(
            url="url_example",
        ),
        one_time_token=False,
        account_request=AccountRequest(
            transaction_from=dateutil_parser('2020-01-01T00:00:00Z'),
            transaction_to=dateutil_parser('2021-01-01T00:00:00Z'),
            expires_at=dateutil_parser('2025-01-01T00:00:00Z'),
            account_identifiers=AccountInfo(
                account_id="500000000000000000000001",
                account_identification=AccountIdentification(
                    type=AccountIdentificationType("SORT_CODE"),
                    identification="401016",
                ),
            ),
            account_identifiers_for_transaction=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            account_identifiers_for_balance=[
                AccountInfo(
                    account_id="500000000000000000000001",
                    account_identification=AccountIdentification(
                        type=AccountIdentificationType("SORT_CODE"),
                        identification="401016",
                    ),
                ),
            ],
            feature_scope=[
                FeatureEnum("INITIATE_PRE_AUTHORISATION"),
            ],
        ),
    ) # AccountAuthorisationRequest | 
    psu_id = "psu-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = "psu-corporate-id_example" # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = "psu-ip-address_example" # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Account Pre-authorisation
        api_response = api_instance.update_pre_authorise_account_consent(consent, account_authorisation_request)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_pre_authorise_account_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Account Pre-authorisation
        api_response = api_instance.update_pre_authorise_account_consent(consent, account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except yapily.ApiException as e:
        print("Exception when calling AuthorisationsApi->update_pre_authorise_account_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. |
 **account_authorisation_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)|  |
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional]
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional]

### Return type

[**ApiResponseOfAccountAuthorisationResponse**](ApiResponseOfAccountAuthorisationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

