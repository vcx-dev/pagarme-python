from tests import dictionaries
from pagarme import transaction
from tests.pagarme_test import UNIT_TEST

def test_create_transaction():
    trx = transaction.create(dictionaries.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    assert trx is not None