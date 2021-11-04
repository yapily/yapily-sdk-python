# BeneficiaryPayee

__Mandatory__. The `BeneficiaryPayee` object contains details of the beneficiary [person or business]. You must define this in your payment request along with all of the nested mandatory properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the beneficiary. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**account_identifications** | [**list[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;BeneficiaryPayee&#x60; bank account. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


