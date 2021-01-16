import pytest
import requests
from pytest_bdd import given, when, parsers

from helpers.environment import Env


@given(parsers.parse('I set Dummy Rest API URL to "{env}"'))
def set_dummy_rest_api_base_url(env):
    dummy_rest_api_base_url = Env.get_dummy_rest_api_version(env)
    pytest.globalDict['dummy_rest_api_base_url'] = dummy_rest_api_base_url


@given(parsers.parse('I set Dummy Rest API GET route to "{route}" for all employees'))
def set_dummy_rest_api_route_all_employees(route):
    pytest.globalDict['api_endpoint'] = pytest.globalDict['dummy_rest_api_base_url'] + route


@given(parsers.parse('I set Dummy Rest API GET route to "{route}" for single employee'))
def set_dummy_rest_api_route_single_employee(route):
    api_route = route.split('{')[0]
    emp_id = (route.split('{')[-1]).split('}')[0]
    pytest.globalDict['employee_id'] = Env.get_employee_id(emp_id)
    pytest.globalDict['api_endpoint'] = pytest.globalDict['dummy_rest_api_base_url'] + api_route + pytest.globalDict['employee_id']


@pytest.fixture
@when(parsers.parse('I set User-Agent as "{user_agent}" in headers'))
def set_headers(user_agent):
    return {'User-Agent': user_agent}


def get_request(headers):
    get_url = pytest.globalDict['api_endpoint']
    response = requests.get(f'{get_url}', headers=headers)
    print(
        f'Request Method: GET \n'
        f'Request URL: {get_url} \n'
        f'Request Headers: {headers} \n'
        f'Response Status Code: {response.status_code}\nResponse Body: {response.json()}'
    )
    return response
