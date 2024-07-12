import datetime
import pandas as pd
import matplotlib.pyplot as plt
import database

def list_active_accounts():
    active_account = database.active_accounts()
    print("--- Active Accounts ---")
    for account in active_account:
        if account[3] == "1": #Checks to see if account is active
            print(f"Account {account[2]} at {account[1]}: ID = {account[0]}")
    

def old_saving():
    active_account = database.active_accounts(active=False)

    time_str = input("Enter date format yyyy-mm-dd")
    time = datetime.datetime.strptime(time_str, "%Y-%m-%d")
    time = time.timestamp()

    print("\n")
    print(" --- Input account value USD ---")
    
    for account in active_account:
        if account[3] == "1": #Checks to see if account is active
            value = input(f"Account {account[2]} at {account[1]}: ")
            database.add_account_record(account[0], value, time)
    print(" --- END of ACTIVE accounts ---")
    print("\n\n")


def deactivate_account():
    list_active_accounts()
    account_to_deactive = input("Select account ID to devativate or q: ")
    if account_to_deactive != "q":
        database.deactivate_account(account_to_deactive)


def update_saving():
    active_account = database.active_accounts()

    today_date = datetime.datetime.today()
    today_date = today_date.timestamp()
    
    print("\n")
    print(" --- Input account value USD ---")
    
    for account in active_account:
        if account[3] == "1": #Checks to see if account is active
            value = input(f"Account {account[2]} at {account[1]}: ")
            database.add_account_record(account[0], value, today_date)
    print(" --- END of ACTIVE accounts ---")
    print("\n\n")


def add_new_saving():
    institution = input("Enter institution: ")
    annount_name = input("Enter account ref: ")

    database.create_account(institution, annount_name)


def add_annual_income(): # TODO
    pass


def update_projection(): # TODO
    pass


def summary_and_plot():
    # Calculate the summary information
    account_summary = database.summary_total()

    # Print the account summary information


    # A lot of messing around to convert the time(number) to time(date)
    x_axis=[]
    for date in account_summary['Date']:
        date_ = datetime.datetime.fromtimestamp(float(date))
        x_axis.append(date_)

    # Plot the account total vs time
    # TODO make this look better
    plt.plot(x_axis,account_summary['AccountTotal'])
    plt.gcf().autofmt_xdate()
    plt.show()

    # TODO add the plan to the plot


def add_spend():
    list_spend_cat()
    spend_cat = input("Enter spending cat ID: ")
    spend_ammount = input("Enter ammount: ")

    today_date = datetime.date.today()
    today_date = datetime.datetime.strftime(today_date, "%Y-%m-%d")
    spend_date_str = input(f"Enter for today {today_date} or input the date 'YYYY-mm-dd': ")
    if spend_date_str == '':
        spend_date = datetime.datetime.strptime(today_date, "%Y-%m-%d")
        spend_date = spend_date.timestamp()
    else:
        spend_date = datetime.datetime.strptime(spend_date_str, "%Y-%m-%d")
        spend_date = spend_date.timestamp()

    database.add_spend_record(spend_cat, spend_ammount, spend_date)

def review_month():
    # https://www.geeksforgeeks.org/how-to-group-by-month-and-year-in-sqlite/
    #TODO Lots
    pass


def plot_spend():
    pass

def list_spend_cat():
    spend_cat = database.active_spend_cat()
    print("--- Active Accounts ---")
    for category in spend_cat:
        if category[3] == "1": #Checks to see if spend cat is active
            print(f"Spend category {category[1]} budget {category[2]}: ID = {category[0]}")


def add_update_spend_cat():
    list_spend_cat()
    print("\n")
    select_operation = input("Select: '1' add new, '2' revise budget or 'q' return to menue: ")
    if select_operation == "1":
        spend_cat_new = input("Enter new spend category: ")
        monthly_budget = input("Enter monthly budget: ")
        database.create_spend_cat(spend_cat_new, monthly_budget)
    elif select_operation == "2":
        spend_cat_update = input("Enter spend category ID to update: ")
        monthly_budget_update = input("Enter new monthly budget: ")
        database.update_spend_cat(spend_cat_update, monthly_budget_update)