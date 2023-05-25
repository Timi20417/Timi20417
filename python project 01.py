
def security_system():
    registered_users = {}

    def register():
        username = input("Enter a username: ")
        passcode = input("Enter a passcode: ")
        registered_users[username] = passcode
        print("Registration successful!")

    def login():
        username = input("Enter your username: ")
        passcode = input("Enter your passcode: ")

        if username in registered_users and registered_users[username] == passcode:
            print("Access granted. Welcome, " + username + "!")
        else:
            print("Access denied. Invalid username or passcode.")

    register()
    login()

security_system()
