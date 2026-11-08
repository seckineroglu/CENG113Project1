def display_menu():
    #display the main menu
    return
def select_department():
    #validate and return a choice from 1 to 6
    return
def display_employees(department):
    
    
    with open("employees.txt","r"):

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
def department_selection_validation()
    try:
        chosenDepartment=int(input("Please select a department(1-6)"))
    except ValueError:
        print("Department selection must be an integer! Please try again.")
        department_selection_validation()
    if (0<=chosenDepartment<=chosenDepartment):
        return chosenDepartment
    else:
        print("Invalid Department number! Please enter a number between 1-6")
        department_selection_validation()
    

    