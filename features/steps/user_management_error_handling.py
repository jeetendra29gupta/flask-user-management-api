import json

import requests
from behave import when

from utility import BASE_URL


@when('I request a user by ID {user_id}')
def step_request_user_by_id(context, user_id):
    context.response = requests.get(f"{BASE_URL}/users/{user_id}")


@when('I delete the user with ID {user_id}')
def step_delete_user(context, user_id):
    context.response = requests.delete(f"{BASE_URL}/users/{user_id}")


@when('I update the user with ID {user_id}')
def step_update_user(context, user_id):
    user_data = {
        "username": "username",
        "email": "email",
        "salary": "salary"
    }
    context.response = requests.put(f"{BASE_URL}/users/{user_id}", json=user_data)


@when('I partially update the user with ID {user_id}')
def step_partial_update_user(context, user_id):
    user_data = {
        "username": "username",
        "email": "email",
        "salary": "salary"
    }
    context.response = requests.patch(f"{BASE_URL}/users/{user_id}", json=user_data)
