def login():
    username = input("Enter your username: ")
    attempts = 3

    while attempts > 0:
        password = input("Enter your password: ")
        retype_password = input("Re-type your password: ")
        if password == retype_password:
            print("Login successful!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Passwords do not match. You have {attempts} attempts remaining.")
            else:
                print("You have exceeded the maximum number of attempts. Try again later.")
login()