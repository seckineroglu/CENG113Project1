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
        display_employees(select_department())
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
    if (0<=chosenDepartment<=6):
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
                    print(f"{name},{surname},{title},{dept},{role}")
    except FileNotFoundError:
        print("The Employees file wasn't found!")
    return
def assaign_weekly_tasks(department):
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
                emp_task_hour = taskFile.readline().strip()
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

    
display_menu()

    