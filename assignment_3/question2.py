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
def main():
    susanMeyers = Employee("SusanMeyers", 47899, "Accounting", "Vice President")
    markJones = Employee("MarkJones", 39119, "IT", "Programmer")
    joyRogers = Employee("JoyRogers", 81774,"Manufacturing","Engineer")

    # print (joyRogers.name(), joyRogers.idNum(), joyRogers.department(), joyRogers.jobTitle())
    print(susanMeyers.get_name()," " ,susanMeyers.get_idNumber(), " " ,susanMeyers.get_department(), " " ,susanMeyers.get_jobTitle())
    print(markJones.get_name()," " ,markJones.get_idNumber(), " " ,markJones.get_department(), " " ,markJones.get_jobTitle())
    print(joyRogers.get_name()," " ,joyRogers.get_idNumber(), " " ,joyRogers.get_department(), " " ,joyRogers.get_jobTitle())
main()