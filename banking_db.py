import sqlite3

DB_BANK = "banking.db"

def bucket_Bank():
  connect = sqlite3.connect(DB_BANK)
  cursor = connect.cursor()

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

    connect.commit()
    print(f"You deposited ${initial_deposit}.")
    connect.close()


  elif choices == "2":
    connect = sqlite3.connect(DB_BANK)
    cursor = connect.cursor()

    print("\t=== Deposit Money ===")
    print("Accounts:")

    cursor.execute("SELECT * from accounts")
    accounts = cursor.fetchall()
    for acc in accounts:
      print(f"ID: {acc[0]}, Name: {acc[1]}, Balance: ${acc[2]}")

    account_id = int(input("Enter the ID you want to deposit: "))
    depo_amount = float(input("How much do you want to deposit: $"))

    cursor.execute('''
    UPDATE accounts SET balance = balance + ? WHERE id = ?
    ''', (depo_amount, account_id))

    connect.commit()
    print(f"You deposited ${depo_amount} into ID {account_id}")
    print("= = = = = = = = = = =")
    connect.close()


  elif choices == "3":
    connect = sqlite3.connect(DB_BANK)
    cursor = connect.cursor()

    print("\t=== Withdraw Money ===")
    print("Accounts:")

    cursor.execute("SELECT * from accounts")
    accounts = cursor.fetchall()
    for acc in accounts:
      print(f"ID: {acc[0]}, Name: {acc[1]}, Balance: ${acc[2]}")

    account_id = int(input("Enter the ID you want to withdraw: "))
    with_amount = float(input("How much do you want to withdraw: $"))

    # This is to check the sufficient amount
    cursor.execute('''
    SELECT balance FROM accounts WHERE id = ?
    ''', (account_id,))
    balance = cursor.fetchone()[0]

    if(with_amount > balance):
      print("Insufficient funds. Try Again!")
    else:
      cursor.execute('''
    UPDATE accounts SET balance = balance - ? WHERE id = ?
    ''', (with_amount, account_id))

    connect.commit()
    print(f"You withdrew ${with_amount} from ID {account_id}")
    print(f"New Balance: ${balance - with_amount}")
    print("= = = = = = = = = = =")
    connect.close()


  elif choices == "4":
    connect = sqlite3.connect(DB_BANK)
    cursor = connect.cursor()

    print("\t=== Displaying accounts ===")
    print("Accounts:")

    cursor.execute("SELECT * from accounts")
    accounts = cursor.fetchall()

    for acc in accounts:
      print(f"ID: {acc[0]}, Name: {acc[1]}, Balance: ${acc[2]}")

    connect.commit()
    connect.close()


  elif choices == "5":
    print("\nThank you for using Bucket Bank. Goodbye")
    exit()


  else:
    print("Incorrect command. Try again!")


bucket_Bank()
