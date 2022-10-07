# AccountAuthorisationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** |  | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**transaction_from** | **datetime** |  | [optional] 
**transaction_to** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**[FeatureEnum]**](FeatureEnum.md) |  | [optional] 
**consent_token** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**authorized_at** | **datetime** |  | [optional] 
**last_confirmed_at** | **datetime** | The time that the PSU last confirmed access to their account information, either through full authentication with the institution, or through reconfirmation with the TPP. | [optional] 
**reconfirm_by** | **datetime** | The time by which the consent should be reconfirmed to ensure continued access to the account information. | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


