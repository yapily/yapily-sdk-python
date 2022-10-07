# VirtualAccountBeneficiary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the Beneficiary | [optional] 
**payment_schemes** | **[str]** | Beneficiary payment schemes | [optional] 
**nickname** | **str** | Reference that can be provided in order to help with identification of the Beneficiary | [optional] 
**type** | **str** | Indicates the type of Beneficiary as either a INDIVIDUAL or BUSINESS | [optional] 
**name** | **str** |  | [optional] 
**birth_date** | **date** |  | [optional] 
**address** | [**VirtualAccountBeneficiaryAddress**](VirtualAccountBeneficiaryAddress.md) |  | [optional] 
**account** | [**VirtualAccountBeneficiaryAccount**](VirtualAccountBeneficiaryAccount.md) |  | [optional] 
**status** | **str** | The current status of the Beneficiary &lt;br&gt; PENDING - Beneficiary is awaiting verification &lt;br&gt; ACTIVE - Beneficiary can be used in a Pay Out &lt;br&gt; BLOCKED - Beneficiary cannot be used in a Pay Out | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


