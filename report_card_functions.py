
# This file contains all the functions for the report card generator

# Global list to store report cards
report_cards = []

def create_report_card():
    """
    Creates a new report card by taking user inputs for name, semester, registration no, batch,
    and subjects with marks.
    """
    name = input("Enter student name: ")
    semester = input("Enter semester: ")
    reg_no = input("Enter registration number: ")
    batch = input("Enter batch: ")

    subjects = {}
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    report_card = {
        'name': name,
        'semester': semester,
        'reg_no': reg_no,
        'batch': batch,
        'subjects': subjects
    }

    report_cards.append(report_card)
    print("Report card created successfully!")

def view_report_card():
    """
    Views an existing report card by registration number.
    """
    reg_no = input("Enter registration number: ")
    for card in report_cards:
        if card['reg_no'] == reg_no:
            display_report_card(card)
            return
    print("Report card not found. Please try again.")
    view_report_card()

def update_report_card():
    """
    Updates an existing report card by registration number.
    Provides options to add, update, or delete subjects.
    """
    reg_no = input("Enter registration number: ")
    for card in report_cards:
        if card['reg_no'] == reg_no:
            while True:
                print("\nUpdate Options:")
                print("1. Add new subject")
                print("2. Update existing subject marks")
                print("3. Delete a subject")
                print("4. Done updating")
                choice = input("Enter your choice: ")

                if choice == '1':
                    subject = input("Enter new subject name: ")
                    marks = float(input(f"Enter marks for {subject}: "))
                    card['subjects'][subject] = marks
                    print("Subject added successfully!")
                elif choice == '2':
                    subject = input("Enter subject name to update: ")
                    if subject in card['subjects']:
                        marks = float(input(f"Enter new marks for {subject}: "))
                        card['subjects'][subject] = marks
                        print("Subject updated successfully!")
                    else:
                        print("Subject not found.")
                elif choice == '3':
                    subject = input("Enter subject name to delete: ")
                    if subject in card['subjects']:
                        del card['subjects'][subject]
                        print("Subject deleted successfully!")
                    else:
                        print("Subject not found.")
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
            return
    print("Report card not found. Please try again.")
    update_report_card()

def remove_report_card():
    """
    Removes an existing report card by registration number.
    """
    reg_no = input("Enter registration number: ")
    for i, card in enumerate(report_cards):
        if card['reg_no'] == reg_no:
            report_cards.pop(i)
            print("Report card removed successfully!")
            return
    print("Report card not found. Please try again.")
    remove_report_card()

def calculate_total_marks(subjects):
    """
    Calculates the total marks from subjects dictionary.
    """
    return sum(subjects.values())

def calculate_average_marks(subjects):
    """
    Calculates the average marks from subjects dictionary.
    """
    if not subjects:
        return 0
    return sum(subjects.values()) / len(subjects)

def calculate_percentage(total_marks, num_subjects):
    """
    Calculates the percentage based on total marks and number of subjects.
    Assumes 100 marks per subject.
    """
    max_total = num_subjects * 100
    if max_total == 0:
        return 0
    return (total_marks / max_total) * 100

def calculate_grade(percentage):
    """
    Calculates the grade based on percentage.
    """
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def display_report_card(card):
    """
    Displays the full report card with calculations.
    """
    print("\n" + "="*50)
    print("REPORT CARD")
    print("="*50)
    print(f"Name: {card['name']}")
    print(f"Semester: {card['semester']}")
    print(f"Registration No: {card['reg_no']}")
    print(f"Batch: {card['batch']}")
    print("\nSubjects and Marks:")
    for subject, marks in card['subjects'].items():
        print(f"  {subject}: {marks}")

    total = calculate_total_marks(card['subjects'])
    average = calculate_average_marks(card['subjects'])
    percentage = calculate_percentage(total, len(card['subjects']))
    grade = calculate_grade(percentage)

    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("="*50)
