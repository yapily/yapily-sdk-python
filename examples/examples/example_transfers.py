import uuid,constants,webbrowser
from yapily import auth_direct_url
from yapily import ApiClient
from yapily import Configuration
from yapily import ApplicationUsersApi
from yapily import ApplicationUser

from yapily import AccountsApi
from yapily import ConsentsApi
from yapily import TransactionsApi
from yapily import TransfersApi

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

    institution_id = "monzo";
    app_user_uuid = created_user._uuid

    redirect_url = auth_direct_url(constants.APPLICATION_ID,app_user_uuid,institution_id,create_callback_with_user_uuid(created_user._uuid),"account")
    webbrowser.open(redirect_url)

    input("Press enter to continue")

    consent = ConsentsApi(apiClient).get_user_consents_using_get(app_user_uuid)[0]
    consent_token = consent.consent_token

    print("Consent: " + consent_token);

    accounts =  AccountsApi(ApiClient(configuration)).get_accounts_using_get(consent_token)

    print("**************ACCOUNTS******************")
    print(accounts)
    print("****************************************")

    transactions_api = TransactionsApi(ApiClient(configuration))
    transactions = transactions_api.get_transactions_using_get(consent_token, accounts.data[0]._id)

    print("**************TRANSACTIONS**************");
    print(transactions);
    print("****************************************");

    transfers_api = TransfersApi(ApiClient(configuration))

    path_params = {"accountId": "{{account-id}}"}
    header_params = {
        "consent": consent_token,
        "Accept": 'application/json;charset=utf-8', 'Content-Type': 'application/json;charset=utf-8'}

    body = {
        "accountId": "{{destination-account-id}}",
        "amount": 0.50,
        "currency": "GBP",
        "reference": "Your transaction with yapily",
        "transferReferenceId": str(uuid.uuid4())
    }

    transfer_response = transfers_api.api_client.call_api(
        "/accounts/{accountId}/transfer", "PUT",
        path_params,
        query_params=[],
        header_params=header_params,
        body=body,
        post_params=[],
        files={},
        response_type="ApiResponseOfTransferResponse",  # noqa: E501
        auth_settings=["basicAuth"],
        asyncRequest=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={})

    print("**************TRANSFERS**************");
    print(transfer_response);
    print("****************************************");


def create_callback_with_user_uuid(user_uuid):
    return constants.CALLBACK_URL+ "?user_uuid="+user_uuid

if __name__ == '__main__':
    main()

