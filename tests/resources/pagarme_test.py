# encoding: utf-8

from pagarme.resources import handler_request
from datetime import datetime, timedelta
import requests
import time


REQUESTBIN_BASE = 'https://requestb.in/api/v1/bins'


def create_postback_url():
    request_bin_response = requests.post(REQUESTBIN_BASE)
    valid_resquest_bin = handler_request.validate_response(request_bin_response)
    if valid_resquest_bin:
        return 'http://requestb.in/'+valid_resquest_bin['name']
    else:
        return 'No postback url'


def generate_timestamp():
    return int(time.mktime((datetime.now()+timedelta(days=3)).timetuple()) * 1000)

auth_test = handler_request.authentication_key(None,True)
