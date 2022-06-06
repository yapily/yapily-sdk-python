# FrequencyRequest

__Mandatory__. Defines the intervals at which payment should be made.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FrequencyEnumExtended**](FrequencyEnumExtended.md) |  | 
**interval_week** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 
**interval_month** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 
**execution_day** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


