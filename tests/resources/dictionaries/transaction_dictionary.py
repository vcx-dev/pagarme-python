# -*- coding: utf-8 -*-

from tests.resources.dictionaries import company_dictionary
from tests.resources.dictionaries import card_dictionary
from tests.resources.dictionaries import customer_dictionary

REFUNDED_OR_CAPTURE_TRANSACTION = {'api_key':company_dictionary.API_KEY['api_key'],'amount':'10000'}

UNVALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'api_key':company_dictionary.API_KEY['api_key'],'amount':'10000',
'card_number':card_dictionary.UNVALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.UNVALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.UNVALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.UNVALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION_CAPTURE_FALSE_DICTIONARY = {'api_key':company_dictionary.API_KEY['api_key'],
'amount':'10000', 'capture':'false','card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name':card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'api_key':company_dictionary.API_KEY['api_key'],'amount':'10000',
'card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'],
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}
