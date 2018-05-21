import uuid

import constants
from yapily import ApiClient
from yapily import Configuration
from yapily import ApplicationUsersApi
from yapily import ApplicationUser

def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    user_api = ApplicationUsersApi(apiClient)
    user_api.add_user_using_post(new_application_user())
    user_api.add_user_using_post_with_http_info(new_application_user())

    application_user_c = new_application_user()
    user_api.add_user_using_post_with_http_info(new_application_user())

    print("Created Users")

    application_users = user_api.get_users_using_get()

    print(application_users)

    user_uuid = application_users[0]._uuid

    user_api.get_user_using_get_with_http_info(user_uuid)

    for application_user in application_users:
        print(application_user._app_user_id)

    application_user_c._app_user_id = "UserC"

    upd = user_api.update_user_using_put(str(application_user_c._uuid),application_user_c)

    print("Updated application user")

    updated_application_users = user_api.get_users_using_get()

    for application_user in updated_application_users:
        print(application_user._app_user_id)

def new_application_user():
    application_user = ApplicationUser()
    application_user.uuid = str(uuid.uuid4())
    return application_user


if __name__ == '__main__':
    main()

