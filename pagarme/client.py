from .request import request

from .subscriptions import Subscriptions
from .transactions import Transactions

class Client:
    def __init__(self, *args, **kw):
        self.authentication = kw['api_key']

        self.transactions = Transactions(self.authentication)
        self.subscriptions = Subscriptions(self.authentication)

