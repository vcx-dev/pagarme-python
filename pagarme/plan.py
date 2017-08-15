from pagarme.resources import handler_request
from pagarme.resources.routes import plan_routes

def create(params):
    return handler_request.post(plan_routes.BASE_URL, params)

def find_all():
    return handler_request.get(plan_routes.GET_ALL_PLANS)

def find_by(params):
    return handler_request.get(plan_routes.GET_PLAN_BY_ID, params)

def update(params):
    return handler_request.put(plan_routes.UPDATE_PLAN, params)