# ExchangeRateInformationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_currency** | **str** | __Mandatory__. The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP &#x3D; xxxCUR, the unit currency is &#x60;GBP&#x60;. | 
**rate_type** | [**RateTypeEnum**](RateTypeEnum.md) |  | 
**rate** | **float** | __Optional__. The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. | [optional] 
**foreign_exchange_contract_reference** | **str** | __Optional__. The unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent. | [optional] 
**exchange_rate_expiry_date** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


