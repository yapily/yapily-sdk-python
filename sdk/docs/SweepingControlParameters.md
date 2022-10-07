# SweepingControlParameters

Define the restrictions and limits for payment orders as part of Sweeping VRP consent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_authentication_methods** | **[str]** | __Mandatory__. Defines the authentication method(s) allowed in payment submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED]. | 
**periodic_limits** | [**[SweepingPeriodicLimits]**](SweepingPeriodicLimits.md) |  | 
**max_amount_per_payment** | **bool, date, datetime, dict, float, int, list, str, none_type** | __Mandatory__. Max amount that can be submitted per payment. | 
**valid_from** | **datetime** | __Optional__. Start date when the consent becomes valid. | [optional] 
**valid_to** | **datetime** | __Optional__. End date when the consent expires and becomes invalid. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


