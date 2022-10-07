# VirtualAccountPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the payment | [optional] 
**created_date_time** | **datetime** | Date and time that the payment was created | [optional] 
**payment_date** | **date** | Date on which the payment instruction will be executed, that may be in the future | [optional] 
**type** | **str** | Type of payment. One of PAY_IN, PAY_OUT, RETURN_IN or RETURN_OUT | [optional] 
**payment_scheme** | **str** | Method of settlement to complete the payment. One of: &lt;br&gt; FASTER_PAYMENTS &lt;br&gt; SEPA_CREDIT &lt;br&gt; SEPA_INSTANT &lt;br&gt; SWIFT &lt;br&gt; SWIFT_EXPRESS &lt;br&gt; CHAPS &lt;br&gt; IAT &lt;br&gt; WIRE | [optional] 
**amount** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**reference** | **str** | Reference to be associated with the payment. This will be appear on the beneficiary&#39;s bank statement | [optional] 
**status** | **str** | The current state of the transaction &lt;br&gt; INITIATED - The transaction request is acknowledged and will not undergo validation checks &lt;br&gt; PROCESSING - Initial checks succeeded and the transaction request is now being processed &lt;br&gt; COMPLETED - The transaction has been successfully processed (terminal status) &lt;br&gt; FAILED - An failure occured during transaction processing (terminal status) | [optional] 
**source** | [**VirtualAccountPaymentSource**](VirtualAccountPaymentSource.md) |  | [optional] 
**destination** | [**VirtualAccountPaymentDestination**](VirtualAccountPaymentDestination.md) |  | [optional] 
**original_payment_id** | **str** | Unique id of the original payment that was refunded | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


