import uuid,constants,webbrowser
from yapily import ApiClient
from yapily import Configuration
from yapily import AccountAuthorisationRequest
from yapily import ApplicationUsersApi
from yapily import ApplicationUser

from yapily import AccountsApi
from yapily import ConsentsApi
from yapily import InstitutionsApi
from yapily import TransactionsApi
from yapily import TransfersApi
from yapily import TransferRequest

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

    print("Consent: " + consent_token);

    accounts = AccountsApi(ApiClient(configuration)).get_accounts_using_get(consent_token)

    print("\nGetting accounts: ")
    accounts = AccountsApi(apiClient).get_accounts_using_get(consent_token)

    print("**************ACCOUNTS******************")
    print(accounts)
    print("****************************************")

    if (len(accounts.data) > 1):

        institutions_api = InstitutionsApi(apiClient)
        features = institutions_api.get_institution_using_get(constants.INSTITUTION_ID).features
        if ("TRANSFER" in features):
            account_id_1 = accounts.data[0].id
            account_id_2 = accounts.data[1].id
            print("\nExecuting a transfer from accout 1 [" + account_id_1 + "] to account 2 [" + account_id_2 + "]:")
            transfers_api = TransfersApi(apiClient)
            transfer = transfers_api.transfer_using_put(
                consent=consent_token,
                account_id=account_id_1,
                transfer_request=TransferRequest(
                    account_id=account_id_2,
                    amount=15.00,
                    currency='GBP',
                    reference='Monthly savings',
                    transfer_reference_id='123456'
                )
            )

            print("**************TRANSFERS**************");
            print(transfer);
            print("****************************************");
        else:
            print("\nCan not execute transfer for institution '" + constants.INSTITUTION_ID + "' as it does not have the required feature: 'TRANSFER'")

    else:
        print("\nYou need to have authorisation to 2 accounts but this Consent only has authorisation for 1. Not executing transfer.")

def create_callback_with_user_uuid(user_uuid):
    return constants.CALLBACK_URL+ "?user_uuid="+user_uuid

if __name__ == '__main__':
    main()

