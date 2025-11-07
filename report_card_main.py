# report_card_main.py
# This file handles user inputs and interfaces with the functions in report_card_functions.py

from report_card_functions import (
    create_report_card,
    view_report_card,
    update_report_card,
    remove_report_card,
    exiting,
    view_all_report_cards
)

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print("\n" + "="*50)
        print("REPORT CARD GENERATOR")
        print("="*50)
        print("1. Create a new report card")
        print("2. View existing report card")
        print("3. Update a report card")
        print("4. Remove existing report card")
        print('5: To view all the report cards')
        print("6. Exit")
        print("="*50)

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            create_report_card()
        elif choice == '2':
            view_report_card()
        elif choice == '3':
            update_report_card()
        elif choice == '4':
            remove_report_card()
        elif choice=='5':
            view_all_report_cards()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            exiting()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
