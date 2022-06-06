# PaymentType

__Mandatory__. Used to specify which of the [payment types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#payment-types) to execute.<br><br>See [European Payments](https://docs.yapily.com/pages/knowledge/open-banking/european_payments/) to verify whether the `type` should be `DOMESTIC` or `INTERNATIONAL`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | __Mandatory__. Used to specify which of the [payment types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#payment-types) to execute.&lt;br&gt;&lt;br&gt;See [European Payments](https://docs.yapily.com/pages/knowledge/open-banking/european_payments/) to verify whether the &#x60;type&#x60; should be &#x60;DOMESTIC&#x60; or &#x60;INTERNATIONAL&#x60;. |  must be one of ["DOMESTIC_PAYMENT", "DOMESTIC_INSTANT_PAYMENT", "DOMESTIC_VARIABLE_RECURRING_PAYMENT", "DOMESTIC_SCHEDULED_PAYMENT", "DOMESTIC_PERIODIC_PAYMENT", "INTERNATIONAL_PAYMENT", "INTERNATIONAL_SCHEDULED_PAYMENT", "INTERNATIONAL_PERIODIC_PAYMENT", "BULK_PAYMENT", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


