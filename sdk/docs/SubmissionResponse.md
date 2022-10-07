# SubmissionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiation_details** | [**InitiationDetails**](InitiationDetails.md) |  | 
**submission_details** | [**SubmissionDetails**](SubmissionDetails.md) |  | 
**id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**refund_account** | [**RefundAccount**](RefundAccount.md) |  | [optional] 
**expected_execution_time** | **datetime** |  | [optional] 
**expected_settlement_time** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


