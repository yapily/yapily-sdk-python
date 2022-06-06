import constants
from yapily.apis import InstitutionsApi
from yapily import ApiClient
from yapily import Configuration

if __name__ == '__main__':

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    institutionsApi = InstitutionsApi(apiClient)
    institutions = institutionsApi.get_institutions()

    print("GET /institutions")
    for institution in institutions.data:
        print(institution.id)

    print("\nGET /institution/{{institution-id}}")
    institution = institutionsApi.get_institution(institutions.data[0].id)

    print(institution.id)
