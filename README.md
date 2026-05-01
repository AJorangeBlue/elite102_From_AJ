# Aiden's Bucket Bank App

Welcome to the Bucket Bank App where users can create and access their bank account, deposit, withdraw,
and open their account to view their balance.


## Copy/Fork
1. Upon at the repository, look to where this is a "Fork" button.

2. Click on it, change the name of the repository (if you want), and then click ok/accept to fork it.

3. Click on the green "Code" button, click the tab "Codespaces", click the plus sign (+) to create a codespace on main.

There you go! You have your copy of my bank app.



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


   
3. **What to consider!**
- The entire bank function works once. There is no recursion function that can repeat the entire program; you have to run the program again for it to work.

- Be careful on IDs and the money input (deposit or withdrawal). Sometimes it's easy to get these 2 mixed up; try to slow down and read the prompt that is asking for before entering your input.




## Thank you for testing this out
- Aiden Jaramillo



## Usage

- The application initializes a connection to the SQLite database and allows for basic CRUD operations.
- Modify the `src/database/db_setup.py` file to customize the database schema and initial data.

## Development

This project is set up to be used with a development container. You can open it in a containerized environment by using the `.devcontainer` configuration.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
