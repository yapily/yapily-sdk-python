# VirtualAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the account | [optional] 
**created_date_time** | **datetime** | Date and time that the account was created | [optional] 
**status** | **str** | The current state of the Account &lt;br&gt; PENDING - Creation of the account is in progress &lt;br&gt; ACTIVE - The account is active and in use &lt;br&gt; FAILED - An issue occured during account creation &lt;br&gt; SUSPENDED - The account has been temporarily suspended by the account provider. It cannot currently be used &lt;br&gt; CLOSED - The account has been permanently closed and cannot be used | [optional] 
**nickname** | **str** | Reference that can be provided in order to help with identification of the account | [optional] 
**currency** | **str** | Three-letter ISO 4217 currency code | [optional] 
**balances** | [**[VirtualAccountBalance]**](VirtualAccountBalance.md) |  | [optional] 
**bank_account** | [**VirtualAccountBankAccount**](VirtualAccountBankAccount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


