# PaymentAuthorisationRequestResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**transaction_from** | **datetime** |  | [optional] 
**transaction_to** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**time_to_expire_in_millis** | **int** | Deprecated. Use &#x60;timeToExpire&#x60; instead. | [optional] 
**time_to_expire** | **str** | ISO 8601 duration | [optional] 
**feature_scope** | **list[str]** |  | [optional] 
**charges** | [**list[ChargeDetails]**](ChargeDetails.md) |  | [optional] 
**exchange_rate_information** | [**ExchangeRateInformationResponse**](ExchangeRateInformationResponse.md) |  | [optional] 
**consent_token** | **str** |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**qr_code_url** | **str** |  | [optional] 
**authorized_at** | **datetime** |  | [optional] 
**explanation** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


