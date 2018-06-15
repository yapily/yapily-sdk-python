# Yapily Python SDK
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=0.1.2-SNAPSHOT)](http://badge.fury.io/gh/boennemann%2Fbadges)

This SDK can be used as a module or an example of how to connect
to any financial institution integrated by Yapily.

## Requirements

To connect to the Yapily API, you will need to register your 
application at [https://dashboard.yapily.com]().

These application credentials can then be used to authorise all
your API requests.

## Installation

The SDK is currently available in the Yapily github repository and 
can be included in your project 
by adding it to your dependencies

#### pip

pip install git+https://github.com/yapily/yapily-sdk-python.git#subdirectory=sdk

## Usage

Sample usage of the SDK can be seen in the `examples` folder.

- Retrieve a list of available financial institutions to connect to

```python
institutionsApi = InstitutionsApi(ApiClient(Configuration()))
institutions = institutionsApi.get_institutions_using_get()
```

- Creating users and retrieving users for your application registered in the Yapily Dashboard
```python
application_user = ApplicationUser()
application_user.uuid = str(uuid.uuid4())
user_api = ApplicationUsersApi(ApiClient(Configuration()))
user_api.add_user_using_post_with_http_info(application_user)
```

- Receiving an authorisation URL your users to log into their institution

```python
redirect_url = auth_direct_url(constants.APPLICATION_ID,app_user_uuid,institution_id,constants.CALLBACK_URL,"account")
```

- Receiving consents issued by your user authorizing
```python
consents = ConsentsApi(apiClient).get_user_consents_using_get(app_user_uuid)
```
 
- Returning user account details

```python
accounts_api =  AccountsApi(ApiClient(configuration,"CONSENT","consent-token"))
accounts = accounts_api.get_accounts_using_get()
```

- Returning user transaction details

```python
transactionsApi = TransactionsApi(ApiClient(configuration,"CONSENT","consent-token"))
transactions = transactionsApi.get_transactions_using_get("account_id")
```

- Returning user identity details
```python
identity_api = IdentityApi(ApiClient(configuration,"CONSENT","consent-token"))
identity =  identity_api.identity_using_get()
```

## Further information

For more information on how to get connected, visit the
[Yapily developer resources](https://github.com/yapily/developer-resources) repo.

###### [Website](https://yapily.com) | [Legal](https://yapily.com/legal-policies) | [Contact Us](mailto:info@yapily.com) 
