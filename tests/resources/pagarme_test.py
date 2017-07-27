# encoding: utf-8

import requests
import unittest
from pagarme.resources import handler_request

UNIT_TEST = unittest.TestCase
TEMPORARY_COMPANY = 'https://api.pagar.me/1/companies/temporary'
REQUESTBIN_BASE = 'https://requestb.in/api/v1/bins'

def create_temporary_company():
    company = requests.post(TEMPORARY_COMPANY)
    valid_company = handler_request.validate_response(company)
    return valid_company

def create_postback_url():
    request_bin_response = requests.post(REQUESTBIN_BASE)
    valid_resquest_bin = handler_request.validate_response(request_bin_response)
    if(valid_resquest_bin):
        return 'http://requestb.in/'+valid_resquest_bin['name']
    else:
        return 'No postback url'