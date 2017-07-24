# -*- coding: utf-8 -*-

from tests.resources.dictionaries import company_dictionary
from tests.resources.dictionaries import card_dictionary
from tests.resources.dictionaries import customer_dictionary

BOLETO_TRANSACTION = {'api_key': company_dictionary.API_KEY['api_key'], 'amount': '10000', 'payment_method': 'boleto'}

CALCULATE_INTALLMENTS_AMOUNT = {'api_key': company_dictionary.API_KEY['api_key'], 'amount': '10000', 'free_installments': "1",
'interest_rate': '13', 'max_installments': '12'}

PAY_BOLETO = {'api_key':company_dictionary.API_KEY['api_key'],'status':'paid'}

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
'card_number':card_dictionary.VALID_CARD_DICTIONARY['card_number'], 'postback_url':'https://requestb.in/1bkne711',
'card_holder_name': card_dictionary.VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':card_dictionary.VALID_CARD_DICTIONARY['card_cvv'],
'card_expiration_date':card_dictionary.VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': customer_dictionary.CUSTOMER_DICTIONARY['customer']}
