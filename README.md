# Cactus Bank Application

## Overview
The Cactus Bank Application is a simple command-line banking system that allows users to create and manage their accounts, perform transactions, and manage savings and checking accounts. Users can create a new account with a custom or system-generated PIN, deposit or withdraw funds, and check account balances.

## Project Goals
The primary goal of this project is to simulate basic banking operations, such as creating accounts, managing checking and savings accounts, and handling transactions, all within a command-line interface.

## Key Features
- **User Account Creation**: New users can create an account with a custom or system-generated PIN.
- **PIN Authentication**: Users are required to enter their PIN to access their account.
- **Account Management**: Users can manage both checking and savings accounts.
- **Transactions**: Supports both deposits and withdrawals.
- **Multiple Attempts for PIN Entry**: Users have up to 3 attempts to enter the correct PIN.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - `os`: For clearing the console.
  - `random`: For generating a random PIN for new accounts.

## Implementation Details
The application stores user accounts in a dictionary, where each user is identified by a username, and their account details are stored in a nested dictionary. The system allows up to three attempts for users to enter their PIN correctly before being locked out. Users can manage both checking and savings accounts, with simple transaction options for deposits and withdrawals.

## How to Use
1. **Run the Program**: Start the application by running the Python script.
2. **Login or Create Account**: If the username is not found, you will be prompted to create a new account.
3. **Enter PIN**: Upon account creation or login, you will be asked to enter your PIN.
4. **Manage Accounts**: Once logged in, you can choose between checking or savings accounts and perform transactions.
5. **Exit**: You can exit the application at any time by entering 'x' when prompted.

## Future Enhancements
- **Add Interest Calculations**: Implement interest rate calculations for savings accounts.
- **Account Statement**: Provide users with a detailed account statement after transactions.
- **Multiple Users**: Expand the system to handle multiple users simultaneously.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
