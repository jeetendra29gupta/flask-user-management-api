import requests
from behave import given, then

BASE_URL = "http://localhost:8181"


@given("the API is running")
def step_api_running(context):
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200, "API is not running"


@given("a user exists with ID {user_id:d}")
def step_user_exists(context, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"User with ID {user_id} does not exist"
    context.user_id = user_id

@then("the response status should be {status_code:d}")
def step_check_response_status(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, but got {context.response.status_code}"


@then('the response message should be "{expected_message}"')
def step_check_response_message(context, expected_message):
    assert context.response.json()[
               "message"] == expected_message, f"Expected message '{expected_message}', but got '{context.response.json()['message']}'"
