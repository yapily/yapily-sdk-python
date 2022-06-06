# BeneficiaryPayee

__Mandatory__. The `BeneficiaryPayee` object contains details of the beneficiary [person or business]. You must define this in your payment request along with all of the nested mandatory properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;BeneficiaryPayee&#x60; bank account. | 
**name** | **str** | The account holder name of the beneficiary. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


