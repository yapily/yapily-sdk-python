# PaymentAuthorisationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** |  | [optional] 
**forward_parameters** | **list[str]** |  | [optional] 
**institution_id** | **str** |  | 
**callback** | **str** |  | 
**one_time_token** | **bool** |  | 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) |  | 
**total_max_amount** | **float** |  | [optional] 
**total_max_amount_frequency** | **str** |  | [optional] 
**max_amount_per_request** | **float** |  | [optional] 
**starts_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**allow_overdraft** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


