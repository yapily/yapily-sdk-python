# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction Id returned by the institution if present | [optional] 
**date** | **datetime** | Transaction date as defined by the institution | [optional] 
**booking_date_time** | **datetime** | Date and (if available) time that transaction is posted | [optional] 
**value_date_time** | **datetime** | The actual or expected date and time transaction is cleared | [optional] 
**status** | **str** | The status of the transaction | [optional] 
**amount** | **float** | Deprecated. Use the amount value in &#x60;transactionAmount&#x60; instead | [optional] 
**currency** | **str** | Deprecated. Use the currency value in &#x60;transactionAmount&#x60; instead | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**currency_exchange** | [**CurrencyExchange**](CurrencyExchange.md) |  | [optional] 
**charge_details** | [**ChargeDetails**](ChargeDetails.md) | If present, contains details of any charges applied during this transaction | [optional] 
**reference** | **str** | Transaction reference | [optional] 
**statement_references** | [**list[StatementReference]**](StatementReference.md) |  | [optional] 
**description** | **str** | Unstructured text containing details of the transaction. Usage varies according to the institution | [optional] 
**transaction_information** | **list[str]** | Further information related to the transaction. Usage varies according to the institution | [optional] 
**address_details** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**iso_bank_transaction_code** | [**IsoBankTransactionCode**](IsoBankTransactionCode.md) |  | [optional] 
**proprietary_bank_transaction_code** | [**ProprietaryBankTransactionCode**](ProprietaryBankTransactionCode.md) |  | [optional] 
**balance** | [**Balance**](Balance.md) | Running account balance after transaction has been applied | [optional] 
**merchant** | [**Merchant**](Merchant.md) | Merchant details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


