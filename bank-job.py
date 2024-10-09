# reads user data from data.txt
def load_data(filename):
    bank_users = {}
    with open(filename,'r') as user_info:
        for line in user_info:
            if line:
                username, password, name, balance = line.split(',')
                bank_users[username] = {
                    'password': password,
                    'Name': name.strip(),
                    'Balance': balance
                }
    return bank_users

#find user function
def find_user(bank_users, username, password):
    user = bank_users.get(username)
    if user and user['password'] == password:
        return user
    else:
        return None
    
#login function
def login():
    bank_users = load_data('data.txt')

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    user = find_user(bank_users, username, password)

    if user:
        print(f"Hello, {user['Name']}!")
        print(f"You have a balance of: {user['Balance']}.")
    else:
        print("Invalid Password")

login()