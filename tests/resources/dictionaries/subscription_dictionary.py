from tests.resources.dictionaries import card_dictionary
from tests.resources.dictionaries import customer_dictionary
from tests.resources.dictionaries import plan_dictionary
from tests.resources.dictionaries import transaction_dictionary
from tests.resources import pagarme_test
from pagarme import card
from pagarme import plan

NO_TRIAL_PLAN = plan.create(plan_dictionary.NO_TRIAL_PLAN)

CARD = card.create(card_dictionary.VALID_CARD_DICTIONARY)

POSTBACK_URL = pagarme_test.create_postback_url()

BOLETO_SUBSCRIPTION = {
    "plan_id": NO_TRIAL_PLAN['id'],
    "customer": customer_dictionary.CUSTOMER_DICTIONARY,
    "payment_method": "boleto",
    "postback_url": POSTBACK_URL
}


CREDIT_CARD_SUBSCRIPTION = {
    "plan_id": NO_TRIAL_PLAN['id'],
    "customer": customer_dictionary.CUSTOMER_DICTIONARY,
    "card_id": CARD['id'],
    "payment_method": "credit_card",
    "postback_url": POSTBACK_URL
}

UPDATE = {
    "payment_method": "boleto"
}

CHARGES = {
    "charges": "1"
}

BOLETO_SPLIT_RULE_SUBSCRIPTION = {
    "plan_id": NO_TRIAL_PLAN['id'],
    "customer": customer_dictionary.CUSTOMER_DICTIONARY,
    "payment_method": "boleto",
    "postback_url": POSTBACK_URL,
    "split_rules": transaction_dictionary.SPLIT_RULE_PERCENTAGE
}

CREDIT_CARD_PERCENTAGE_SPLIT_RULE_SUBSCRIPTION = {
    "plan_id": NO_TRIAL_PLAN['id'],
    "customer": customer_dictionary.CUSTOMER_DICTIONARY,
    "card_id": CARD['id'],
    "payment_method": "credit_card",
    "postback_url": POSTBACK_URL,
    "split_rules": transaction_dictionary.SPLIT_RULE_PERCENTAGE
}

BOLETO_PERCENTAGE_SPLIT_RULE_SUBSCRIPTION = {
    "plan_id": NO_TRIAL_PLAN['id'],
    "customer": customer_dictionary.CUSTOMER_DICTIONARY,
    "card_id": CARD['id'],
    "payment_method": "boleto",
    "postback_url": POSTBACK_URL,
    "split_rules": transaction_dictionary.SPLIT_RULE_PERCENTAGE
}