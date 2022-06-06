# Payee

__Mandatory__. The `Payee` object contains details of the beneficiary [person or business]. You must define this in your payment request alongwith all of the nested mandatory properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __Mandatory__. The account holder name of the beneficiary. | 
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payee&#x60; bank account. | 
**address** | [**Address**](Address.md) |  | [optional] 
**merchant_id** | **str** | __Optional__. The merchant ID is a unique code provided by the payment processor to the merchant. | [optional] 
**merchant_category_code** | **str** | __Optional__. The category code of the merchant in case the &#x60;Payee&#x60; is a business. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


