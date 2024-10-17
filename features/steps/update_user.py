import requests
from behave import when

from utility import BASE_URL


@when('I update the user with username "{username}", email "{email}", and salary {salary:d}')
def step_update_user(context, username, email, salary):
    user_data = {
        "username": username,
        "email": email,
        "salary": salary
    }
    context.response = requests.put(f"{BASE_URL}/users/{context.user_id}", json=user_data)
