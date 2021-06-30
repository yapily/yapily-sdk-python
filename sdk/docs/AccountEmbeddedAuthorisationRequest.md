# AccountEmbeddedAuthorisationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** | Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided. | [optional] 
**application_user_id** | **str** | Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided. | [optional] 
**forward_parameters** | **list[str]** |  | [optional] 
**institution_id** | **str** |  | 
**callback** | **str** |  | 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**account_request** | [**AccountRequest**](AccountRequest.md) |  | [optional] 
**one_time_token** | **bool** |  | 
**user_credentials** | [**UserCredentials**](UserCredentials.md) |  | [optional] 
**selected_sca_method** | [**ScaMethod**](ScaMethod.md) |  | [optional] 
**sca_code** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


