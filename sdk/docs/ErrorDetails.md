# ErrorDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** | Unique identifier of the request, used by Yapily for support purposes | 
**code** | **int** | Numeric HTTP status code associated with the error | 
**status** | **str** | Textual description of the HTTP status | 
**support_url** | **str** | Link to where further information regarding the error can be found | [optional] 
**source** | **str** | Source of the error. This may be YAPILY, the INSTITUTION, or the USER | [optional] 
**issues** | [**[ErrorIssue]**](ErrorIssue.md) | List of issues relating to the error | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


