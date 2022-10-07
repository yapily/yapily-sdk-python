# NonSweepingAuthorisationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** | This is the Yapily user identifier for the user returned by the create user step POST ../users | [optional] 
**application_user_id** | **str** | A client&#39;s own user reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use either their own applicationUserId or the Yapily userId to reference the same user in future calls. | [optional] 
**institution_id** | **str** | The reference to the Institution which identifies which institution the authorisation request is sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**feature_scope** | [**[FeatureEnum]**](FeatureEnum.md) | __Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the &#x60;Institution&#x60;, this may also populate a consent screen which list these scopes before the user authorises.&lt;br&gt;&lt;br&gt;This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the &#x60;Institution&#x60; supports.To find out which scopes an &#x60;Institution&#x60; supports, check [GET Institution](./#get-institution). | [optional] 
**consent_token** | **str** | The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the payment request. | [optional] 
**state** | **str** |  | [optional] 
**authorized_at** | **datetime** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** |  | [optional] 
**control_parameters** | [**NonSweepingControlParameters**](NonSweepingControlParameters.md) |  | [optional] 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**initiation_details** | [**InitiationDetails**](InitiationDetails.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


