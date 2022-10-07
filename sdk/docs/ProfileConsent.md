# ProfileConsent

Object returned when creating a User Profile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the ProfileConsent | [optional] 
**status** | **str** | The status, can be PENDING, COMPLETED or ERROR. | [optional] 
**user_id** | **str** | The userUuid. | [optional] 
**reference_consent_id** | **str** | The referenceConsentId. | [optional] 
**institution_id** | **str** | The id of the Institution. | [optional] 
**created_at** | **datetime** | When a profile consent is created. | [optional] 
**expires_at** | **datetime** | When a profile consent is expired after created + X. | [optional] 
**data_inserted_at** | **datetime** | After data retrieval from aggregated profile consent is completed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


