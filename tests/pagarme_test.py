# encoding: utf-8

import requests
import unittest
from pagarme.resources import handler_request

UNIT_TEST = unittest.TestCase
HANDLER_REQUEST = handler_request
TEMPORARY_COMPANY = 'https://api.pagar.me/1/companies/temporary'

def create_temporary_company():
    company = requests.post(TEMPORARY_COMPANY)
    valid_company = HANDLER_REQUEST.validate_response(company)
    return valid_company
