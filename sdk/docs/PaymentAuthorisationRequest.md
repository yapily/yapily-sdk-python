# PaymentAuthorisationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** | Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided. | [optional] 
**application_user_id** | **str** | Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided. | [optional] 
**forward_parameters** | **list[str]** |  | [optional] 
**institution_id** | **str** |  | 
**callback** | **str** |  | 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**one_time_token** | **bool** |  | 
**total_max_amount** | **float** |  | [optional] 
**total_max_amount_frequency** | **str** |  | [optional] 
**max_amount_per_request** | **float** |  | [optional] 
**starts_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**allow_overdraft** | **bool** |  | [optional] 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


