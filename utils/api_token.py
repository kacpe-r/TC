def get_api_token():
    with open('../apiToken', "r") as data_file:
        return data_file.readline().rstrip()
 