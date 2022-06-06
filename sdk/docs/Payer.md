# Payer

__Conditional__. The `Payer` object contains details of the benefactor [person or business]. If you define this in your payment request, you mustdefine this along with all of the nested mandatory properties.<ol>     <li>The `Payer` object is mandatory along with its mandatory properties when the account of the benefactor is from an `Institution` in Europe.          See [Berlin Group](https://docs.yapily.com/pages/knowledge/open-banking/berlin_group/) for more information.</li>     <li>The `Payer` should be specified if the `Payer` account is intended to be locked.</li></ol>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payer&#x60; bank account. | 
**name** | **str** | __Mandatory__. The account holder name of the Payer. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


