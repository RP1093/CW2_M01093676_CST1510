import sqlite3
import pandas as pd

from app_model.db import get_connection
from app_model.users import add_user,get_user
from hashing import generate_hash, is_valid_hash

# user registration 
def register_user(conn):
    name = input("Enter your name:>")
    password = input("Enter your password:>")
    hash_password = generate_hash(password)
    add_user(conn, name, hash_password)

    

# user log in 
def log_in_user(conn):
    name = input('Enter your name:>')
    password = input('Enter your password:>')
    user = get_user(conn, name)
    if user is None: 
        print("User not found!")
        return False
    user_id, user_name, user_hash = user
    print(f"Welcome {user_name} !!")
    if is_valid_hash(password, user_hash):
        return True
    else:
        print("Incorrect password!")
        return False

def main(): 
    while True:
        print('welcome to the system!!')
        print('Choose from the following options:')
        print('1.To Register')
        print('2. To Log in')
        print('3. To Exist')

        choice = input(': > ')

        if choice == '1':
            register_user(conn)
        elif choice == '2':
            if log_in_user(conn):
                print('Log in successfully! ')
            else:
                print('Incorrect log in. Try again !')
        elif choice == '3':
            print('Good Bye!!')
            break 




if __name__ == '__main__':
    main()











































