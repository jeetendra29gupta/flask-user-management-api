import requests
from behave import when

from utility import BASE_URL


@when('I create a new user with username "{username}", email "{email}", and salary {salary}')
def step_create_user(context, username, email, salary):
    user_data = {
        "username": username,
        "email": email,
        "salary": float(salary)
    }
    context.response = requests.post(f"{BASE_URL}/users", json=user_data)
