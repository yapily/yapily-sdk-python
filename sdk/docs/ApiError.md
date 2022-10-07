# ApiError

Provides details of the error that has occured.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | _Mandatory_. Numeric &#x60;HTTP&#x60; status code associated with the error. | [optional] 
**institution_error** | [**InstitutionError**](InstitutionError.md) |  | [optional] 
**message** | **str** | __Mandatory__. Description of the exact error that has been experienced. | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** | __Mandatory__. Textual description of the &#x60;HTTP&#x60; error status type. | [optional] 
**tracing_id** | **str** | _Optional_.  A unique identifier assigned by Yapily for the request that can be used for support purposes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


