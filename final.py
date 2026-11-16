def display_menu():
    #display the main menu
    while True:
        try:
            print("1-)Display Employees\n2-)Assign Weekly Tasks\n3-)Generate Meeting Report\n4-)Display Meeting Report\n5-)Review Meeting Report\n6-)Display Task Summary\n0-)Exit")
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
    while True:
        try:
            chosenDepartment=int(input("Please select a department(1-6):"))
        except ValueError:
            print("Department number must be an integer! Please try again.")
        if(0<chosenDepartment<=6):#type:ignore
            return chosenDepartment#type:ignore
        else:
            print("Department number must be between 1-6.Please try again.")
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
    if(meeting_report_status(department)!=-1):
        print("Only rejected assaignments can be rewritten!")
        return
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
    tasksExists=tasks_n_existence(department)
    departmentName=get_department_name(department)
    if(tasksExists==-1):
        print("Meeting reports can only be generated on already assinged tasks! Please assign tasks to the corresponding department first")
        return
    reportExists=meeting_report_status(department)
    if(reportExists==2):#doesnt exist, free to proceed
        review_date=input("Please provide a date for the meeting report.")
        review_note=input("Please provide a note for the meeting report.")
        with open(f"review_{department}.txt","w") as writeReview:
            writeReview.write("Pending Approval\n")
            writeReview.write("-\n")
            writeReview.write("-\n")
            writeReview.write("-\n")
            writeReview.write(f"review_date.strip()\n")
            writeReview.write(review_note.strip())
        #write meeting_report_{department} here 
        with open(f"meeting_report_{department}.txt","w") as writeReport:
            writeReport.write("----- MEETING REPORT -----\n")
            writeReport.write(f"Department:{departmentName}\n")
            writeReport.write(f"Meeting Date:{review_date}\n")
            writeReport.write(f"Meeting Note:{review_note}\n")
            writeReport.write("Status: Pending Approval\n")
            writeReport.write("Employee Tasks:\n")
            with (open(f"tasks_{department}.txt","r") as tasksRead,
                  open("employees.txt","r") as employeesRead):
                while True:
                    # Read one full record (6 lines)
                    emp_content_id = employeesRead.readline().strip()
                    if emp_content_id == "":# end of file reached
                        break
                    content_name = employeesRead.readline().strip()
                    content_surname = employeesRead.readline().strip()
                    content_title = employeesRead.readline().strip()
                    content_dept = employeesRead.readline().strip()
                    content_role = employeesRead.readline().strip()
                    employeesRead.readline()
                    if(content_dept!=departmentName):
                        continue
                    task_id = tasksRead.readline().strip()
                    task = tasksRead.readline().strip()
                    task_hour = tasksRead.readline().strip()
                    tasksRead.readline()
                    totalHours=0
                    totalHours=totalHours+int(task_hour)
                    averageHours=totalHours/get_employee_amount(department)    
                    if content_dept == departmentName: # type: ignore
                        writeReport.write(f"{emp_content_id} | ")
                        writeReport.write(f"{content_name} | ")
                        writeReport.write(f"{content_surname} | ")
                        writeReport.write(f"{content_title} | ")
                        writeReport.write(f"{task} | ")
                        writeReport.write(f"{task_hour} |")
                        writeReport.write("\n")
                writeReport.write(f"Number of Employees:{get_employee_amount(department)}\n")
                writeReport.write(f"Total estimated hours:{totalHours}\n") #type:ignore
                writeReport.write(f"Average estimated hours:{averageHours:.2f}\n")#type:ignore
                writeReport.write("Reviewer ID:-\nReviewer Name:-\nReviwer Comment:-")
    elif(reportExists==0):#pending approval, no permission
        print("Report already exists and is pending approval! Please try again later.")
        return
    elif(reportExists==1):# approved,no permission
        print("Report already exsits and is approved! Please try again later.")
        return
    elif(reportExists==-1): # rejected, yes permission
        while True:
            confirmation=input("This report was rejected.Do you wish to proceed to override it? (Yes/No)")
            if(confirmation.lower()=="yes" or confirmation.lower()=="no"):
                if(confirmation.lower() == "yes"):
                    break
                else:
                    print("Rejected to override, returning to main menu.")
                    return
            else:
                print("Please enter a valid input")
        #first save the old date and note
        with open(f"meeting_report_{department}.txt","r")as oldRead:
            #3-4
            oldRead.readline()
            oldRead.readline()
            oldDate=oldRead.readline().strip()
            oldNote=oldRead.readline().strip()
        #the old code, again,without date and note
        with (open(f"meeting_report_{department}.txt","w") as writeReport,
              open(f"tasks_{department}.txt","r") as tasksRead,
              open("employees.txt","r") as employeesRead):
            writeReport.write("----- MEETING REPORT -----\n")
            writeReport.write(f"Department:{departmentName}\n")
            writeReport.write(f"{oldNote}\n")
            writeReport.write(f"{oldDate}\n")
            writeReport.write("Status: Pending Approval\n")
            writeReport.write("Employee Tasks:\n")
            while True:
                # Read one full record (6 lines)
                emp_content_id = employeesRead.readline().strip()
                if emp_content_id == "":# end of file reached
                    break
                content_name = employeesRead.readline().strip()
                content_surname = employeesRead.readline().strip()
                content_title = employeesRead.readline().strip()
                content_dept = employeesRead.readline().strip()
                content_role = employeesRead.readline().strip()
                employeesRead.readline()
                if(content_dept!=departmentName):
                    continue
                task_id = tasksRead.readline().strip()
                task = tasksRead.readline().strip()
                task_hour = tasksRead.readline().strip()
                tasksRead.readline()
                totalHours=0
                totalHours=totalHours+int(task_hour)
                averageHours=totalHours/get_employee_amount(department)    
                if content_dept == departmentName: # type: ignore
                    writeReport.write(f"{emp_content_id} | ")
                    writeReport.write(f"{content_name} | ")
                    writeReport.write(f"{content_surname} | ")
                    writeReport.write(f"{content_title} | ")
                    writeReport.write(f"{task} | ")
                    writeReport.write(f"{task_hour} |")
                    writeReport.write("\n")
            writeReport.write(f"Number of Employees:{get_employee_amount(department)}\n")
            writeReport.write(f"Total estimated hours:{totalHours}\n") #type:ignore
            writeReport.write(f"Average estimated hours:{averageHours:.2f}\n")#type:ignore
            writeReport.write("Reviewer ID:-\nReviewer Name:-\nReviwer Comment:-")
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
        print()
    except FileNotFoundError:
        # Inform the user that if the meeting report did not get generated yet
        print("No meeting report found in this department")
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
                if int(emp_id) == int(manager_id) and role == "Manager" and dept == department_name:
                    is_valid_manager = True,
                    break
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
                if int(file_id) == manager_id and file_password == password:
                    password_matches = True
                    break
    except FileNotFoundError:
        print("The manager passwords file was not found!")
        return False
    # Both checks must pass
    return is_valid_manager and password_matches
def review_meeting_report(department):
    emptyString=""
    rejectionNote=""
    if(meeting_report_status==2):
        print("Report not found! Returning to main menu.")
        return
    elif(meeting_report_status==-1):
        print("Report is already rejected! Override it to continue.Returning to main menu.")
        return
    elif(meeting_report_status==1):
        print("Report is already approved.Returning to main menu.")
        return
    manager_id=login_manager_handler()
    manager_name=get_manager_name(manager_id)  
    display_meeting_report(department)
    while True:
        try:
            choice=int(input("Please enter what do you want to do with the report.1 for approval,2 for rejection,3 for cancellation."))
            break
        except ValueError:
            print("Please give a proper input.")
    if(choice==3):
        print("Cancelled,returning to main menu.")
        return
    elif(choice==2):
        while(rejectionNote == emptyString):
            rejectionNote=input("Please enter a rejection comment.Do not leave a blank message.")
        with open(f"review_{department}.txt","r")as reviewRead:
            reviewRead.readline()
            reviewRead.readline()
            reviewRead.readline()
            reviewRead.readline()
            oldDate=reviewRead.readline()
            oldNote=reviewRead.readline()
        with open(f"review_{department}.txt","w")as reviewWrite:
            reviewWrite.write("Rejected")
            reviewWrite.write(f"{manager_id}")
            reviewWrite.write(f"{manager_name}")
            reviewWrite.write(f"{rejectionNote}")
            reviewWrite.write(f"{oldDate}")
            reviewWrite.write(f"{oldNote}")
        
    elif(choice==1):
        approvalNote=input("Please enter a approval comment.")
    
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
            if (0 >= estimatedHours) or (40 > estimatedHours):
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
def get_manager_info():
    while True:
        try:
            manager_id=int(input("Enter Manager ID:"))
            break
        except ValueError:
            print("Manager ID must be an integer! Try again")
    while True:
        try:
            manager_password=(input("Enter Manager Password:"))
            break
        except:
            print("Couldn't process the password! Try again.")
    while True:
        try:
            manager_department=int(input("Enter manager department as an integer(1-6)"))
            break
        except ValueError:
            print("Manager Department must be an integer! Please try again.")
    return manager_id,manager_password,manager_department
def login_manager_handler():
    attempts = 0
    while attempts < 3:
        manager_id,password,department=get_manager_info()
        if authenticate_manager(manager_id, password, department):
            return manager_id
        attempts=attempts+1
        print("Invalid manager ID or password, or unauthorized department.")
    print("No attempts remaining. Returning to menu.")
    return -1
def get_manager_name(manager_id):
    with open("employees.txt","r")as file:
        while True:
            id=file.readline().strip()
            name=file.readline().strip()
            surname=file.readline().strip()
            doesntmatter=file.readline().strip()
            alsodoesntmatter=file.readline().strip()
            role=file.readline
            file.readline()#empty space between entries
            if(int(id)==manager_id):
                fullName=name+" "+surname
                return fullName
def review_status(department):
    try:
        with open(f"review_{department}.txt") as file:
            status=file.readline().strip()
            if(status.lower()=="pending approval"):
                return 0
            elif(status.lower()=="approved"):
                return 1
            elif (status.lower()=="rejected"):
                return -1
    except FileNotFoundError:
        return 2
def meeting_report_status(department):
    #5
    try:
        with open(f"meeting_report_{department}.txt","r") as file:
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            status=file.readline().strip()
            if(status=="Status: Pending Approval"):
                return 0
            elif(status=="Status: Approved"):
                return 1
            elif(status=="Status: Rejected"):
                return -1
    except FileNotFoundError:
        return 2
def tasks_n_existence(department):
    try:
        with open(f"tasks_{department}.txt","r")as file:
            return 1
    except FileNotFoundError:
        return -1



main()
