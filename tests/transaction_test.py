from tests.resources import dictionaries
from pagarme import transaction
from tests.resources.pagarme_test import UNIT_TEST

def test_create_transaction():
    trx = transaction.create(dictionaries.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    assert trx is not None

def test_find_all_transactions():
    all_transactions = transaction.find_all(dictionaries.API_KEY)
    assert all_transactions is not None