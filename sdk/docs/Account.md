# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the account. | [optional] 
**type** | **str** | Specifies the type of account e.g. (BUSINESS_CURRENT). | [optional] 
**description** | **str** | Product name as defined by the financial institution for this account | [optional] 
**balance** | **float** | Main / headline balance for the account. &lt;br&gt;&lt;br&gt; Use of this field is recommended as fallback only. Instead, use of the typed balances (accountBalances) is recommended. | [optional] 
**currency** | **str** | Currency the bank account balance is denoted in. &lt;br&gt;&lt;br&gt; Specified as a 3-letter ISO 4217 currency code | [optional] 
**usage_type** | [**UsageType**](UsageType.md) |  | [optional] 
**account_type** | [**AccountType**](AccountType.md) |  | [optional] 
**nickname** | **str** | Nickname of the account that was provided by the account owner. &lt;br&gt;&lt;br&gt; May be used to aid identification of the account. | [optional] 
**details** | **str** | Supplementary specifications that might be provided by the Bank. These provide further characteristics about the account. | [optional] 
**account_names** | [**[AccountName]**](AccountName.md) |  | [optional] 
**account_identifications** | [**[AccountIdentification]**](AccountIdentification.md) |  | [optional] 
**account_balances** | [**[AccountBalance]**](AccountBalance.md) |  | [optional] 
**consolidated_account_information** | [**ConsolidatedAccountInformation**](ConsolidatedAccountInformation.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


