import database
import menue

MENU_PROMPT = """-- Menu --

Daily Update:
1.1) Add spend
1.2) Review monthly
1.3) Plot spend
1.4) View, add or update spend category


Finnance Update:
2.1) Update savings accounts
2.2) Add new account
2.3) Add annual income
2.4) Update projection assumptions
2.5) Show summary and chart

EXIT/QUIT
q) Quit/Exit

Enter your choice: """

NEW_OPTION_PROMPT = "Enter new option text (or leave empty to stop adding options): "

def menu():
    while (selection := input(MENU_PROMPT)) != "q":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid input selected. Please try again.")


MENU_OPTIONS = {
    "0.1": menue.old_saving,
    "0.2": menue.list_active_accounts,
    "0.3": menue.deactivate_account,
    "1.1": menue.add_spend,
    "1.2": menue.review_month,
    "1.3": menue.plot_spend,
    "1.4": menue.add_update_spend_cat,
    "2.1": menue.update_saving,
    "2.2": menue.add_new_saving,
    "2.3": menue.add_annual_income,
    "2.4": menue.update_projection,
    "2.5": menue.summary_and_plot,
}

database.create_tables()
menu()