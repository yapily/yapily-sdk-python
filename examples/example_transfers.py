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

    print("\nUsing user:", constants.APPLICATION_USER_ID)

    accounts_api = AccountsApi(apiClient)
    account_authorisation_request = AccountAuthorisationRequest(
        application_user_id=constants.APPLICATION_USER_ID, 
        institution_id=constants.INSTITUTION_ID,
        callback='',
        one_time_token=''
    )

    ## Send the user to the bank to approve the request to retrieve their financial data
    account_authorisation_response = accounts_api.initiate_account_request_using_post(account_auth_request=account_authorisation_request)
    
    ## Store the consent id
    consent_id = account_authorisation_response.data.id

    ## Send the user to the bank to approve the request to retrieve their financial data
    redirect_url = account_authorisation_response.data.authorisation_url
    webbrowser.open(redirect_url)

    ## Wait for the user to authorise before continuing 
    input("\nTo demo transfers, make sure you authorise two accounts at the bank!")
    input("\nPress enter to continue")
    

    # Check the status of the consent object that was created using the consent id
    consent = ConsentsApi(apiClient).get_consent_by_id_using_get(consent_id=consent_id)

    if (consent.data.status == 'AUTHORIZED'):
        consent_token = consent.data.consent_token

        print("\nRetrieved the account consent token: ", consent_token)

        ## Retrieve the account information
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

                ## If more than 2 accounts were authorised and the bank supports transfers, execute a transfer between the first two accounts
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

                print("**************TRANSFERS**************")
                print(transfer)
                print("****************************************")
            else:
                print("\nCan not execute transfer for institution '" + constants.INSTITUTION_ID + "' as it does not have the required feature: 'TRANSFER'")

        else:
            print("\nYou need to have authorisation to 2 accounts but this Consent only has authorisation for 1. Not executing transfer.")
    else:
        print("\nThe user did not authorise sharing their financial data!")

if __name__ == '__main__':
    main()

