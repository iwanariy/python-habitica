# coding: utf-8

import ConfigParser
import os


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
    print(load_tokens("token.ini"))


if __name__ == '__main__':
    print(u"Hello, Habatica")

    main()
