from pagarme.resources import handler_request
from pagarme.resources.routes import plan_routes

def create(params):
    return handler_request.post(plan_routes.BASE_URL, params)
