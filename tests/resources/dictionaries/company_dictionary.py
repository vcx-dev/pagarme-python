from tests.resources import pagarme_test

COMPANY = {'company':pagarme_test.create_temporary_company()}

API_KEY = {'api_key':COMPANY['company']['api_key']['test']}