class User:
    # create the class attributes
    users = []
    n_active = 0

    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name

        if active:
            User.n_active += 1
            User.users.append(user_name)
