USERS = [
    {'login': 'admin', 'password': 'admin1', 'is_admin': True},
    {'login': 'regular', 'password': 'regular1', 'is_admin': False}
]

def get_user_by_role(is_admin):
    return next((user for user in USERS if user['is_admin'] == is_admin), None)
