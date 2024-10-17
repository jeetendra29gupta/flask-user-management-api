import requests
from behave import when

from utility import BASE_URL


@when('I partially update the user with username "{username}"')
def step_partial_update_user(context, username):
    user_data = {"username": username}
    context.response = requests.patch(f"{BASE_URL}/users/{context.user_id}", json=user_data)
