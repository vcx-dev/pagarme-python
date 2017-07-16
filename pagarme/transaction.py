# encoding: utf-8

from pagarme.resources import API_KEY as API_KEY
from pagarme.resources import handler_request
from pagarme.resources.routes import transaction_routes

def find_all (api_key):
    return handler_request.get(transaction_routes.BASE_URL,api_key)

def find_by(search_param,api_key):
    return handler_request.get(transaction_routes.GET_TRANSACTION_BY.format(search_param),api_key)

def payables (transaction_id,api_key):
    return handler_request.get(transaction_routes.GET_ALL_PAYABLES_WITH_TRANSACTION_ID.format(transaction_id,),api_key)

def operations (transaction_id,api_key):
    return handler_request.get(transaction_routes.GET_TRANSACTION_OPERATION.format(transaction_id),api_key)

def events (transaction_id,api_key):
    return handler_request.get(transaction_routes.GET_EVENTS_TRANSACTION.format(transaction_id),api_key)

def create(dictionary):
    return handler_request.post(transaction_routes.BASE_URL,dictionary)

def capture (transaction_id, dictionary):
    return handler_request.post(transaction_routes.CAPTURE_TRANSACTION_AFTER.format(transaction_id), dictionary)

def refund (transaction_id, dictionary):
    return handler_request.post(transaction_routes.REFUND_TRANSACTION.format(transaction_id),dictionary)
