# ChargeBearerType

__Optional__. Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Valid values are:<ul><li>`DEBT` - All transaction charges are to be borne by the debtor.</li><li>`CRED` - All transaction charges are to be borne by the creditor.</li><li>`SHAR` - In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor</li><li>`SLEV` - Charges are to be applied following the rules agreed in the service level and/or scheme.</li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | __Optional__. Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Valid values are:&lt;ul&gt;&lt;li&gt;&#x60;DEBT&#x60; - All transaction charges are to be borne by the debtor.&lt;/li&gt;&lt;li&gt;&#x60;CRED&#x60; - All transaction charges are to be borne by the creditor.&lt;/li&gt;&lt;li&gt;&#x60;SHAR&#x60; - In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor&lt;/li&gt;&lt;li&gt;&#x60;SLEV&#x60; - Charges are to be applied following the rules agreed in the service level and/or scheme.&lt;/li&gt;&lt;/ul&gt; |  must be one of ["DEBT", "CRED", "SHAR", "SLEV", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


