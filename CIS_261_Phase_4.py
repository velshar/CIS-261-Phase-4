# Sharon Robinson
#CIS 261 Phase 4

from datetime import datetime

def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    ########## Open the file user.txt in append mode and assign to UserFile
    UserFile = open("Users.txt", "a")
     
    while True:
        ########## Write the line of code that will call function GetUserName and assign the return value to username
        username = GetUserName()

        if (username.upper() == "END"):
            break

     # Call the GetUserPassword function and assign the return value to userpwd
        userpwd = GetUserPassword()
        
        # Call the GetUserRole function and assign the return value to userrole
        userrole = GetUserRole()


        ########## Write the line of code that will call function GetUserPassword and assign the return value to userpwd
        
        ########## Write the line of code that will call function GetUserRole() and assign the return value to userrole
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"  
        UserFile.write(UserDetail)
    # close file to save data
    ########## Write the line of code that will close the file UserFile
    UserFile.close()
    
def GetUserName():

    ##### write the code to enter the username or End and return username 

    userID = input("Enter username or 'End': ").lower()

#3/2
    #Check to see if username already exists. Loop to say 'user already exist. Try again.'
    userIDObj = []
    checkUsersFile = open("Users.txt", "r")
    

    with checkUsersFile as file:
        for line in file:
            userInfo = line.strip().split('|')
            userIDObj.append(userInfo[0])

    while True:        
        if userID in userIDObj:
            userID = input("Please enter another name OR 'End': ")
        else:
            return userID.lower()

def GetUserPassword():
    ##### write the code to enter the pwd and return pwd
    return input("Enter password: ")

def GetUserRole():
     userrole = input("Enter role (Admin or User): ")
     while True:
         ####### write the if statement that validates that Admin or User has been entered. If true, return userrole.  If false, re-input userrole
             # Check if the value entered is Admin or User
       if userrole.lower() == "admin" or userrole.lower() == "user":
            # If true, return the user role
            return userrole
       else:
            # If false, ask the user to enter the role again
            userrole = input("Invalid role entered. Enter role (Admin or User): ")

def printuserinfo():
    UserFile = open("Users.txt","r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)

    UserFile.close()

def Login():
        # read login information and store in a list
    ########## Write the line of code that will open the file Users.txt in read mode
    UserFile = open("Users.txt", "r")
    
    UserName = input("Enter User Name: ").lower()
    UserRole = "None"
    while True:
       ########## Write the line of code that will read a line from UserFile and assign it to UserDetail
       UserDetail = UserFile.readline()    
       if not UserDetail:
           return UserRole, UserName
       ########## Write the line of code that will replace the carriage return in UserDetail
       UserDetail = UserDetail.replace("\n", "")
       ########## Write the line of code that will split UserDetail on the pipe delimiter (|) and assign it to UserList
       UserList = UserDetail.split("|") 
       
       if UserName == UserList[0]:
            UserRole = UserList[2]  # user is valid, return role
            return UserRole, UserName
    
def GetEmpName():
    empname = input("Enter employee name or 'End' to quit: ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy: ")
    todate = input("Enter End Date (mm/dd/yyyy: ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt","r")
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue  # skip next if statement and re-start loop
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue        
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate  = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True   
    if (DetailsPrinted):  #skip of no detail lines printed
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
       

if __name__ == "__main__":
    ##################################################
    ########## Write the line of code to call the method CreateUsers
    

    CreateUsers()
    printuserinfo()
    
    print()
    print("##### Data Entry #####")
    ########## Write the line of code to assign UserRole and UserName to the function Login

    UserRole, UserName = Login()
    

    DetailsPrinted = False  ###
    EmpTotals = {} ###
    ########## Write the if statement that will check to see if UserRole is equal to NONE (NOTE: code will show red error lines until this line is written)


    if (UserRole == 'None'):
        print(UserName," is invalid.")
    else:
    # only admin users can enter data
        ##### write the if statement that will check to see if the UserRole is equal to ADMIN (NOTE: code will show red error lines until this line is written)        
        if (UserRole.lower() == 'admin'):
            EmpFile = open("Employees.txt", "a+")                
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(taxrate) + "\n"  
                EmpFile.write(EmpDetail)
            # close file to save data
            EmpFile.close() 
            
        printinfo(DetailsPrinted)
       
