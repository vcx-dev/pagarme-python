from pagarme.resources import handler_request
from pagarme.resources.routes import balance_operation_routes


def find_all():
    return handler_request.get(balance_operation_routes.BASE_URL)


def find_by(balance_operation_id):
    return handler_request.get(balance_operation_routes.GET_BALANCE_OPERATIONS_BY.format(balance_operation_id))
