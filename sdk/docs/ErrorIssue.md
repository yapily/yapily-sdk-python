# ErrorIssue

Detailed information regarding the issue that was experienced during processing of the request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Category of the issue | 
**code** | **str** | Code that uniquely identifies the type of issue | 
**parameter** | **str** | Identfies the parameter / property within the request (headers, query parameters or body) that the issue relates to. For headers and query parameters, it refers to the parameter name. For the body, it refers to the JSONPath of the property | [optional] 
**message** | **str** | Human readable description of the issue that was experienced | [optional] 
**institution_error** | [**InstitutionError**](InstitutionError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


