import sqlite3

BD_BANK = "banking.db"

def bucket_Bank:
  connect = sqlite3.connect(DB_BANK)
  cursor = connectcursor()

  #create Table
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance REAL
    )
  ''')

  connect.commit()
  connect.close()

  print("  === Bucket Bank ===")
  print("=======================")
  print("| 1. Create Account  |")
  print("| 2. Deposit Money   |")
  print("| 3. Withdraw Money  |")
  print("| 4. Check Balance   |")
  print("| 5. Exit Bank       |")
  print("=======================")
  print(" ====================")

  choices = input("Enter your options (1-5): ")

  if choices == "1":
    connect = sqlite3.connect(DB_BANK)
    cursor = connect.cursor()
    name = input("Enter the full name to your account: ")
    initial_deposit = float(input("Enter how much you want to deposit: $"))
    
    cursor.execute('''
    INSERT INTO accounts (name, balance) VALUES (?,?) 
    ''', (name, initial_deposit))





