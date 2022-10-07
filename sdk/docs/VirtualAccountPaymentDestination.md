# VirtualAccountPaymentDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of destination for a payment. One of ACCOUNT, EXTERNAL or BENEFICIARY | 
**account_id** | **str** | Only present if type is ACCOUNT. Identifies the Virtual Account to which the payment was made | [optional] 
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) | Only present if type is EXTERNAL. The account identifications that identify an external destination | [optional] 
**beneficiary_id** | **str** | Only present if type is BENEFICIARY. Unique id of the beneficiary | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


