import requests
from behave import when, then

from utility import BASE_URL


@when("I request that user")
def step_request_user(context):
    context.response = requests.get(f"{BASE_URL}/users/{context.user_id}")


@then('the user details should include username "{expected_username}"')
def step_check_user_details(context, expected_username):
    user_data = context.response.json()
    assert user_data[
               'username'] == expected_username, f"Expected username '{expected_username}', but got '{user_data['username']}'"
