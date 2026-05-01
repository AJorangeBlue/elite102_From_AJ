# Aiden's Bucket Bank App

Welcome to the Bucket Bank App where users can create and access their bank account, deposit, withdraw,
and open their account to view their balance.

## How It Works
1. **Run the application:**
   You can start the application by running:
   ```
   python banking_db.py
   ```
   or just by going the the "banking_db.py" file and pressing the little play button.

2. **Pick a choice...**
   You'll come across a UI that gives you five choices that sound exactly you'd expect:
   Create an Account, Deposit Money, Withdraw Money, Check Balance and Exit Bank.

   You can only use the numbers from 1-5; any number, word, or special characters will give you an error.
   
   

## Usage

- The application initializes a connection to the SQLite database and allows for basic CRUD operations.
- Modify the `src/database/db_setup.py` file to customize the database schema and initial data.

## Development

This project is set up to be used with a development container. You can open it in a containerized environment by using the `.devcontainer` configuration.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
