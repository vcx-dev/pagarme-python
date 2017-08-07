from .request import request

class Transactions:
    def __init__(self, opts):
        self.opts = opts

    def create(self, body):
        create(self.opts, body)

def create(opts, body):
    request.post(opts, body)
