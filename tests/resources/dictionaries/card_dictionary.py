# -*- coding: utf-8 -*-

from tests.resources.dictionaries import company_dictionary

UNVALID_CARD_DICTIONARY = {'card_number': '4242424242424242','card_cvv': '611','card_holder_name': 'Aardvark da Silva',
'card_expiration_date': '1220'}

VALID_CARD_DICTIONARY = {'api_key':company_dictionary.API_KEY['api_key'],'card_number': '4242424242424242','card_cvv': '111','card_holder_name': 'Aardvark da Silva',
'card_expiration_date': '1220'}