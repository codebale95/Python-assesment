# report_card_functions.py
# This file contains all the functions for the report card generator

# Global list to store report cards
report_cards = []
import csv
import json
import ast
report_cards = []

with open('students.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert JSON string → dict
        row['subjects'] = json.loads(row['subjects'])
        report_cards.append(row)


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
    reg_no = input("Enter registration number of the student to be found: ")
    semester = input("Enter semester whose result is to be found: ")
    for card in report_cards:
        if card['reg_no'] == reg_no and card['semester']==semester:
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
    semester = input("Enter semester whose result is to be found: ")
    for card in report_cards:
        if card['reg_no'] == reg_no and card['semester']==semester:
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
    semester = input("Enter semester whose result is to be found: ")
    for i, card in enumerate(report_cards):
        if card['reg_no'] == reg_no and card['semester']==semester:
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
    Displays the report card in a single horizontal table with borders.
    """

    # Calculations
    total = calculate_total_marks(card['subjects'])
    average = calculate_average_marks(card['subjects'])
    percentage = calculate_percentage(total, len(card['subjects']))
    grade = calculate_grade(percentage)

    # Format subjects as single string
    subjects_str = ", ".join(f"{sub}: {marks}" for sub, marks in card['subjects'].items())

    # Table header and row data
    headers = [
        "Name", "Semester", "Reg No", "Batch",
        "Subjects", "Total", "Average", "Percentage", "Grade"
    ]

    row = [
        card['name'],
        card['semester'],
        card['reg_no'],
        card['batch'],
        subjects_str,
        str(total),
        f"{average:.2f}",
        f"{percentage:.2f}%",
        grade
    ]

    # Calculate column widths
    col_widths = [
        max(len(headers[i]), len(row[i])) + 2
        for i in range(len(headers))
    ]

    # Helper to print horizontal line
    def print_line():
        print("+" + "+".join("-" * w for w in col_widths) + "+")

    # Print table
    print_line()
    print("|" + "|".join(headers[i].center(col_widths[i]) for i in range(len(headers))) + "|")
    print_line()
    print("|" + "|".join(row[i].ljust(col_widths[i]) for i in range(len(row))) + "|")
    print_line()


def exiting():
    fieldnames = ['name', 'semester', 'reg_no', 'batch', 'subjects']

    with open('students.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in report_cards:
            row = record.copy()
            # Convert subjects dict → JSON string
            row['subjects'] = json.dumps(record['subjects'])
            writer.writerow(row)

def view_all_report_cards():

    # Read CSV
    with open("students.csv", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0] + ["Average", "Grade"]
    data = []

# Process each student row
    for row in rows[1:]:
        name, semester, reg_no, batch, subjects = row
    
        subject_dict = ast.literal_eval(subjects)  # convert to dict
    
        marks = list(subject_dict.values())
        avg = sum(marks) / len(marks)
        grade = calculate_grade(avg)

        data.append([name, semester, reg_no, batch, subjects, f"{avg:.2f}", grade])

    # Combine for full table
    table = [header] + data

    # Calculate column widths
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table)]

    # Function to print horizontal line
    def print_line():
        line = "+"
        for w in col_widths:
            line += "-" * (w + 2) + "+"
        print(line)

    # Print table with borders
    print_line()
    print("| " + " | ".join(cell.ljust(width) for cell, width in zip(header, col_widths)) + " |")
    print_line()

    for row in data:
        print("| " + " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths)) + " |")
        print_line()


    
