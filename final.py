def display_menu():
    #display the main menu
    while True:
        try:
            print("1-)Display Employees\n2-Assign Weekly Tasks\n3-)Generate Meeting Report\n4-)Display Meeting Report\n5-)Review Meeting Report\n6-)Display Task Summary\n0-)Exit")
            userMenuChoice:int=int(input("Please choose an option to display:"))
            break
        except ValueError:
            print("Choice must be an integer!Please try again.")
    if(userMenuChoice==0):# type: ignore # 0. Exit
        print("Exiting the program.")
        return -1
    elif(userMenuChoice==1):# type: ignore 1. Display department employees 
        display_employees(select_department())
    elif(userMenuChoice==2):# pyright: ignore[reportPossiblyUnboundVariable] # 2. Assign weekly tasks 
        assign_weekly_tasks(select_department())
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
    if (0<chosenDepartment<=6): # type: ignore
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
    departmentReportNumber = department
    departmentName = get_department_name(department)
    employeeNumber = get_employee_amount(department)
    total_estimated_hour = 0
    total_task_number = 0
    try:
        with open(f"tasks_{departmentReportNumber}.txt", "r") as taskFile:
            while True:
                emp_id = taskFile.readline().strip()
                emp_task = taskFile.readline().strip()
                emp_task_hour = int(taskFile.readline().strip())
                if emp_id == "" and emp_task == "" and emp_task_hour =="":
                    break
                elif emp_id == "" or emp_task == "" or emp_task_hour == "":
                    print("Task file is incomplete! Please check the file before generating a meeting report.")
                    return
                else:
                    try:
                        if 1 <= emp_task_hour <= 40:
                            total_estimated_hour += int(emp_task_hour)
                        else:
                            print("Please check the file, some estimated hour values might be wrong.")
                            return  
                    except ValueError:
                        print("Please check the file, some estimated hour values might be wrong.")
                        return
                    total_task_number += 1
                    taskFile.readline()
    except FileNotFoundError:
        print("There is no task assigned for this department yet.")
    meeting_date = input("Please enter a date for the meeting. Use the format YYYY/MM/DD: ")
    meeting_note = input("Please enter a note for the meeting: ")
    if employeeNumber != total_task_number:
        print("Please check the file, some tasks might be unfilled.")
        return
    else:
        average_estimated_hour = total_estimated_hour / total_task_number
    with open(f"review_{departmentReportNumber}.txt", "w") as reviewFile:
            reviewFile.write(f"Pending Approval\n-\n-\n-\n{meeting_date}\n{meeting_note}")
    with open(f"meeting_report_{departmentReportNumber}.txt", "w") as reportFile:
        reportFile.write(f"----- MEETING REPORT -----\n")
        reportFile.write(f"Department: {departmentName}\nMeeting Date: {meeting_date}\nMeeting Note: {meeting_note}\nStatus: Pending Approval\nEmployee Task: \n")
        try:
            with open("employees.txt", "r") as employeeContentFile:
                while True:
                    # Read one full record (6 lines)
                    emp_content_id = employeeContentFile.readline().strip()
                    if emp_content_id == "":# end of file reached
                        break
                    content_name = employeeContentFile.readline().strip()
                    content_surname = employeeContentFile.readline().strip()
                    content_title = employeeContentFile.readline().strip()
                    content_dept = employeeContentFile.readline().strip()
                    content_role = employeeContentFile.readline().strip()
                    employeeContentFile.readline()
                    with open(f"tasks_{departmentReportNumber}.txt", "r") as taskContentFile:
                        task_id = taskContentFile.readline().strip()
                        task = taskContentFile.readline().strip()
                        task_hour = taskContentFile.readline().strip()
                        taskContentFile.readline()
                if content_dept == departmentName:
                    reportFile.write(f"{emp_content_id} | {content_name} {content_surname} | {content_title} | {task} | {task_hour}\n")
        except FileNotFoundError:
            print("Employee file not found!")
        reportFile.write(f"Number of Employees: {employeeNumber}\nTotal Estimated Hours: {total_estimated_hour}\nAverage Estimated Hours: {average_estimated_hour:.2f}\n")
        reportFile.write(f"Reviewer ID              -   \nReviewer Name                -   \nReview Comment               -   ")
        return
    return
def display_meeting_report(department):
    # display the report or explain that none exists

    filename = f"meeting_report_{department}.txt"
    try:
        # Open the report in the read mode and print each line until lines finish.
        with open(filename, "r") as file:
            line = file.readline()
            while line != "":
                print(line, end="")
                line = file.readline()
    except FileNotFoundError:
        # Inform the user that if the meeting report did not get generated yet
        print("No meeting report found in this department")

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
    control=0
    while(control!=-1):
        control=display_menu()
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
main()