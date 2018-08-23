import uuid

import constants
from yapily import ApiClient
from yapily import Configuration
from yapily import ApplicationUsersApi
from yapily import ApplicationUser
from yapily import NewApplicationUser

def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    user_api = ApplicationUsersApi(apiClient)
    user_api.add_user_using_post(new_application_user())

    print("Created User")

    application_users = user_api.get_users_using_get()

    print(application_users)

    user_api.delete_user_using_delete(application_users[-1]._uuid)

    for user in user_api.get_users_using_get():
        print(user._uuid)


def new_application_user():
    application_user = NewApplicationUser(str(uuid.uuid4()))
    return application_user


if __name__ == '__main__':
    main()


