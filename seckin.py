def display_menu():
    #display the main menu
    try:
        userMenuChoice:int=int(input("Please choose an option to display:"))
    except ValueError:
        print("Choice must be an integer!Please try again.")
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
        display_meeting_report(select_department())
    elif(userMenuChoice==5):# 5. Review meeting report
        review_meeting_report(select_department())
    elif(userMenuChoice==6): # Display task summary
        display_task_summary(select_department())
    else:
        print("Invalid menu number! Please try again.")
        display_menu()
        
    return
def select_department():
    try:
        chosenDepartment:int=int(input("Please select a department(1-6)"))
    except ValueError: 
        print("Department selection must be an integer! Please try again.")
        select_department()
    if (0<chosenDepartment<=6):
            return chosenDepartment # type: ignore
    else:
        print("Invalid Department number! Please enter a number between 1-6")
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
                    print(f"ID:{emp_id},Name:{name},Surname:{surname},Title:{title},Department:{dept},Role:{role}")
    except FileNotFoundError:
        print("The Employees file wasn't found!")
    return
def assign_weekly_tasks(department):
    requestedDepartment = get_department_name(department)
    with open(f"tasks_{department}.txt", "w") as writeFile:
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
                        print(f"Tasks for Department:{requestedDepartment},ID:{emp_id}")
                        taskDescription=task_description_validation()
                        estimatedHours=estimated_hours_validation()
                        writeFile.write(f"{emp_id}\n")
                        writeFile.write(f"{taskDescription}\n")
                        writeFile.write(f"{estimatedHours}\n")  
                        writeFile.write("\n")
        except FileNotFoundError:
            print("The Employees file wasn't found!")
    #collect and save weekly tasks,,
    #allow replacement of existing assaignments only after report rejection
    return 
def generate_meeting_report(department):
    #collect missing meeting metadata and build the report
    #done by arda
    return
def display_meeting_report(department):
    #display the report or explain that none exsists
    #done by deniz
    return
def authenticate_manager(manager_id,password,department):
    #return true only when all authentication checks pass
    return
def review_meeting_report(department):
    #handle login attempts
    #decision input and report updates
    #done by ozan
    return
def display_task_summary(department):
    total_hours=0
    average_hours=0
    emptyString=""
    try:
        with open(f"tasks_{department}.txt","r") as task:
            while True:
                ID=task.readline().strip()
                if(ID==emptyString):
                    break
                description=task.readline().strip()
                hour=int(task.readline().strip())
                task.readline().strip()
                total_hours=total_hours + hour
        average_hours = total_hours / get_employee_amount(department)
        print(f"Department employee amount:{get_employee_amount(department)}\nNumber of assigned tasks:{get_employee_amount(department)}\nTotal estimated hours:{total_hours}\nAverage estimated hours:{average_hours}")
    except FileNotFoundError:
        print(f"Assaigned Tasks:0,Total hours:0,Average Time:N/A")
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
def task_description_validation():
    emptyString:str="" #for some reason couldnt put "" in if, solution was this
    while True:
        taskDescription=input("Please enter a task description:")
        if taskDescription == emptyString:
            print("Please enter a non-empty task description")
        else:
            break
    return taskDescription
def estimated_hours_validation():
    while True:
        try:
            estimatedHours=int(input("Please enter an estimate of required hours:"))
            if 0 > estimatedHours or estimatedHours > 40:
                print("Please enter a number between 0 and 40!")
                continue
            else:
                break
        except ValueError:
            print("Estimated hours must be an integer! Please try again")
    return estimatedHours
def get_employee_amount(department)->int:

    if department==1:
        return 10
    elif department==2:
        return 9
    elif department==3:
        return 8
    elif department==4:
        return 8
    elif department==5:
        return 8
    elif department==6:
        return 7
    else:
        return -1

assign_weekly_tasks(2)