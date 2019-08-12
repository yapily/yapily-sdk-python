# PaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**payment_lifecycle_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount_details** | [**Amount**](Amount.md) |  | [optional] 
**charge_details** | [**list[ChargeDetails]**](ChargeDetails.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


