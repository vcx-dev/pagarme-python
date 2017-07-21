from tests.resources.dictionaries import transaction_dictionary
from pagarme import transaction
from tests.resources.pagarme_test import UNIT_TEST

def test_create_transaction():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    assert trx['id'] is not None

def test_find_all_transactions():
    all_transactions = transaction.find_all(transaction_dictionary.company_dictionary.API_KEY)
    assert all_transactions is not None

def test_find_by():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    find_trx = transaction.find_by(trx['id'],transaction_dictionary.company_dictionary.API_KEY)
    assert trx['id'] == find_trx['id']

def test_get_all_transction_payables():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    all_payables = transaction.payables(trx['id'],transaction_dictionary.company_dictionary.API_KEY)
    assert all_payables is not None

def test_get_all_transaction_operations():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    all_operations = transaction.operations(trx['id'],transaction_dictionary.company_dictionary.API_KEY)
    assert all_operations is not None

def test_get_all_transaction_events():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    all_events = transaction.events(trx['id'],transaction_dictionary.company_dictionary.API_KEY)
    assert all_events is not None

def test_refund_transaction ():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)
    refunded_transaction = transaction.refund(trx['id'],transaction_dictionary.REFUNDED_OR_CAPTURE_TRANSACTION)
    assert 'refunded' == refunded_transaction['status']

def test_capture_transaction():
    trx = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_CAPTURE_FALSE_DICTIONARY)
    capture_transaction = transaction.capture(trx['id'],transaction_dictionary.REFUNDED_OR_CAPTURE_TRANSACTION)
    assert 'paid' == capture_transaction['status']