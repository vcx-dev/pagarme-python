# encoding: utf-8

from resources import API_KEY as API_KEY
from resources.handler_request import *
from resources.routes.transaction_routes import *

def get_transactions (api_key):
    return get(BASE_URL,api_key)

def get_transaction_by(search_param,api_key):
    return get(GET_TRANSACTION_BY.format(search_param),api_key)

def get_all_transaction_payables (transaction_id,api_key):
    return get(GET_ALL_PAYABLES_WITH_TRANSACTION_ID.format(transaction_id),api_key)

def get_all_transactions_opeations (transaction_id,api_key):
    return get(GET_TRANSACTION_OPERATION.format(transaction_id),api_key)

def get_all_transaction_events (transaction_id,api_key):
    return get(GET_EVENTS_TRANSACTION.format(transaction_id),api_key)