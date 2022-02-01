import requests
from utils.api_token import get_api_token
from utils.environment import BASE_URL
from xml.etree import ElementTree

def delete_all_groups():
    URL = BASE_URL + '/app/rest/userGroups'
    TOKEN = get_api_token()
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(URL, headers=HEADERS)
    root = ElementTree.fromstring(response.content)
    for child in root.iter('group'):
        if child.attrib['name'] != 'All Users':
            delete_group(child.attrib['key'])

def delete_group(group_name):
    URL = BASE_URL + f'/app/rest/userGroups/{group_name}'
    TOKEN = get_api_token()
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}'
    }

    requests.delete(URL, headers = HEADERS)

def create_group(group_name, username):
    URL = BASE_URL + '/app/rest/userGroups'
    TOKEN = get_api_token()
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    json_data = {
        'key': group_name,
        'name': group_name,
        'users': {
            'count': 1,
            'user': [
                {
                    'username': username
                }
            ]
        }
    }

    requests.post(URL, headers = HEADERS, json = json_data)
