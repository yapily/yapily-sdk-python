import uuid,constants,webbrowser
from yapily import ApiClient
from yapily import Configuration
from yapily import AccountAuthorisationRequest

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

    print("\nUsing user:", constants.APPLICATION_USER_ID)

    accounts_api = AccountsApi(apiClient)
    account_authorisation_request = AccountAuthorisationRequest(
        application_user_id=constants.APPLICATION_USER_ID, 
        institution_id=constants.INSTITUTION_ID,
        callback='',
        one_time_token=''
    )

    ## Execute the account authorisation request to generate an authorisation url to send the user to the bank
    account_authorisation_response = accounts_api.initiate_account_request_using_post(account_auth_request=account_authorisation_request)

    ## Store the consent id
    consent_id = account_authorisation_response.data.id
        
    ## Send the user to the bank to approve the request to retrieve their financial data
    redirect_url = account_authorisation_response.data.authorisation_url
    webbrowser.open(redirect_url)

    ## Wait for the user to authorise before continuing 
    input("\nPress enter to continue AFTER completing the authorisation!")

    ## Check the status of the consent object that was created using the consent id
    consent = ConsentsApi(apiClient).get_consent_by_id_using_get(consent_id=consent_id)

    if (consent.data.status == 'AUTHORIZED'):
        consent_token = consent.data.consent_token

        print("\nRetrieved the account consent token: ", consent_token)

        institutions_api = InstitutionsApi(apiClient)

        ## If the bank supports identity data, retrieve the identity information
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

        ## Retrieve the account information
        print("\nGetting accounts: ")
        accounts = AccountsApi(apiClient).get_accounts_using_get(consent_token)

        print("**************ACCOUNTS******************")
        print(accounts)
        print("****************************************")

        ## Retrieve the transactions for the first account
        print("\nGetting transactions for account ", accounts.data[0].id + ": ")
        transactionsApi = TransactionsApi(apiClient)
        transactions = transactionsApi.get_transactions_using_get(consent_token, accounts.data[0]._id)

        print("**************TRANSACTIONS**************")
        print(transactions)
        print("****************************************")
    else:
        print("\nThe user did not authorise sharing their financial data!")

if __name__ == '__main__':
    main()
