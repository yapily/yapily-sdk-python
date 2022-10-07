# ApplicationUser

Information about a user of an application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | A unique identifier for the &#39;User&#39; assigned by Yapily. | [optional] 
**application_uuid** | **str** | Unique identifier of the application the user is associated with. | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60;. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_consents** | [**[InstitutionConsent]**](InstitutionConsent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


