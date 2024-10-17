import requests
from behave import when

from utility import BASE_URL


@when('I create a new user with username "{username}" and salary {salary}')
@when('I create a new user with username "{username}" and email "{email}"')
@when('I create a new user with email "{email}" and salary {salary}')
def step_create_user(context, username=None, salary=None, email=None):
    payload = {}
    if username:
        payload['username'] = username
    if email:
        payload['email'] = email
    if salary:
        payload['salary'] = salary

    context.response = requests.post(f"{BASE_URL}/users", json=payload)
