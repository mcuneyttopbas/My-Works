
## CREATED BY MCUNEYTTOPBAS ##

# !!!!!! READ !!!!!
# Default Username : default
# Default Password : 123
# or you can create yourself a new account from Register menu


#Dictionary to store new Accounts and Default Accounts
accounts_dict = {'default': {'name': 'Jason',
                            'surname':'Thompson',
                            'phone':'05334353322',
                            'email':'jason@gmail.com',
                            'username':'default',
                            'password':'123',
                            'mainAccount':5400,
                            'loanAccount':2500},}


def starting_menu():
    menu_title("Starting Menu")
    display_menu("Login","Register","Exit")
    starting_select_item(choose_menu_item("1","2","3"))

#Function to insert menu numbers automatically
def display_menu(*menu_items):
    list(menu_items)
    for i in range(0, len(menu_items)):
        print(f"{i + 1}.{menu_items[i]}")

#Create Title to use same title at all Screens
def menu_title(title):
    print(str(int((60 - len(title))/2) * "*") + f" {title} " + str(int((60 - len(title))/2) * "*"))

#Function for menu item directing
def choose_menu_item(*list_numbers):
    while True:
        choose = input("Please write the Menu Item Number that you want to go: ")
        if choose not in list_numbers:
            print("The Menu item you requested is not exist!")
            continue
        else:
            return choose

#Function to direct starting menu items to adresses
def starting_select_item(select):
    if select == "1":
        login_menu()
    elif select == "2":
        register_menu()
    else:
        exit()

#Function to direct main menu items to adresses
def main_select_item(select,username_entry):
    if select == "1":
        account_info(username_entry)
    elif select == "2":
        deposit_money(username_entry)
    elif select == "3":
        withdraw_money(username_entry)
    elif select == "4":
        loan_money(username_entry)
    else:
        starting_menu()

#Login Menu to check if datas of username and password is added to dictionary
def login_menu():
    menu_title("login")
    print("Provide your credidentials below")
    while True:
        username_entry = input("Please write your username: ")
        password_entry = input("Please write your password: ")

        #Check username and password in dictionary
        if username_entry in accounts_dict and password_entry in (accounts_dict[f"{username_entry}"]["password"]):
            main_menu(username_entry)
            break
        else:
            print("The username or password you provided is WRONG!!")
            continue

#Register Menu to add new Accounts and datas to dictionary exist as default
def register_menu():
    menu_title("Register")
    print("PLease fill the personal information form.")

    name = input("Name: ")
    surname = input("Surname:")

    #Check Tool if there is str or int in Phone Input
    while True:
        phone = input("Phone Number: ")
        is_int = True
        try:
            # convert to integer
            int(phone)
        except ValueError:
            is_int = False
        # print result
        if is_int:
            break
        else:
            print('Please enter a valid Phone Number!')
            continue



    #Check Tool if there is @ in Email Input
    while True:
        email = str(input("Email: "))
        if "@" in email:
            break
        else:
            print("Please enter a valid E-mail adress!")
            continue

    username = input("Username: ")
    password = input("Password: ")

    while True:
        passWAgain = input("Password (Again): ")
        if password == passWAgain:
            break
        else:
            print("Password is not same with your first entry!")
            continue

    #To adding new dictionaries to Nested Dictionary
    accounts_dict[username] = {'name':name,
                               'surname':surname,
                               'phone':phone,
                               'email':email,
                               'username':username,
                               'password':password,
                               'mainAccount':0,
                               'loanAccount':0}

    print("Saving your information...")
    print("Returning to Starting Menu")
    starting_menu()

def main_menu(username_entry):
    menu_title("Main Menu")
    display_menu("Account Information","Deposit Money","Withdraw Money","Apply For Money", "Log-out")
    main_select_item(choose_menu_item("1","2","3","4","5"),username_entry)

#Function show some information on Account and its balances
def account_info(username_entry):
    menu_title("Account Information")
    print(f"Name/Surname: {accounts_dict[username_entry]['name']} {accounts_dict[username_entry]['surname']}")
    print("Contact Information:")
    print(f"          Phone Number: {accounts_dict[username_entry]['phone']} \n          Email: {accounts_dict[username_entry]['email']}")
    print("Balance Information: ")
    print(f"          Primary Account Balance: {accounts_dict[username_entry]['mainAccount']} \n          Loan Account Balance: {accounts_dict[username_entry]['loanAccount']}")

    print("Returning to Main Menu")
    main_menu(username_entry)

#Function that allow the user adding new amount of money on main balance which stored in the dictonary
def deposit_money(username_entry):
    menu_title("Deposit Money")

    print(f"Your current balance in Primary Account is {accounts_dict[username_entry]['mainAccount']}")

    #To check if entry is int or str
    while True:
        deposit_amount = input("Please write the amount you would like to deposit: ")
        is_int = True
        try:
            # convert to integer
            int(deposit_amount)
        except ValueError:
            is_int = False
        # print result
        if is_int:
            break
        else:
            print('Please just use numbers!')
            continue

    #Codes to add new amount of money on Main Account
    accounts_dict[username_entry]['mainAccount'] += int(deposit_amount)
    print(f"Your updated balance is {accounts_dict[username_entry]['mainAccount']}")

    #Codes to check if entry valid or not
    while True:
        again = input("Would you like to deposit again? (Y or N)")
        if again == "Y" or again == "y":
            deposit_money(username_entry)
            break
        elif again == "N" or again == "n":
            print("Returning to Main Menu...")
            main_menu(username_entry)
            break
        elif again.isspace() or again == "":
                print("Please do not use space!")
                continue
        else:
            print("Please enter a valid answer!")
            continue





def withdraw_money(username_entry):
    menu_title("Withdraw Money")

    #Display Balances of Accounts
    print(f"1.Your current balance in Primary Account is {accounts_dict[username_entry]['mainAccount']}")
    print(f"2.Your current balance in Loan Account is {accounts_dict[username_entry]['loanAccount']}")


    while True:
        account_select = input("Please choose from which you would like to withdraw money from: ")
        if account_select == "1":

            #Codes to check if entry valid or not
            while True:
                amount_withdraw = input("Please write the amount you would like to withdraw from your Primary Account: ")
                is_int = True
                try:
                    # convert to integer
                    int(amount_withdraw)
                except ValueError:
                    is_int = False
                # print result
                if is_int:
                    break
                else:
                    print('Please just use numbers!')
                    continue

            #Codes to check if both of account not enough to withdraw so directing to Loan Apply or Main MENU
            while True:
                if int(amount_withdraw) > accounts_dict[username_entry]['mainAccount'] + accounts_dict[username_entry]['loanAccount']:

                    while True:
                        again = input("Sorry your account balance is not enough, would you like to barrow loan?( Y or N): ")
                        if again == "Y" or again == "y":
                            loan_money(username_entry)
                            break
                        elif again == "N" or again == "n":
                            print("Returning to Main Menu...")
                            main_menu(username_entry)
                            break
                        elif again.isspace() or again == "":
                            print("Please do not use space!")
                            continue
                        else:
                            print("Please enter a valid answer!")
                            continue

                #Codes to check if main account is not enough but sum of main and loan account is enough so ask to use loan account as well or directing to main menu
                elif int(amount_withdraw) > accounts_dict[username_entry]['mainAccount'] and int(amount_withdraw) < accounts_dict[username_entry]['mainAccount'] + accounts_dict[username_entry]['loanAccount']:

                    while True:
                        again = input("Sorry your primary account balance is not enough, would you like to use loan account as well?( Y or N): ")
                        if again == "Y" or again == "y":
                            #Codes to take money from main account then take rest of it from loan account
                            backup_account_use_amount = int(amount_withdraw) - accounts_dict[username_entry]['mainAccount']
                            accounts_dict[username_entry]['mainAccount'] = 0
                            accounts_dict[username_entry]['loanAccount'] -= int(backup_account_use_amount)
                            print(f"Your current loan account is {accounts_dict[username_entry]['mainAccount']}$ ")
                            print(f"Your current loan account is {accounts_dict[username_entry]['loanAccount']}$ ")
                            print("Returning to Main Menu...")
                            main_menu(username_entry)
                            break
                        elif again == "N" or again == "n":
                            print("Returning to Main Menu...")
                            main_menu(username_entry)
                            break
                        elif again.isspace() or again == "":
                            print("Please do not use space!")
                            continue
                        else:
                            print("Please enter a valid answer!")
                            continue

                    #Codes which capable to withdraw money from main account if balance is enough
                elif int(amount_withdraw) < accounts_dict[username_entry]['mainAccount']:
                    accounts_dict[username_entry]['mainAccount'] -= int(amount_withdraw)

                    print(f"Your updated balance is {accounts_dict[username_entry]['mainAccount']}")
                    print("Returning to Main Menu...")
                    main_menu(username_entry)


                break

        elif account_select == "2":

            while True:
                amount_withdraw = input("Please write the amount you would like to withdraw from your Loan Account: ")
                is_int = True
                try:
                    # convert to integer
                    int(amount_withdraw)
                except ValueError:
                    is_int = False
                # print result
                if is_int:
                    break
                else:
                    print('Please just use numbers!')
                    continue

            #Codes to direct user to barrow loan if loan Account is not enough
            if int(amount_withdraw) > accounts_dict[username_entry]['loanAccount'] and int(amount_withdraw) > accounts_dict[username_entry]['mainAccount'] + accounts_dict[username_entry]['loanAccount']:

                while True:
                    again = input("Sorry your loan account balance is not enough, would you like to barrow loan?( Y or N): ")
                    if again == "Y" or again == "y":
                        loan_money(username_entry)
                        break
                    elif again == "N" or again == "n":
                        print("Returning to Main Menu...")
                        main_menu(username_entry)
                        break
                    elif again.isspace() or again == "":
                        print("Please do not use space!")
                        continue
                    else:
                        print("Please enter a valid answer!")
                        continue

            #Codes to check if load account is not enough but sum of main and loan account is enough so ask to use loan account as well or directing to main menu
            elif int(amount_withdraw) > accounts_dict[username_entry]['loanAccount'] and int(amount_withdraw) < accounts_dict[username_entry]['mainAccount'] + accounts_dict[username_entry]['loanAccount']:

                    while True:
                        again = input("Sorry your loan account balance is not enough, would you like to use primary account as well?( Y or N): ")
                        if again == "Y" or again == "y":
                            #Codes to take money from main account then take rest of it from loan account
                            backup_account_use_amount = int(amount_withdraw) - accounts_dict[username_entry]['loanAccount']
                            accounts_dict[username_entry]['loanAccount'] = 0
                            accounts_dict[username_entry]['mainAccount'] -= int(backup_account_use_amount)
                            print(f"Your current loan account is {accounts_dict[username_entry]['mainAccount']}$ ")
                            print(f"Your current loan account is {accounts_dict[username_entry]['loanAccount']}$ ")
                            print("Returning to Main Menu...")
                            main_menu(username_entry)
                            break
                        elif again == "N" or again == "n":
                            print("Returning to Main Menu...")
                            main_menu(username_entry)
                            break
                        elif again.isspace() or again == "":
                            print("Please do not use space!")
                            continue
                        else:
                            print("Please enter a valid answer!")
                            continue

            else:
                #withdraw money from loan account if it is enough
                accounts_dict[username_entry]['loanAccount'] -= int(amount_withdraw)
                print(f"Your current loan account is {accounts_dict[username_entry]['mainAccount']}$ ")
                print(f"Your current loan account is {accounts_dict[username_entry]['loanAccount']}$ ")
                print("Returning to Main Menu...")
                main_menu(username_entry)


            break

        else:
            print("Please write a valid entry!")
            continue

def loan_money(username_entry):

    menu_title("Apply For Loan")

    loan_rate = 15  #Loan Rate per year

    print("Please Note that interest rate is %15!")



    #Pay Back Period Input Check
    while True:
        loan_period = input("Please write the time period you would like to pay back: ")
        is_int = True
        try:
            # convert to integer
            int(loan_period)
        except ValueError:
            is_int = False
        # print result
        if is_int:
            break
        else:
            print('Please just use numbers!')
            continue

    #Amount of Loan Input Check
    while True:
        loan_amount = input("Please provide the amount you would like to barrow (max 10.000$) : ")
        s_int = True
        try:
            # convert to integer
            int(loan_amount)
        except ValueError:
            is_int = False
        # print result
        if is_int:
            if int(loan_amount) > 10000:
                print("You can not loan more than 10.000$ ! ")
                continue
            break
        else:
            print('Please just use numbers!')
            continue

    menu_title("Report")

    #Calculating Interest
    payback_amount = ((int(loan_amount)*loan_rate*int(loan_period))/1200)+int(loan_amount)
    monthly_pay_amount = int(payback_amount)/int(loan_period)

    #Total Payment Section
    print(f"Total Payment Amount: {round(payback_amount,2)}$")

    #Loop For Monthly Payments
    for i in range(1,int(loan_period)+1):
        print(f"********* Month #{i} ***********\nTotal Payment Left:{round((int(payback_amount)-monthly_pay_amount*i),2)}$ \nThis Month Installment: {round(monthly_pay_amount,2)}$")

    #Confirmation for Loan
    while True:
        respond = input("Please write 'ok' to confirm and 'cancel' to stop your loan request:  ")
        if respond == "ok" or respond == "Ok" or respond == "OK":
            #Adding Loan to Loan Account and Displaying Account Info Screen
            accounts_dict[username_entry]['loanAccount'] += int(loan_amount)
            print("Your Loan transferring to Loan Account...\nRedirecting to Account Information Menu...")
            account_info(username_entry)
            break
        elif respond == "cancel" or respond == "Cancel" or respond == "CANCEL":
            print("Returning to Main Menu...")
            main_menu(username_entry)
            break
        elif respond.isspace() or respond == "":
            print("Please do not use space!")
            continue
        else:
            print("Please enter a valid answer!")
            continue

def log_out():
    #Option to get back to Starting Menu
    starting_menu()



#To start whole application
starting_menu()
