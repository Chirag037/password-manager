import hashlib
import getpass

password_manager={}
def create_account():
    username = input("enter you desired username:")
    password = getpass.getpass("enter your pasword:")
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    password_manager[username]=hashed_password
    print("accounte created succedfully")

def login():
    username = input("enter your username:")
    password = getpass.getpass("enter your password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:
        print("login successful")
    else:
        print("login failed. please check your username and password :")

def main():
    while True:
        print("welcome to password manager")
        print("1 create account :")
        print("2 login ")
        print("3 exit")
        choice = input("enter your choice:")
        if choice =='1':
            create_account()
        elif choice =='2':
            login()
if __name__ == "_main__":
    main()

