# EmbeddedAccountAuthorisationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | &#x60;User&#x60; for which the authorisation request was created. | [optional] 
**user_uuid** | **str** | __Conditional__. User-friendly identifier of the &#x60;User&#x60; that provides authorisation. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60; that will authorise the authorisation request. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** | __Mandatory__. The &#x60;Institution&#x60; the authorisation request is sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** | Date and time of when the embedded authorisation was created by the application user. | [optional] 
**transaction_from** | **datetime** | When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved. | [optional] 
**transaction_to** | **datetime** | When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved. | [optional] 
**expires_at** | **datetime** | Date and time of when the embedded authorisation will expire by. Reauthorisation will be needed to retain access. | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**[FeatureEnum]**](FeatureEnum.md) | The set of features that the consent will provide access to. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to access account information or make a payment request. | [optional] 
**state** | **str** | Corellation ID used when handshaking with a new insitution via OAuth2 registration. | [optional] 
**authorized_at** | **datetime** | Date and time of when the request was authorised by the Institution. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the Institution. | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** | The URL link for the QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded). | [optional] 
**sca_methods** | [**[ScaMethod]**](ScaMethod.md) | List of &#x60;SCA methods&#x60; the &#x60;Institution&#x60; supports and that are available for selection. | [optional] 
**selected_sca_method** | [**ScaMethod**](ScaMethod.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


