import sqlite3
from pandas import DataFrame


connection=sqlite3.connect("finnance_data.db")

def create_tables():
    create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts (
        id_account INTEGER PRIMARY KEY,
        institution TEXT,
        description TEXT,
        active TEXT
    );"""
    
    create_account_record_table = """CREATE TABLE IF NOT EXISTS account_value (
        id_record INTEGER PRIMARY KEY,
        account INTEGER,
        ammount REAL,
        date REAL,
        FOREIGN KEY (account) REFERENCES accounts(id_account)
    );"""

    create_budget_table = """CREATE TABLE IF NOT EXISTS budget (
        id_cat INTEGER PRIMARY KEY,
        spend_cat INTEGER,
        monthly_budget REAL,
        active TEXT
    );"""

    create_spend_table = """CREATE TABLE IF NOT EXISTS spend_daily (
        id_spend INTEGER PRIMARY KEY,
        spend_cat_id INTEGER,
        ammount REAL,
        date REAL,
        FOREIGN KEY (spend_cat_id) REFERENCES budget(id_cat)
    );"""

    with connection:
        connection.execute(create_accounts_table)
        connection.execute(create_account_record_table)
        connection.execute(create_budget_table)
        connection.execute(create_spend_table)


def create_account(user_institution, user_description):
    create_account = "INSERT INTO accounts (institution, description, active) VALUES (?, ?, ?);"
    with connection:
        connection.execute(create_account, (user_institution, user_description, True))


def active_accounts(active=True):
    if active == True:
        get_active_accounts = "SELECT * FROM accounts WHERE active = True;"
    else:
        get_active_accounts = "SELECT * FROM accounts;"
        
    cursor = connection.cursor()
    with connection:
        cursor.execute(get_active_accounts,)
    return cursor.fetchall()


def deactivate_account(account_id_deactive):
    update_active_account = "UPDATE accounts SET active = False WHERE id_account = ?;"
    with connection:
        connection.execute(update_active_account, (account_id_deactive,))


def add_account_record(account, value, today_date):
    add_account_record = "INSERT INTO account_value (account, ammount, date) VALUES (?, ?, ?);"
    with connection:
        connection.execute(add_account_record, (account, value, today_date))


def summary_total():
    time_summary = "SELECT date, SUM(ammount) FROM account_value GROUP BY date;"
    cursor = connection.cursor()
    with connection:
        cursor.execute(time_summary)

    df = DataFrame(cursor.fetchall())
    df = df.rename(columns={0: "Date", 1: "AccountTotal"})
    return df

def create_spend_cat(spend_cat_new, monthly_budget):
    create_account = "INSERT INTO budget (spend_cat, monthly_budget, active) VALUES (?, ?, ?);"
    with connection:
        connection.execute(create_account, (spend_cat_new, monthly_budget, True))

def active_spend_cat(active=True):
    if active == True:
        get_active_spend_cat = "SELECT * FROM budget WHERE active = True;"
    else:
        get_active_spend_cat = "SELECT * FROM budget;"
        
    cursor = connection.cursor()
    with connection:
        cursor.execute(get_active_spend_cat,)
    return cursor.fetchall()


def update_spend_cat(spend_cat_update, monthly_budget_update):
    update_active_account = "UPDATE budget SET monthly_budget = ? WHERE id_cat = ?;"
    with connection:
        connection.execute(update_active_account, (monthly_budget_update, spend_cat_update))

def add_spend_record(spend_cat, spend_ammount, spend_date):
    add_spend_record = "INSERT INTO spend_daily (spend_cat_id, ammount, date) VALUES (?, ?, ?);"
    with connection:
        connection.execute(add_spend_record, (spend_cat, spend_ammount, spend_date))


# def sum_spend_month();
#     sum_record = """
#                 SELECT strftime('%Y-%m', date) AS sales_month
#                  , sum(amount) AS total_sales
#                 FROM sales
#                 GROUP BY sales_month
#                 ORDER BY sales_month
#     """
