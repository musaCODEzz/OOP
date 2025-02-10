from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f"email accessed at {datetime.now()}")
        return self._email.upper().strip()

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("John", "  John@gmail", 1234)
user1.email = "musa@gmail"
print(user1.email)
