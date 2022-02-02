import requests
from config.environment import BASE_URL
from utils.api_token import get_api_token

def delete_user(username):
    URL = BASE_URL + f'/app/rest/users/{username}'
    TOKEN = get_api_token()
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/xml',
        'Content-Type': 'application/json'
    }
    requests.delete(URL, headers = HEADERS)

def create_regular_user(username):
    URL = BASE_URL + '/app/rest/users'
    TOKEN = get_api_token()
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    json_data = {
        'username': username,
        'hasPassword': True,
        'password': f'{username}1',
    }

    requests.post(URL, headers = HEADERS, json = json_data)
