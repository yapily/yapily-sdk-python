# SubmissionRequest

__Mandatory__. The payment request object defining the details of the payment for execution under the Variable Recurring Payment consent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | __Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | 
**psu_authentication_method** | **str** | __Mandatory__. Chosen authentication method for submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED]. | 
**payment_amount** | [**Amount**](Amount.md) |  | 
**context_type** | [**PaymentContextType**](PaymentContextType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


