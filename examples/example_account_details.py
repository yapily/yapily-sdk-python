import uuid,constants,webbrowser
from yapily import auth_direct_url
from yapily import ApiClient
from yapily import Configuration
from yapily import ApplicationUsersApi
from yapily import ApplicationUser

from yapily import AccountsApi
from yapily import ConsentsApi
from yapily import IdentityApi
from yapily import TransactionsApi


def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    user_api = ApplicationUsersApi(apiClient)

    application_user = ApplicationUser()
    application_user._app_user_id = str(uuid.uuid4())

    created_user = user_api.add_user_using_post_with_http_info(application_user)[0]

    print("Created user",created_user._uuid)

    institution_id = "bbva-sandbox";
    app_user_uuid = created_user._uuid

    redirect_url = auth_direct_url(constants.APPLICATION_ID,app_user_uuid,institution_id,constants.CALLBACK_URL,"account")
    webbrowser.open(redirect_url)

    input("Press enter to continue")

    consent = ConsentsApi(apiClient).get_user_consents_using_get(app_user_uuid)[0]

    identity_api = IdentityApi(ApiClient(configuration,"CONSENT",consent._consent_token))
    identity =  identity_api.identity_using_get()

    print("**************IDENTITY******************")
    print(identity)
    print("****************************************")

    accounts =  AccountsApi(ApiClient(configuration,"CONSENT",consent._consent_token)).get_accounts_using_get()

    print("**************ACCOUNTS******************")
    print(accounts)
    print("****************************************")

    transactionsApi = TransactionsApi(ApiClient(configuration,"CONSENT",consent._consent_token))
    transactions = transactionsApi.get_transactions_using_get(accounts[0]._id)

    print("**************TRANSACTIONS**************");
    print(transactions);
    print("****************************************");

if __name__ == '__main__':
    main()
