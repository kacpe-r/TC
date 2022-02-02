def get_api_token():
    with open('../config/token', "r") as data_file:
        return data_file.readline().rstrip()
 