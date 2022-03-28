# Yapily Python SDK
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.326.3&x2=0)](http://badge.fury.io/gh/boennemann%2Fbadges)

This SDK was generated using [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen). The SDK can be used as a module in your code and the examples demonstrate how to connect
to financial institutions integrated with Yapily.

## Requirements

To connect to the Yapily API, you will need to register your 
application at [https://dashboard.yapily.com]().

These application credentials can then be used to authorise all
your API requests.

## Installation

The SDK is currently available in the Yapily github repository and 
can be included in your project 
by adding it to your dependencies

#### pip install

pip3 install git+https://github.com/yapily/yapily-sdk-python.git#subdirectory=sdk

#### pip upgrade

pip3 install --upgrade git+https://github.com/yapily/yapily-sdk-python.git#subdirectory=sdk

## Usage

Sample usage of the SDK can be seen in the `examples` folder.

- Retrieve a list of available financial institutions to connect to

```python
configuration = Configuration()
configuration.username = constants.APPLICATION_ID
configuration.password = constants.APPLICATION_SECRET

apiClient = ApiClient(configuration)
institutionsApi = InstitutionsApi(apiClient)
institutions = institutionsApi.get_institutions_using_get()
```

- Creating users and retrieving users for your application registered in the Yapily Dashboard
```python
application_user = NewApplicationUser(application_user_id=app_user_id)
user_api = ApplicationUsersApi(apiClient)
user_api.add_user_using_post(application_user)
```

- Create an authorisation URL for your users to use to log into their institution

```python
account_authorisation_request = AccountAuthorisationRequest(
    application_user_id=constants.APPLICATION_USER_ID, 
    institution_id=constants.INSTITUTION_ID,
    callback='',
    one_time_token=''
)

response = accounts_api.initiate_account_request_using_post(account_auth_request=account_authorisation_request)
redirect_url = response.data.authorisation_url
```
 
- Obtaining a valid consent for financial data

```python
def filterByStatus(consent):
    if (consent.status == "AUTHORIZED"):
        return True
    else:
        return False

consents = ConsentsApi(apiClient).get_consents_using_get(
    filter_application_user_id=[constants.APPLICATION_USER_ID],
    filter_institution=[constants.INSTITUTION_ID]
).data

authorised_consents = list(filter(filterByStatus, consents))
consent = authorised_consents[0]
consent_token = consent.consent_token
```

- Returning user account details
```python
accountsApi = AccountsApi(apiClient)
accounts = accountsApi.get_accounts_using_get(consent_token)
```

- Returning user transaction details

```python
transactionsApi = TransactionsApi(apiClient)
transactions = transactionsApi.get_transactions_using_get(consent_token, accounts.data[0]._id)
```

- Returning user identity details
```python
institutions_api = InstitutionsApi(apiClient)
features = institutions_api.get_institution_using_get(constants.INSTITUTION_ID).features
if ("IDENTITY" in features):
    identity_api = IdentityApi(apiClient)
    identity = identity_api.get_identity_using_get(consent_token)
```

## Further information

For more information on how to get connected, visit the [Yapily Knowledge Base](https://kb.yapily.com).
