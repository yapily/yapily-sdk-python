# VirtualAccountPayInDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the payment | [optional] 
**payment_scheme** | **str** | Method of settlement to complete the payment. One of: &lt;br&gt; FASTER_PAYMENTS &lt;br&gt; SEPA_CREDIT &lt;br&gt; SEPA_INSTANT &lt;br&gt; SWIFT &lt;br&gt; SWIFT_EXPRESS &lt;br&gt; CHAPS &lt;br&gt; IAT &lt;br&gt; WIRE | [optional] 
**amount** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**reference** | **str** | Reference associated with the payment and which appears on the beneficiary&#39;s bank statement | [optional] 
**source** | [**VirtualAccountPaymentSource**](VirtualAccountPaymentSource.md) |  | [optional] 
**name** | **str** | Account source name | [optional] 
**address** | **str** | The address of the source bank account | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


