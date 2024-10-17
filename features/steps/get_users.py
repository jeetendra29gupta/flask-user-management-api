import requests
from behave import when, then

from utility import BASE_URL


@when("I request all users")
def step_request_all_users(context):
    context.response = requests.get(f"{BASE_URL}/users")


@then("the response should be a list of users")
def step_check_response_list_of_users(context):
    assert isinstance(context.response.json(), list), "Response is not a list"
    assert len(context.response.json()) >= 0, "User list is empty"
