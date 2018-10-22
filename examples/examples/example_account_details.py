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
    application_user._reference_id = str(uuid.uuid4())

    created_user = user_api.add_user_using_post_with_http_info(application_user)[0]

    print("Created user",created_user._uuid)

    institution_id = "bbva-sandbox";
    app_user_uuid = created_user._uuid

    redirect_url = auth_direct_url(constants.APPLICATION_ID,app_user_uuid,institution_id,create_callback_with_user_uuid(created_user._uuid),"account")
    webbrowser.open(redirect_url)

    input("Press enter to continue")

    consent = ConsentsApi(apiClient).get_user_consents_using_get(app_user_uuid)[0]
    print("Consent: " + consent.consent_token);
    identity_api = IdentityApi(ApiClient(configuration))
    identity =  identity_api.get_identity_using_get(consent.consent_token)

    print("**************IDENTITY******************")
    print(identity)
    print("****************************************")

    accounts =  AccountsApi(ApiClient(configuration)).get_accounts_using_get(consent.consent_token)

    print("**************ACCOUNTS******************")
    print(accounts)
    print("****************************************")

    transactionsApi = TransactionsApi(ApiClient(configuration))
    transactions = transactionsApi.get_transactions_using_get(consent.consent_token, accounts.data[0]._id)

    print("**************TRANSACTIONS**************");
    print(transactions);
    print("****************************************");

def create_callback_with_user_uuid(user_uuid):
    return constants.CALLBACK_URL+ "?user_uuid="+user_uuid

if __name__ == '__main__':
    main()
