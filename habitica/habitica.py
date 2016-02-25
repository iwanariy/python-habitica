# coding: utf-8

import ConfigParser
import os
import requests

BASE_URL = "https://habitica.com:443/api/v2/"


def get_tasks(user, key):
    """
        Get tasks
    """
    headers = {'x-api-user': user, 'x-api-key': key}
    actions = 'user/tasks'

    r = requests.get(BASE_URL + actions, headers=headers)

    return r


def load_tokens(path):
    """
        Get x-api-user & x-api-key from ini file
    """
    if not os.path.exists(path):
        raise Exception("File not found: {0}".format(path))

    # Load config file
    config = ConfigParser.SafeConfigParser()
    config.read(path)

    # Get values
    x_api_user = config.get("token", "x-api-user")
    x_api_key = config.get("token", "x-api-key")

    return (x_api_user, x_api_key)


def main():
    user, key = load_tokens("token.ini")
    r = get_tasks(user, key)


if __name__ == '__main__':
    print(u"Hello, Habatica")

    main()
