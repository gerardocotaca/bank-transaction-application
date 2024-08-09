# Gerardo Cota Canez, CIS 345, Online Session B, PE3
# os allows us to clear the screen in an actual console or terminal
import os
import random

# TODO: modify the users data structure
# key = username, value = account dictionary
# account dictionary has 4 items
# Create objects for balances and transaction
accounts = {'selin2': {'Pin': 9999, 'Name': 'John Doe', 'C': 472.04, 'S': 1000.00}}
account = 1000.00
pin = 0
ans = ''

# Allow 3 invalid pin entries
tries = 1
pin_tries = 1
max_tries = 3
pin_found = False

username = input('Welcome to Cactus Bank.  Please enter your username: ')

if username not in accounts:
    print(f"{username}, Didn't find your username.")
    ans = input("Do you want to create an account (Y/N)? ").lower()
    if ans[0] != 'y':
        print('Thank you for visiting Cactus Bank.  Come back soon.')
        tries = max_tries + 1
    else:
        ans1 = int(input('Enter 1 to create a pin yourself or 2 and the system will create a pin for you: '))
        if ans1 == 1:
            while pin_tries <= max_tries:
                pin = int(input('Select a number between 1 and 9999 as your pin: '))
                print(pin)
                if 0 < pin < 10000:
                    accounts[username] = {'Pin': pin, 'Name': '', 'C': 0, 'S': 0}
                    pin_found = True
                    pin_tries = max_tries + 1
                else:
                    print('Invalid pin entered.')
                    pin_tries += 1
                    if pin_tries > max_tries:
                        print('Please try later ....')
                        tries = max_tries + 1
        elif ans1 == 2:
            pin = random.randint(1, 9999)
            print("Your pin is: ", pin)
            accounts[username] = {'Pin': pin, 'Name': '', 'C': 0, 'S': 0}
            tries = 1
            pin_found = True
        else:
            print('Invalid option! Thank you for visiting Cactus Bank.  Come back soon.')
            tries = max_tries + 1

    if pin_found:
        print("Please remember your pin.")
        print("The system will require you to enter it again.")
        input("Press Enter to continue...")
        # os.system('cls') for windows
        os.system('clear')

while tries <= max_tries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # Determine exit or incorrect pin
    if selection == 'x':
        break
    elif selection != str(accounts[username]['Pin']):
        os.system('cls')
        print(f'Invalid pin. Attempt {tries} of {max_tries}. Please try again.')
        if tries == max_tries:
            print('Locked out! Exiting program.')
            exit()
        tries += 1
    else:
        os.system('cls')
        print(f'Welcome, {accounts[username]["Name"]}!')
        print('Select Account.')
        while True:
            account_type = input('Enter C for Checking or S for Savings: ').upper()
            if account_type == 'C':
                print('\nOpening Checking Account...')
                print('Transaction instructions:')
                print('- Withdrawal enter a negative dollar amount: -20.00.')
                print('- Deposit enter a positive dollar amount: 10.50')

                # Here you can implement the transaction logic for checking account
                transaction = float(input('Enter transaction amount for Checking: '))
                if (transaction + accounts[username]['C']) >= 0:
                    accounts[username]['C'] += transaction
                    print(f'New balance for Checking: ${accounts[username]["C"]:.2f}')
                    print('Transaction complete.')
                else:
                    print('Insufficient Funds. Transaction Cancelled.')
                break
            elif account_type == 'S':
                print('\nOpening Savings Account...')
                print('Transaction instructions:')
                print('- Withdrawal enter a negative dollar amount: -20.00.')
                print('- Deposit enter a positive dollar amount: 10.50')

                # Here you can implement the transaction logic for savings account
                transaction = float(input('Enter transaction amount for Savings: '))
                if (transaction + accounts[username]['S']) >= 0:
                    accounts[username]['S'] += transaction
                    print(f'New balance for Savings: ${accounts[username]["S"]:.2f}')
                    print('Transaction complete.')
                else:
                    print('Insufficient Funds. Transaction Cancelled.')
                break
            else:
                print('Incorrect selection. You must enter C or S.')
        break