import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_PARAMS = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db():
    """Create a database connection."""
    conn = psycopg2.connect(**DB_PARAMS)
    return conn

def user_exists(username):
    """Check if a user exists in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE username = %s;', (username,))
    exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()
    return exists

def get_password(username):
    """Get the password for a given username."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = %s;', (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

def add_user(username, password):
    """Add a new user to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s);', (username, password))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    logged_in = None
    
    while True:
        command = input("Enter 'login' to log in, 'signup' to create a new account, or 'exit' to quit: ").strip().lower()
        
        if command == "exit":
            print("Exiting the program.")
            break
        
        elif command == "login":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            
            if user_exists(username) and get_password(username) == password:
                logged_in = username
                print("You are now logged in.")
            else:
                print("Invalid username or password.")
        
        elif command == "signup":
            while True:
                new_username = input("Enter a new username: ").strip()
                if user_exists(new_username):
                    print("Username already exists. Please choose a different username.")
                else:
                    break
            
            new_password = input("Enter your password: ").strip()
            add_user(new_username, new_password)
            print("Your account has been created successfully.")
        
        else:
            print("Invalid command. Please enter 'login', 'signup', or 'exit'.")
    
    if logged_in:
        print(f"Logged in user: {logged_in}")
    else:
        print("No user was logged in.")

if __name__ == "__main__":
    main()
