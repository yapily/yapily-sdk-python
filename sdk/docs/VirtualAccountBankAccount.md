# VirtualAccountBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter ISO 4217 currency code | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_address** | **str** |  | [optional] 
**bank_country** | **str** | Two-letter ISO 3166 country code | [optional] 
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) | The account identifications that identify the Beneficiary bank account. | [optional] 
**pay_in_reference** | **str** | Reference required for paying into the account. When no reference is provided, then one is not required to pay into the acount. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


