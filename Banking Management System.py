def create_account():
    account_no = input(" Enter Account Number : ")
    name = input(" Enter Customer Name : ")
    balance = input(" Enter Initial Balance : ")
    file = open("Banking Management System\Accounts.txt", "a")
    file.write(account_no + "," + name + "," + balance + "\n")
    file.close()
    print(" Account Created Successfully ")

def view_account():
    file = open("Banking Management System\Accounts.txt", "r")
    data = file.read()
    if data == "":
        print(" No Accounts Availale ")
    else :
        print("\n===== Accounts List =====")
        print(data)
    file.close()

def search_account():
    search_acc = input(" Enter Account Number to Search : ")
    file = open("Banking Management System\Accounts.txt", "r")
    found = False
    for line in file:
        data = line.strip().split(",")
        if data[0] == search_acc:
            print(" Account Found ")
            print(" Account Number : ",data[0])
            print(" Name : ",data[1])
            print(" Balance : ",data[2])
            found = True
            break
    file.close()
    if found == False:
        print(" Account Not Found ")

def deposit_money():
    account_no = input(" Enter Account Number : ")
    deposit = int(input(" Enter Deposit Amount : "))
    file = open("Banking Management System\Accounts.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("Banking Management System\Accounts.txt", "w")
    found = False
    for line in lines:
        data = line.strip().split(",")
        if data[0] == account_no:
            balance = int(data[2])
            balance += deposit
            file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
            found = True
        else :
            file.write(line)
    file.close()
    if found == True:
        print(" Amount Deposited Successfully ")
    else :
        print(" Account Not Found ")

def withdraw_money():
    account_no = input(" Enter Account Number : ")
    withdraw = int(input(" Enter Withdrraw Amount : "))
    file = open("Banking Management System\Accounts.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("Banking Management System\Accounts.txt", "w")
    found = False
    for line in lines:
        data = line.strip().split(",")
        if data[0] == account_no:
            balance = int(data[2])
            if withdraw <= balance:
                balance -= withdraw
                file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
                print(" Amount Withdraw Successfully ")
            else :
                file.write(line)
                print(" Insufficient Balance ")
            found = True
        else :
            file.write(line) 
    file.close()
    if found == False :
        print(" Account Not Found ") 

def check_balance():
    account_no = input(" Enter Account Number : ")
    file = open("Banking Management System\Accounts.txt", "r")
    found = False
    for line in file :
        data = line.strip().split(",")
        if data[0] == account_no:
            print("\n====== Account Details ======")
            print(" Account Number : ",data[0])
            print(" Customer Name : ",data[1])
            print(" Current Balance : ",data[2])
            found = True
            break
    file.close()
    if found == False:
        print(" Account Not Found ")

def delete_account():
    delete_acc = input(" Enter Account Number : ")
    file = open("Banking Management System\Accounts.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("Banking Management System\Accounts.txt", "w")
    found = False
    for line in lines:
        data = line.strip().split(",")
        if data[0] != delete_acc:
            file.write(line)
        else:
            found = True
    file.close()
    if found == True:
        print(" Account Deleted Successfully ")
    else :
        print(" Account Not Found ")
            

while True:
    print("\n====== Banking Management System ====== ")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdrow Money")
    print("6. Check Balance")
    print("7. Delete Account")
    print("8. Exit")
    
    choice = input(" Enter Choice : ")

    if choice == "1":
        create_account()
    elif choice == "2":
        view_account()
    elif choice == "3":
        search_account()
    elif choice == "4":
        deposit_money()
    elif choice == "5":
        withdraw_money()
    elif choice == "6":
        check_balance()
    elif choice == "7":
        delete_account()
    elif choice == "8":
        print(" Exit ")
        break
    else :
        print(" Invalid Choice ")
    