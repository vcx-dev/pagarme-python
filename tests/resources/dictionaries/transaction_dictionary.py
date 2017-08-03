# -*- coding: utf-8 -*-

from tests.resources.dictionaries import card_dictionary
from tests.resources.dictionaries import customer_dictionary
from tests.resources import pagarme_test

BOLETO_TRANSACTION = {'amount': '10000', 'payment_method': 'boleto'}

CALCULATE_INTALLMENTS_AMOUNT = {'amount': '10000', 'free_installments': "1", 'interest_rate': '13',
'max_installments': '12'}

PAY_BOLETO = {'status':'paid'}

REFUNDED_OR_CAPTURE_TRANSACTION = {'amount':'10000'}

INVALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'amount':'10000',
'card_number':card_dictionary.INVALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.INVALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.INVALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.INVALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION_CAPTURE_FALSE_DICTIONARY = {'amount':'10000', 'capture':'false',
'card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name':card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'amount':'10000',
'card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION__WITH_POSTBACK_DICTIONARY = {'amount':'10000',
'card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'], 'postback_url':pagarme_test.create_postback_url(),
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}