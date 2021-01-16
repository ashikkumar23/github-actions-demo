import pytest
from assertpy import assert_that
from pytest_bdd import when, scenarios, then, parsers

from step_definitions.test_common import get_request

scenarios('get_employee_data.feature', strict_gherkin=False)


@pytest.fixture(scope='session')
def context():
    return {}


@when('I send a GET HTTP request')
def send_get_request(set_headers, context):
    get_response = get_request(headers=set_headers)
    context['get_response'] = get_response.json()
    context['get_status_code'] = get_response.status_code


@then(parsers.parse('I expect response body to contain status: "{msg}"'))
def validate_get_status_msg(msg, context):
    assert_that(context['get_response']['status']).is_equal_to(msg)


@then('I expect response body to contain all employee data')
def validate_all_employee_data(context):
    assert_that(len(context['get_response']['data'])).is_greater_than(1)


@then(parsers.parse('I expect response body to contain message: "{msg}"'))
def validate_single_employee_response_msg(msg, context):
    assert_that(context['get_response']['message']).is_equal_to(msg)


@then('I expect response body to contain a single employee data')
def validate_single_employee_data(context):
    assert_that(context['get_response']['data']['id']).is_equal_to(int(pytest.globalDict['employee_id']))
