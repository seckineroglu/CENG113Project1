def display_menu():
    #display the main menu
    try:
        userMenuChoice:int=int(input("Please choose an option to display: "))
    except ValueError:
        print("Choice must be an integer! Please try again.")
        display_menu()
    if(userMenuChoice==0):# type: ignore # 0. Exit
        #impelement exiting
        return
    elif(userMenuChoice==1):# 1. Display department employees 
        display_employees(select_department())
    elif(userMenuChoice==2):# pyright: ignore[reportPossiblyUnboundVariable] # 2. Assign weekly tasks 
        assaign_weekly_tasks(select_department())
    elif(userMenuChoice==3):# type: ignore # 3. Generate meeting report 
        generate_meeting_report(select_department())
    elif(userMenuChoice==4): # type: ignore # 4. Display meeting report 
        display_employees(select_department())
    elif(userMenuChoice==5):# 5. Review meeting report
        review_meeting_report(select_department())
    elif(userMenuChoice==6): # Display task summary
        display_task_summary(select_department())
    else:
        print("Invalid menu number! Please try again. ")
        display_menu()
        
    return
def select_department():
    try:
        chosenDepartment:int=int(input("Please select a department(1-6) "))
    except ValueError: 
        print("Department selection must be an integer! Please try again. ")
        select_department()
    if (0<=chosenDepartment<=6):
            return chosenDepartment # type: ignore
    else:
        print("Invalid Department number! Please enter a number between 1-6 ")
        select_department()
def display_employees(department):
    requestedDepartment = get_department_name(department)
    try:
        with open("employees.txt", "r") as file:
            while True:
                # Read one full record (6 lines)
                emp_id = file.readline().strip()
                if emp_id == "":# end of file reached
                    break
                name = file.readline().strip()
                surname = file.readline().strip()
                title = file.readline().strip()
                dept = file.readline().strip()
                role = file.readline().strip()
                file.readline()
                if(dept==requestedDepartment):
                    print(f"{name},{surname},{title},{dept},{role}")
    except FileNotFoundError:
        print("The Employees file wasn't found! ")
    return
def assaign_weekly_tasks(department):
    #collect and save weekly tasks,,
    #allow replacement of existing assaignments only after report rejection
    return 
def generate_meeting_report(department):
    #collect missing meeting metadata and build the report
    return
def display_meeting_report(department):
    #display the report or explain that none exsists
    return
def authenticate_manager(manager_id, password, department):
    # Return True only when all authentication checks pass
    department_name = get_department_name(department)
    is_valid_manager = False
    password_matches = False

    # Check 1: ID exists, role is Manager, manager belongs to this department
    try:
        with open("employees.txt", "r") as file:
            while True:
                emp_id = file.readline().strip()
                if emp_id == "":  # end of file reached
                    break
                file.readline()  # name (not needed)
                file.readline()  # surname (not needed)
                file.readline()  # title (not needed)
                dept = file.readline().strip()
                role = file.readline().strip()
                file.readline()  # empty line between records
                if emp_id == manager_id and role == "Manager" and dept == department_name:
                    is_valid_manager = True
    except FileNotFoundError:
        print("The employees file was not found!")
        return False

    # Check 2: ID and password match a record in manager_passwords.txt
    try:
        with open("manager_passwords.txt", "r") as file:
            while True:
                file_id = file.readline().strip()
                if file_id == "":  # end of file reached
                    break
                file_password = file.readline().strip()
                file.readline()  # empty line between records
                if file_id == manager_id and file_password == password:
                    password_matches = True
    except FileNotFoundError:
        print("The manager passwords file was not found!")
        return False

    # Both checks must pass
    return is_valid_manager and password_matches
def review_meeting_report(department):
    # Build the review file name from the department number (e.g. review_1.txt)
    review_file_name = f"review_{department}.txt"

    try:
        # Read only the first line of the file, which is the status
        with open(review_file_name, "r") as file:
            status = file.readline().strip()
    except FileNotFoundError:
        # No review file means no report has been generated yet
        print("No meeting report exists for this department yet.")
        return

    # Only a report that is waiting for approval can be reviewed
    if status != "Pending Approval":
        print(f"This report is already {status}. ")
        return
    elif status == "Pending Approval":
        print("This report is waiting for approval. ")

    # Login attempts: manager gets 3 tries
    attempts = 0
    while attempts < 3:
        manager_id = input("Enter your manager ID: ")
        password = input("Enter your password: ")
        if authenticate_manager(manager_id, password, department):
            print("Login successful!")
            # TODO: approve or reject the report
            return
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"Login failed! You have {remaining} attempt(s) left.")
            else:
                print("Login failed! No attempts remaining. Returning to menu.")
    return
def display_task_summary(department):
    #calculate and display counts total hours and average
    return
def main():
    #run the menu loop and call other functions
    return
def get_department_name(department):
    if(department==1):
        return "Software Development"
    elif(department==2):
        return "Artificial Intelligence"
    elif(department==3):
        return "Research and Development"
    elif(department==4):
        return "Quality Assurance"
    elif(department==5):
        return "IT Operations"
    elif(department==6):
        return "Human Resources"
display_menu()

    