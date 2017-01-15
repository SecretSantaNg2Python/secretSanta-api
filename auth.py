from flask import g

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth

from argon2 import exceptions
# may need to switch to argon2_cffi, exceptions isn't showing up in this


import models

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='token')
auth = MultiAuth(token_auth, basic_auth)


@basic_auth.verify_password
def verify_password(email_or_username, password):
    try:
        user = models.User.get(
            (models.User.email == email_or_username) |
            (models.User.username == email_or_username)
        )
        if not user.verify_password(password):
            return False
    except models.User.DoesNotExist:
        return False
    except exceptions.VerifyMismatchError:
        return False
    else:
        g.user = user
        return True


@token_auth.verify_token
def verify_token(token):
    user = models.User.verify_auth_token(token)
    if user is not None:
        g.user = user
        return True
    return False
