# SortCodePaymentAuthRequest

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
**payment_request** | [**SortCodePaymentRequest**](SortCodePaymentRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


