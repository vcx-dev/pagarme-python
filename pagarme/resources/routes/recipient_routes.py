BASE_URL = 'https://api.pagar.me/1/recipients'

GET_ALL_RECIPIENTS = BASE_URL

GET_RECIPIENT_BY_ID = BASE_URL + '/{recipient_id}'

UPDATE_RECIPIENT = BASE_URL + '/{recipient_id}'

GET_RECIPIENT_BALANCE = BASE_URL + '{recipient_id}/balance'

GET_RECIPIENT_BALANCE_OPERATIONS = BASE_URL + '{recipient_id}/balance/operations'

GET_RECIPIENT_BALANCE_OPERATION_BY_ID = BASE_URL + '{recipient_id}/balance/operations/{balance_operation_id}'
