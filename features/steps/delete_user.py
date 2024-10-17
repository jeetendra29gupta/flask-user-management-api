import requests
from behave import when

from utility import BASE_URL


@when("I delete the that user")
def step_delete_user(context):
    context.response = requests.delete(f"{BASE_URL}/users/{context.user_id}")
