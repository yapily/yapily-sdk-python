import constants
from yapily.api.institutions_api import InstitutionsApi
from yapily.api_client import ApiClient
from yapily.configuration import Configuration

if __name__ == '__main__':

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    institutionsApi = InstitutionsApi(apiClient)
    institutions = institutionsApi.get_institutions_using_get()

    for institution in institutions:
        print(institution._id)


    institution = institutionsApi.get_institution_using_get(institutions[0]._id)

    print(institution._id)