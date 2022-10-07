# EnrichedBalances

Enriched Balance information generated which include historic aggregated balances and predicted balances

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | A list of Account Ids used to generate Balance Prediction Profile. | [optional] 
**institutions** | **[str]** | A list of Institution Ids associated with the accounts used to generate Balance Prediction Profile. | [optional] 
**historic** | [**[EnrichedHistoricBalance]**](EnrichedHistoricBalance.md) | A list of historic balances. Each balance in the list is an aggregation (sum) of the reported balance for each account within the profile at a point in time. | [optional] 
**predicted** | [**[EnrichedPredictedBalance]**](EnrichedPredictedBalance.md) | A list of predicted balances. Each balance in the list is a projected balance of the profile at a future point in time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


