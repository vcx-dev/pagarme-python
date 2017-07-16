# -*- coding: utf-8 -*-

from tests import pagarme_test

ADDRESS_DICTIONARY = {'address':{'zipcode':'04571020','neighborhood':'Cidade Monções',
'street':'R. Dr. Geraldo Campos Moreira','street_number':'240'}}

COMPANY = {'company':pagarme_test.create_temporary_company()}

VALID_CARD_DICTIONARY = {'api_key':COMPANY['company']['api_key']['test'],'card_number': '4242424242424242','card_cvv': '111','card_holder_name': 'Aardvark da Silva',
'card_expiration_date': '1220'}

UNVALID_CARD_DICTIONARY = {'card_number': '4242424242424242','card_cvv': '611','card_holder_name': 'Aardvark da Silva',
'card_expiration_date': '1220'}

PHONE_DICTIONARY = {'phone': {'number':'987654321','ddd':'11'}}

CUSTOMER_DICTIONARY = {'customer':{'email':'aardvark.silva@gmail.com','name':'Aardvark da Silva',
'document_number':'18152564000105','address':ADDRESS_DICTIONARY['address'],'phone':PHONE_DICTIONARY['phone']}}

UNVALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'api_key':COMPANY['company']['api_key']['test'],'amount':'10000',
'card_number':UNVALID_CARD_DICTIONARY['card_number'],'card_holder_name': UNVALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':UNVALID_CARD_DICTIONARY['card_cvv'],'card_expiration_date':UNVALID_CARD_DICTIONARY['card_expiration_date'],
'customer': CUSTOMER_DICTIONARY['customer']}

VALID_CREDIT_CARD_TRANSACTION_DICTIONARY = {'api_key':COMPANY['company']['api_key']['test'],'amount':'10000',
'card_number':VALID_CARD_DICTIONARY['card_number'],'card_holder_name': VALID_CARD_DICTIONARY['card_holder_name'],
'card_cvv':VALID_CARD_DICTIONARY['card_cvv'],'card_expiration_date':VALID_CARD_DICTIONARY['card_expiration_date'],
'customer': CUSTOMER_DICTIONARY['customer']}