# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# LTurner, 8.10.21, Reviewed script and started assignment, update variables to python snake
# LTurner, 8.11.21, Started writing and testing processing script
# LTurner, 8.12.21, Started testing the input/output script
#                  Started combining the processing and input/output for step 4
# LTurner, 8.13.21, Continued on integrating all the pieces of code together
#                   Also edited code to clean it up for snipping into write-up
# LTurner, 8.14.21, More testing of code - adding new lines to make the output
#                   easier to read
# lTurner, 8.15.21, Added some complexity - count, reviewed to make sure all
#                   inputs/outputs for all functions were working
#                   Cleaned up the data input section
#                   Updated try loops based on homework feedback
#                   Tried to update count in removal loop based on feedback
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "ToDoFile.txt"  # The name of the data file
list_table = []  # A list that acts as a 'table' of rows
choice = ""  # Captures the user option selection
task = ""  # Captures the user task data
priority = ""  # Captures the user priority data
status = ""  # Captures the status of an processing functions
count = ""  # Count to check if a task was deleted
choice_y_n: ""  # Capture the choice of y or n from the user


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name_input, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name_input: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: list_of_rows and status: (list) of dictionary rows, status
        """
        list_of_rows.clear()  # clear current data
        reader = open(file_name_input, "r")
        for line in reader:
            task_input, priority_input = line.split(",")
            row = {"Task": task_input.strip(), "Priority": priority_input.strip()}
            list_of_rows.append(row)
        reader.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task_input, priority_input, list_of_rows):
        """ Adds data from user inputs into a dictionary row,
            then adds the row to the list of rows

        :param task_input: user entered task
        :param priority_input: user entered priority
        :param list_of_rows: list of dictionary rows to append new information to
        :return: list of dictionary rows, status
        """
        row = {"Task": task_input, "Priority": priority_input}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task_remove, list_of_rows):
        """Removes row from the list of rows based on user input

        :param task_remove: user entered task
        :param list_of_rows: list of dictionary rows
        :return: list_of_rows: list of dictionary rows,
                count_check: indication of if a task was deleted,
                status status of the function
        """
        found = ""
        for row in list_of_rows:
            if row['Task'].lower() == task_remove.lower():
                list_of_rows.remove(row)
                break
            else:
                continue
        else:
            found = "not"
        return list_of_rows, found, 'Success'

    @staticmethod
    def write_data_to_file(file_name_input, list_of_rows):
        """This function writes the list of dictionary rows to a file

        :param file_name_input: name of the file to save the data to
        :param list_of_rows: list of dictionary rows
        :return status
         """
        file_open = open(file_name_input, 'w')
        for row in list_of_rows:
            file_open.write(row['Task'] + ',' + row['Priority'] + '\n')
        file_open.close()
        return 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: choice_input - users inputted choice
        """
        choice_input = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice_input

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print('\n')
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ This function gets a task and priority from the user

        :return: task and priority from the user to be added
        """
        add_task = input("What task do you want to add to the list? ")
        add_priority = input('What priority do you want to give for the task entered? ')
        return add_task, add_priority

    @staticmethod
    def input_task_to_remove():
        """ This function gets a task from the user to be removed

        :return: task from the user for removal
        """
        remove_task = input('What task would you like to remove? ')
        return remove_task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
# Added a try and except block in case the file doesn't exist
# but doesn't cause the program to break with an error
try:
    list_table, status = Processor.read_data_from_file(file_name, list_table)  # read file data
except FileNotFoundError:
    IO.input_press_to_continue('File not found. Please save data if you want to read data from it.')  # message to user

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_tasks_in_list(list_table)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    choice = IO.input_menu_choice()  # Get menu option from user

    # Step 4 - Process user's menu choice
    # Add a new task to the list of dictionary rows
    if choice.strip() == '1':
        task, priority = IO.input_new_task_and_priority()  # Get user inputs for task and priority
        # Add the user inputs to the list of rows
        list_table, status = Processor.add_data_to_list(task, priority, list_table)
        IO.print_current_tasks_in_list(list_table)  # Print back to the user to the list of rows
        IO.input_press_to_continue(status)  # Print message to hit enter to continue
        continue  # to show the menu

    # Remove a task from the list of dictionary rows
    elif choice == '2':
        task = IO.input_task_to_remove()  # Gets user input for task to remove
        # Removal of the task from the list of rows
        list_table, count, status = Processor.remove_data_from_list(task, list_table)
        # print message based if the task was found and deleted or not
        if count == "":
            IO.input_press_to_continue("Task deleted")
        else:
            IO.input_press_to_continue("Task not found. No task deleted.")
        IO.print_current_tasks_in_list(list_table)  # Print back current list of rows
        continue  # to show the menu

    # Saving the list of rows to a file
    elif choice == '3':
        choice_y_n = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # User input if they want to save
        if choice_y_n.lower() == "y":
            Processor.write_data_to_file(file_name, list_table)  # Writes list of rows to a text file
            IO.input_press_to_continue("Data saved to file.")  # Print message, and message to hit enter to continue
        else:
            IO.input_press_to_continue("Save Cancelled!")  # If user doesn't want to save, provide message.
        continue  # to show the menu

    # Reloading the data from the file
    elif choice == '4':
        IO.input_press_to_continue("Warning: Unsaved Data Will Be Lost!")  # Warning to the user about reloading
        choice_y_n = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")  # input from user
        if choice_y_n.lower() == 'y':
            try:
                Processor.read_data_from_file(file_name,list_table)  # read data from file to list of rows
            except FileNotFoundError:
                IO.input_press_to_continue("File not found. Try saving file before next reload.")

            IO.print_current_tasks_in_list(list_table)  # print current list of rows
            IO.input_press_to_continue(status)  # print message to hit enter to continue
        else:
            IO.input_press_to_continue("File Reload Cancelled!")  # print message to user that file not reloaded
        continue  # to show the menu

    elif choice == '5':  # Exit Program
        choice_y_n = IO.input_yes_no_choice("Are you sure you want to exit? (y/n) - ")
        if choice_y_n.lower() == "y":
            print("Goodbye!")
            break
        else:
            continue

