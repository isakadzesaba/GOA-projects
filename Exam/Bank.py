all_accounts = []

def create_acc():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    data_output = input("create acc? ")

    if data_output.lower() == "yes":
        account = {
            "username": username,
            "password": password,
            "balance": 0
        }
        all_accounts.append(account)
        print("Account created successfully username: ", username)
    else:
        print("No acc created")
    
# 2
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for acc in all_accounts:
        if acc["username"] == username and acc["password"] == password:
            return acc
    return None

def update_acc(account):
    print("Current username:", account["username"])
    updated_username = input("Enter new username: ")
    if updated_username:
        account["username"] = updated_username


    updated_password = input("Enter new password: ")
    if updated_password:
        account["password"] = updated_password
    
    print("Acc info UpDated.")

def delete_acc():
    pass

def search_acc(username):
    for acc in all_accounts:
        if acc["username"] == username:
            print("username:", acc["username"])
            print("password:", acc["password"])
            print("balance:", acc["balance"])
    print(f"Acc {username} not found")

def customers():
    if all_accounts:
        print("Our customers: ")
        for acc in all_accounts:
            print("Username: ", acc["username"])
            print("balance: ", acc["balance"])
            print("We can't tell you all passwords :)")

    else:
        print("No customers found :( ")

def menu(account):
    while True:
        print("1. withdrawal")
        print("2. deposit")
        print("3. check balance")
        print("4. Update acc info")
        print("5. Delete acc :(")
        print("6. Search acc info")
        print("7. View customers")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            withdrawal_amount = float(input("Enter the amount: "))
            if withdrawal_amount > account["balance"]:
                print("You don't have enough money")
            else:
                account["balance"] -= withdrawal_amount
                print("withdrawal successful. balance: ")
                print("  ")
                print("  ")
                print("  ")
                print(account["balance"])
                print("  ")
                print("  ")
                print("  ")
        elif choice == "2":
            deposit_amount = float(input("Enter the amount: "))
            account["balance"] += deposit_amount
            print("deposit successful. balance: ")
            print("  ")
            print("  ")
            print("  ")
            print(account["balance"])
            print("  ")
            print("  ")
            print("  ")
        
        elif choice == "3":
            print("balance: ")
            print("  ")
            print("  ")
            print("  ")
            print(account["balance"])
            print("  ")
            print("  ")
            print("  ")
        elif choice == "4":
            update_acc(account)
        
        elif choice == "5":
            delete_acc(account["username"])
            break

        elif choice == "6":
            username = input("Enter username (to search): ")
            search_acc(username)

        elif choice == "7":
            customers()

        elif choice == "8":
            print("Exiting ...")
            break


while True:
    print("1. create Account")
    print("2. Login")
    print("3. Exit")


    option = input("choose: ")

    if option == "1":
        create_acc()
    elif option == "2":
        account = login_user()
        
        if account:
            print("Login successful")
            menu(account)

        else:
            print("Please try agein")
    elif option == "3":
        print("Exiting ...")
        break
    
    else:
        print("choose 1-3: ")



print("Thank you.")
for i in range(10):
    print("Bye", "Bye", "❤️")