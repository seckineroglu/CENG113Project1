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
    review_file_name = f"review_{department}.txt"

    # Read review file to check status and preserve meeting date/note
    try:
        with open(review_file_name, "r") as file:
            status = file.readline().strip()
            file.readline()  # reviewer id
            file.readline()  # reviewer name
            file.readline()  # comment
            meeting_date = file.readline().strip()
            meeting_note = file.readline().strip()
    except FileNotFoundError:
        print("No meeting report exists for this department yet.")
        return

    # Only Pending Approval reports can be reviewed
    if status != "Pending Approval":
        print(f"This report is already {status}.")
        return

    # Manager login - 3 attempts
    attempts = 0
    while attempts < 3:
        manager_id = input("Enter your manager ID: ")
        password = input("Enter your password: ")
        if authenticate_manager(manager_id, password, department):
            break
        attempts += 1
        if attempts < 3:
            print("Invalid manager ID or password, or unauthorized department.")
        else:
            print("Invalid manager ID or password, or unauthorized department.")
            print("No attempts remaining. Returning to menu.")
            return

    # Get reviewer full name from employees.txt
    reviewer_name = ""
    try:
        with open("employees.txt", "r") as file:
            while True:
                emp_id = file.readline().strip()
                if emp_id == "":
                    break
                name = file.readline().strip()
                surname = file.readline().strip()
                file.readline()  # title
                file.readline()  # department
                file.readline()  # role
                file.readline()  # empty line
                if emp_id == manager_id:
                    reviewer_name = name + " " + surname
    except FileNotFoundError:
        print("The employees file was not found!")
        return

    # Display the current report
    try:
        with open(f"meeting_report_{department}.txt", "r") as file:
            while True:
                line = file.readline()
                if line == "":
                    break
                print(line, end="")
    except FileNotFoundError:
        print("Meeting report file not found!")
        return

    # Ask for decision
    print("\n1. Approve  2. Reject  3. Cancel")
    decision = input("Enter your decision (1-3): ")

    if decision == "1":
        comment = input("Enter approval comment (or press Enter to skip): ")
        if comment.strip() == "":
            comment = "-"
        new_status = "Approved"
    elif decision == "2":
        comment = ""
        while comment.strip() == "":
            comment = input("Enter rejection comment (required): ")
            if comment.strip() == "":
                print("Rejection comment cannot be empty!")
        new_status = "Rejected"
    else:
        print("No changes made.")
        return

    # Save updated review file
    with open(review_file_name, "w") as file:
        file.write(new_status + "\n")
        file.write(manager_id + "\n")
        file.write(reviewer_name + "\n")
        file.write(comment + "\n")
        file.write(meeting_date + "\n")
        file.write(meeting_note + "\n")
    print(f"Report {new_status.lower()} successfully.")
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

    