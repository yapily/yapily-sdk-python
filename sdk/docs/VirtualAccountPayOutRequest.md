# VirtualAccountPayOutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique id of the source / payer account | 
**amount** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**reference** | **str** | Reference to be associated with the payment. This will be appear on the beneficiary&#39;s bank statement | 
**beneficiary_id** | **str** | Unique id of the beneficiary to whom the payment will be made | 
**payment_scheme** | **str** | Method of settlement to complete the payment. One of: &lt;br&gt; FASTER_PAYMENTS &lt;br&gt; SEPA_CREDIT &lt;br&gt; SEPA_INSTANT &lt;br&gt; SWIFT &lt;br&gt; SWIFT_EXPRESS &lt;br&gt; CHAPS &lt;br&gt; IAT &lt;br&gt; WIRE | 
**payment_date** | **date** | Date on which a payment instruction will be executed, that must be in the future | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


