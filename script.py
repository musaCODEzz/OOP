class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display(self):
        print(f"The Username is {self.username} and the email is {self.email}")


user1 = User("John", "John@gmail")
user2 = User("Musa", "Musa@gmail")

user1.display()
user2.display()
print(f"The total number of users are {User.user_count}")
