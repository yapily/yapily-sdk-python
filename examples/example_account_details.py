import uuid,constants,webbrowser
from yapily import ApiClient
from yapily import Configuration
from yapily import AccountAuthorisationRequest
from yapily import ApplicationUsersApi
from yapily import ApplicationUser

from yapily import AccountsApi
from yapily import ConsentsApi
from yapily import IdentityApi
from yapily import InstitutionsApi
from yapily import TransactionsApi


def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    user_api = ApplicationUsersApi(apiClient)

    users_exists = user_api.get_users_using_get(filter_application_user_id=[constants.APPLICATION_USER_ID])
    if not users_exists:
        application_user = ApplicationUser()
        application_user._application_user_id = constants.APPLICATION_USER_ID
        sdk_user = user_api.add_user_using_post_with_http_info(application_user)[0]
        print("Created new sdk user:", sdk_user.application_user_id)
    else:
        sdk_user = users_exists[0]
        print("Using existing sdk user:", constants.APPLICATION_USER_ID)

    accounts_api = AccountsApi(apiClient)
    account_authorisation_request = AccountAuthorisationRequest(
        application_user_id=constants.APPLICATION_USER_ID, 
        institution_id=constants.INSTITUTION_ID,
        callback='',
        one_time_token=''
    )

    response = accounts_api.initiate_account_request_using_post(account_auth_request=account_authorisation_request)
        
    redirect_url = response.data.authorisation_url
    webbrowser.open(redirect_url)

    input("\nPress enter to continue")

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

    print("Consent: " + consent_token)

    institutions_api = InstitutionsApi(apiClient)
    features = institutions_api.get_institution_using_get(constants.INSTITUTION_ID).features
    if ("IDENTITY" in features):
        print("\nGetting identity data: ")

        identity_api = IdentityApi(apiClient)
        identity = identity_api.get_identity_using_get(consent_token)

        print("**************IDENTITY******************")
        print(identity)
        print("****************************************")
    else:
        print("\nCan not get identity information for institution '" + constants.INSTITUTION_ID + "' as it does not have the required feature: 'IDENTITY'")

    print("\nGetting accounts: ")
    accounts = AccountsApi(apiClient).get_accounts_using_get(consent_token)

    print("**************ACCOUNTS******************")
    print(accounts)
    print("****************************************")

    print("\nGetting transactions for account ", accounts.data[0].id + ": ")
    transactionsApi = TransactionsApi(apiClient)
    transactions = transactionsApi.get_transactions_using_get(consent_token, accounts.data[0]._id)

    print("**************TRANSACTIONS**************")
    print(transactions)
    print("****************************************")

def create_callback_with_application_user_id(user_uuid):
    return constants.CALLBACK_URL+ "?application_user_id=" + constants.application_user_id

if __name__ == '__main__':
    main()
