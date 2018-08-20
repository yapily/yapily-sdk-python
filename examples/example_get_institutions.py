import constants
from yapily import InstitutionsApi
from yapily import ApiClient
from yapily import Configuration

if __name__ == '__main__':

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    institutionsApi = InstitutionsApi(apiClient)
    institutions = institutionsApi.get_institutions_using_get()

    for institution in institutions.data:
        print(institution._id)


    institution = institutionsApi.get_institution_using_get(institutions.data[0]._id)

    print(institution._id)
