# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Rachael Leahy, 8/17/2025, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # Holds data in dictionary format
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

#Import JSON library
import json

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    if file.closed==False:
            file.close()
    print("JSON file must exist before running this script.\n")
    print("Built in Python error info:")
    print(e, e.__doc__, type(e), sep="\n")
except json.JSONDecodeError as e:
    if file.closed==False:
            file.close()
    print("JSON file is invalid. \n")
    print("Built in Python error info:")
    print(e, e.__doc__, type(e), sep="\n")
except Exception as e:
    if file.closed==False:
            file.close()
    print("There was a non-specific error.\n")
    print("Built in Python error info:")
    print(e, e.__doc__, type(e), sep="\n")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name must contain only letters.")
                break
            except ValueError as e:
                print(e)
                print("--Technical Error Message--")
                print(e.__doc__)
                print(e.__str__())
            except Exception as e:
                print("There was a non-specific error.\n")
                print("Built in Python error info:")
                print(e, e.__doc__, type(e), sep="\n")
        while True:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name must contain only letters.")
                break
            except ValueError as e:
                print(e)
                print("--Technical Error Message--")
                print(e.__doc__)
                print(e.__str__())
            except Exception as e:
                print("There was a non-specific error.\n")
                print("Built in Python error info:")
                print(e, e.__doc__, type(e), sep="\n")

        course_name = input("Please enter the name of the course: ")
        student_data = {
            "Name": student_first_name + " " + student_last_name,
            "Course": course_name
        }
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"{student["Name"]}, {student["Course"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data are saved to the file:")
            for student in students:
                print(f"{student['Name']}, {student['Course']}")

        except PermissionError as e:
            if file.closed == False:
                file.close()
            print("Permission denied. Cannot write to file. \n")
            print("Built in Python error info:")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            if file.closed == False:
                file.close()
            print("There was a non-specific error.\n")
            print("Built in Python error info:")
            print(e, e.__doc__, type(e), sep="\n")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
