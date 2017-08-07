# Pagar.me Python

How to use:

#### By importing separate modules

```
from pagarme import transactions

trx = transactions.create({ api_key: 'ak_test_xxx' }, { amount: 1000 })
```

#### By using the API client

```
import pagarme

cli = pagarme.Client(api_key='ak_test_xxx')

trx = cli.transactions.create({ amount: 1000 })
```

