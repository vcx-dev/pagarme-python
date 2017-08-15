from tests.resources.dictionaries import plan_dictionary
from pagarme import plan

def test_create_plan():
    _plan = plan.create(plan_dictionary.plan_DICTIONARY)
    assert _plan['id'] is not None


def test_find_all_plans():
    all_plans = plan.find_all()
    assert all_plans is not None


def test_find_by():
    _plan = plan.create(plan_dictionary.plan_DICTIONARY)
    find_plan= plan.find_by(_plan['id'])
    assert _plan['id'] == find_plan['id']
