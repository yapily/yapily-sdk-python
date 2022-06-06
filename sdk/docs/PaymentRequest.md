# PaymentRequest

__Mandatory__. The payment request object defining the details of the payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | __Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | 
**type** | [**PaymentType**](PaymentType.md) |  | 
**payee** | [**Payee**](Payee.md) |  | 
**amount** | [**Amount**](Amount.md) |  | 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**context_type** | [**PaymentContextType**](PaymentContextType.md) |  | [optional] 
**periodic_payment** | [**PeriodicPaymentRequest**](PeriodicPaymentRequest.md) |  | [optional] 
**international_payment** | [**InternationalPaymentRequest**](InternationalPaymentRequest.md) |  | [optional] 
**payment_date_time** | **datetime** | __Conditional__. Used to specify the date of the payment when the payment type is one of the following:&lt;ul&gt;    &lt;li&gt;&lt;code&gt;DOMESTIC_SCHEDULED_PAYMENT&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;DOMESTIC_PERIODIC_PAYMENT&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;INTERNATIONAL_SCHEDULED_PAYMENT&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;INTERNATIONAL_PERIODIC_PAYMENT&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 
**read_refund_account** | **bool** | __Optional__. Used to request the payer details in the payment response when the &#x60;Institution&#x60; provides the feature &#x60;READ_DOMESTIC_SINGLE_REFUND&#x60;.&lt;br&gt;&lt;br&gt;See [Reverse Payments](https://docs.yapily.com/pages/knowledge/open-banking/reverse_payments/) for more information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


