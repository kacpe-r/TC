def get_super_user():
    with open("../superUser", "r") as data_file:
        return data_file.readline().rstrip()
