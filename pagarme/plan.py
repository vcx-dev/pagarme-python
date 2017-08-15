from pagarme.resources import handler_request
from pagarme.resources.routes import plan_routes

def create(params):
    return handler_request.post(plan_routes.BASE_URL, params)

def find():
    return handler_request.get(plan_routes.GET_ALL_PLANS)
