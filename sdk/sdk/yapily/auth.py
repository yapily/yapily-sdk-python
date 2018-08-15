import urllib.parse

def auth_direct_url(application_uuid, user_uuid, institution_id, callback_url, scope):

    vars = {'application': application_uuid, 'user': user_uuid, 'institution': institution_id, 'callback': callback_url, 'scope':scope}

    return 'https://auth.yapily.com/direct/?' + urllib.parse.urlencode(vars)
