# InternationalPaymentRequest

__Conditional__. Used to specify properties to define an international payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>INTERNATIONAL_SINGLE_PAYMENT</code></li>     <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_of_transfer** | **str** | __Mandatory__. The 3-letter currency code for the currency of the payment to be transferred which can differ from the currency of the payer&#39;s account. | 
**exchange_rate_information** | [**ExchangeRateInformation**](ExchangeRateInformation.md) |  | [optional] 
**purpose** | **str** | __Optional__. Used to indicate the external purpose as a [ISO20022 purpose code](https://www.rba.hr/documents/20182/183267/External+purpose+codes+list/8a28f888-1f83-5e29-d6ed-fce05f428689?version&#x3D;1.1) value. | [optional] 
**priority** | [**PriorityCodeEnum**](PriorityCodeEnum.md) |  | [optional] 
**charge_bearer** | [**ChargeBearerType**](ChargeBearerType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


