import uuid

import constants
from yapily import ApiClient
from yapily import Configuration
from yapily.apis import UsersApi
from yapily.models import NewApplicationUser

def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    user_api = UsersApi(apiClient)
    app_user_id = "B"
    
    print("\nCreated User with application user Id '" + app_user_id + "':")
    user = user_api.add_user(new_application_user(app_user_id))
    print(user)

    print("\nGetting all users with the application user id: '" + app_user_id + "':")
    application_users = user_api.get_users(
        filter_application_user_id=[app_user_id]
    )
    print(application_users)

    print("\nDeleting the user with application user id '" + app_user_id + "'")
    user_api.delete_user(user.uuid)

    for user in user_api.get_users(filter_application_user_id=[app_user_id]):
        print(user._uuid)


def new_application_user(application_user_uuid):
    application_user = NewApplicationUser(
        application_user_id=application_user_uuid
    )
    return application_user


if __name__ == '__main__':
    main()


