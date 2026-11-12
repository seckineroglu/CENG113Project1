def display_menu():
    #display the main menu
    try:
        userMenuChoice:int=int(input("Please choose an option to display:"))
    except ValueError:
        print("Choice must be an integer!Please try again.")
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

        
    return
def select_department():
    try:
        chosenDepartment:int=int(input("Please select a department(1-6)"))
    except ValueError: 
        print("Department selection must be an integer! Please try again.")
        select_department()
    if (0<=chosenDepartment<=chosenDepartment):
            return chosenDepartment # type: ignore
    else:
        print("Invalid Department number! Please enter a number between 1-6")
        select_department()
def display_employees(department):
    try:
        with open("employees.txt", "r") as file:
            while True:
                # Read one full record (6 lines)
                emp_id = file.readline().strip()
                if emp_id == "":          # end of file reached
                    break
                name = file.readline().strip()
                surname = file.readline().strip()
                title = file.readline().strip()
                dept = file.readline().strip()
                role = file.readline().strip()
                file.readline()
    except FileNotFoundError:
        print("The Employees file wasn't found!")
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
def authenticate_manager(manager_id,password,department):
    #return true only when all authentication checks pass
    return
def review_meeting_report(department):
    #handle login attempts
    #decision input and report updates
    return
def display_task_summary(department):
    #calculate and display counts total hours and average
    return
def main():
    #run the menu loop and call other functions
    return

display_employees(1)

    