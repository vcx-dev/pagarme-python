from pagarme.resources import handler_request
from tests.resources.pagarme_test import auth_test


def test_authentication_key():
    auth = handler_request.authentication_key(auth_test['api_key'])
    assert auth['api_key'] == auth_test['api_key']
