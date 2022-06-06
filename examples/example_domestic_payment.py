import uuid,constants,webbrowser,time
from yapily import ApiClient
from yapily import Configuration
from yapily.models import AccountIdentification, AccountIdentificationType
from yapily.models import Address
from yapily.models import Amount
from yapily.models import FrequencyRequest, FrequencyEnumExtended
from yapily.models import Payee, Payer
from yapily.models import PaymentRequest, PaymentType
from yapily.models import PaymentAuthorisationRequest
from yapily.models import PeriodicPaymentRequest
from yapily.apis import ConsentsApi
from yapily.apis import InstitutionsApi
from yapily.apis import PaymentsApi
from yapily.apis import AuthorisationsApi


def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)
    payments_api = PaymentsApi(apiClient)
    authorisation_api = AuthorisationsApi(apiClient)
    print("\nUsing user:", constants.APPLICATION_USER_ID)

    ## Create a domestic payment request payload so be sent immediately
    payment_request = PaymentRequest(
        payment_idempotency_id=str(uuid.uuid4())[:34],
        amount=Amount(
            amount=float(1),
            currency='GBP'
        ),
        reference='TEST PAYMENT',
        type=PaymentType('DOMESTIC_PAYMENT'),
        payee=Payee(
            name='Jane Bloggs',
            account_identifications=[
                AccountIdentification(
                    type=AccountIdentificationType('ACCOUNT_NUMBER'),
                    identification='12345678'
                ),
                AccountIdentification(
                    type=AccountIdentificationType('SORT_CODE'),
                    identification='123456'
                )
            ],
            address=Address(
                country='GB'
            )
        )
    )

    payment_authorisation_request = PaymentAuthorisationRequest(
        application_user_id=constants.APPLICATION_USER_ID, 
        institution_id=constants.INSTITUTION_ID,
        payment_request=payment_request
    )

    ## Execute the payment authorisation request to generate an authorisation url to send the user to the bank
    payment_authorisation_response = authorisation_api.create_payment_authorisation(payment_authorisation_request)

    ## Store the consent id
    consent_id = payment_authorisation_response.data.id

    ## Send the user to the bank to approve the request to make the payment
    redirect_url = payment_authorisation_response.data.authorisation_url
    webbrowser.open(redirect_url)

    ## Wait for the user to authorise before continuing 
    input("\nPress enter to continue AFTER completing the authorisation!")

    ## Check the status of the consent object that was created using the consent id
    consent = ConsentsApi(apiClient).get_consent_by_id(consent_id=consent_id)

    if (consent.data.status == 'AUTHORIZED'):
        consent_token = consent.data.consent_token

        print("\nRetrieved the payment consent token: ", consent_token)
        print("\nExecuting the payment: ")

        ## Execute the payment using the payment request object and consent token issued by the user
        payment= payments_api.create_payment(consent=consent_token, payment_request=payment_request)

        print("\nResponse", payment)

        status = payment.data.status
        if (status == 'PENDING'):
            print("\nChecking the payment status...")
            for x in range(3):

                ## Check the status of the payment if the status is still PENDING
                status = payments_api.get_payments(payment_id=payment.data.id, consent=consent_token).data[0].status
                if (status != 'PENDING'):
                    break
                else:
                    print("\nThe payment is still pending, check again later")
                    time.sleep(2)

        if (status == 'COMPLETED'):
            print("\nThe payment is completed!")
        if (status == 'FAILED'):
            print("\nThe payment failed, please contact your bank")
    else:
        print("\nThe user did not authorise the payment!")

if __name__ == '__main__':
    main()
