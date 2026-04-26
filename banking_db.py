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
