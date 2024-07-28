# Initialize a dictionary with users and their passwords
users = {
    "user1": "password123",
    "user2": "securepass",
    "user3": "mypassword"
}

# Variable to keep track of the logged-in user
logged_in = None

while True:
    # Prompt the user for input
    command = input("Enter 'login' to log in, 'signup' to create a new account, or 'exit' to quit: ").strip().lower()
    
    if command == "exit":
        print("Exiting the program.")
        break
    
    elif command == "login":
        # Ask for username and password
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        # Check if the username and password are correct
        if username in users and users[username] == password:
            logged_in = username
            print("You are now logged in.")
        else:
            print("Invalid username or password.")
    
    elif command == "signup":
        # Ask for a new username
        while True:
            new_username = input("Enter a new username: ").strip()
            if new_username in users:
                print("Username already exists. Please choose a different username.")
            else:
                break
        
        # Ask for the new password
        new_password = input("Enter your password: ").strip()
        
        # Add the new user to the dictionary
        users[new_username] = new_password
        print("Your account has been created successfully.")
    
    else:
        print("Invalid command. Please enter 'login', 'signup', or 'exit'.")
    
# Print the logged-in user at the end of the session (if any)
if logged_in:
    print(f"Logged in user: {logged_in}")
else:
    print("No user was logged in.")
