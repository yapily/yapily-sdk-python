# RealTimeTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**date** | **datetime** |  | [optional] 
**booking_date_time** | **datetime** |  | [optional] 
**value_date_time** | **datetime** |  | [optional] 
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**gross_amount** | [**Amount**](Amount.md) |  | [optional] 
**currency_exchange** | [**CurrencyExchange**](CurrencyExchange.md) |  | [optional] 
**charge_details** | [**TransactionChargeDetails**](TransactionChargeDetails.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**statement_references** | [**[StatementReference]**](StatementReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**transaction_information** | **[str]** |  | [optional] 
**address_details** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**iso_bank_transaction_code** | [**IsoBankTransactionCode**](IsoBankTransactionCode.md) |  | [optional] 
**proprietary_bank_transaction_code** | [**ProprietaryBankTransactionCode**](ProprietaryBankTransactionCode.md) |  | [optional] 
**balance** | [**TransactionBalance**](TransactionBalance.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**payer_details** | [**Payer**](Payer.md) |  | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**supplementary_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


