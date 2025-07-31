from models.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def add(self, user: User):
        self.users.append(user)

    def get_all(self):
        return self.users

    def get_by_id(self, user_id: str):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_by_name(self, name: str):
        for user in self.users:
            if user.name == name:
                return user
        return None