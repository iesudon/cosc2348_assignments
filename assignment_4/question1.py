class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__jobTitle = jobTitle
    def get_name(self):
        return self.__name
    def get_idNumber(self):
        return self.__idNumber
    def get_department(self):
        return self.__department
    def get_jobTitle(self):
        return self.__jobTitle
def menu():
    print("Hello and welcome to the employee management system \n")
    print("1 Look for a employee by ID \n")
    print("2 Add new employee \n")
    print("3 Delete employee \n")
    print("4 Change employee name, department, or job title \n")
    print("5 Quit \n")
    userSelection = int(input("Make your selection: \n"))
    while(userSelection < 0 and userSelection > 5):
        print("Enter a valid selection. \n")
        userSelection = int(input("Make your selection: \n"))
    return userSelection
        
def selection(userSelected, employeeDict):
    if userSelected == 1:
        employeeIdInput = int(input("Enter employee ID: "))
        if employeeIdInput in employeeDict:
            print("Employee " + str(employeeIdInput) + " is named " + employeeDict[employeeIdInput].get_name())
            print("Job title: " + employeeDict[employeeIdInput].get_jobTitle() + " | Department: " + employeeDict[employeeIdInput].get_department())
        else:
            print("Employee not found!")
        return True
    elif userSelected == 2:
        newEmployeeId = int(input("Enter Employee ID: "))
        while employeeDict[newEmployeeId]:
            print("Employee exists! Try again \n")
            newEmployeeId = int(input("Enter Employee ID: "))
        newEmployeeName = input("Enter employee name: ")
        newEmployeeDepartment = input("Enter department: ")
        newEmployeeJobTitle = input("Enter job title: ")
        employeeDict[newEmployeeId] = Employee(newEmployeeName,newEmployeeId,newEmployeeDepartment,newEmployeeJobTitle)
        return True
    elif userSelected == 3:
        deletedEmployeeID = int(input("Enter employee ID to be deleted. "))
        print("Delete employee: " + employeeDict[deletedEmployeeID].get_name() + "? ")
        deleteyesOrNo = input("This action cannot be undone. Y or N: ")
        if deleteyesOrNo == "Y" or DeleteyesOrNo == "y":
            employeeDict.pop(deletedEmployeeID)
            return True
        else:
            return True
    elif userSelected == 5:
        print("Goodbye!\n")
        return False
        
def main():
    john_titor = Employee("John Titor", 8, "Time travel", "Time traveler")
    employeeDict = {8:john_titor}
    programContinue = True
    while programContinue == True:
        print("\n")
        userChoice = menu()
        programContinue = selection(userChoice,employeeDict)
main()
