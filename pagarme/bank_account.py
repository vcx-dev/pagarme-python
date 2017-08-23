from pagarme.resources import handler_request
from pagarme.resources.routes import bank_account_routes


def create(dictionary):
    return handler_request.post(bank_account_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(bank_account_routes.BASE_URL)


def find_by(bank_account_id):
    return handler_request.get(bank_account_routes.GET_BANK_ACCOUNTS_BY.format(bank_account_id))
