# Address

__Conditional__. The address of the `Payee` or `Payer`.<ul><li>`payee.address` is mandatory when the `paymentType` is an `INTERNATIONAL` payment</li><li>An `Institution` may require you to specify the `country` when used in the context ofthe `Payee` to be able to make a payment.</li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **[str]** | __Optional__. The address line of the address | [optional] 
**street_name** | **str** | __Optional__. The street name of the address | [optional] 
**building_number** | **str** | __Optional__. The building number of the address | [optional] 
**post_code** | **str** | __Optional__. The post code of the address | [optional] 
**town_name** | **str** | __Optional__. The town name of the address | [optional] 
**county** | **[str]** | __Optional__. The list of counties for the address | [optional] 
**country** | **str** | __Conditional__. The 2-letter country code for the address. &lt;br&gt;&lt;br&gt;An &#x60;Institution&#x60; may require you to specify the &#x60;country&#x60; when used in the context of the &#x60;Payee&#x60; to be able to make a payment | [optional] 
**department** | **str** | __Optional__. The department for the address | [optional] 
**sub_department** | **str** | __Optional__. The sub-department for the address | [optional] 
**address_type** | [**AddressTypeEnum**](AddressTypeEnum.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


