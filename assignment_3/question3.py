class Employee:
    def __init__(self, name, idNumber, department, jobTitle): # create employee object
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__jobTitle = jobTitle
    def get_name(self): ## return name
        return self.__name
    def get_idNumber(self): ## return id num
        return self.__idNumber
    def get_department(self): ## return department
        return self.__department
    def get_jobTitle(self): ## return jobtitle
        return self.__jobTitle
    def get_fullName(self, name): ## get full name
        fullName = ''
        for letter in name: # for char in name
            if(letter != (name[0]) and letter.isupper()): # if letter does not equal name at zero and is uppercase
                fullName += ' ' # add space
            fullName += letter ## add letter to full name
        return fullName
    def get_email(self,name):
        fullName = ''
        for letter in name:
            if(letter != (name[0]) and letter.isupper()): ## add dot
                fullName += '.'
            fullName += letter
        return (fullName+"@company.com")
def main():
    susanMeyers = Employee("SusanMeyers", 47899, "Accounting", "Vice President")
    markJones = Employee("MarkJones", 39119, "IT", "Programmer")
    joyRogers = Employee("JoyRogers", 81774,"Manufacturing","Engineer")

    # print (joyRogers.name(), joyRogers.idNum(), joyRogers.department(), joyRogers.jobTitle())
    print(susanMeyers.get_name()," " ,susanMeyers.get_idNumber(), " " ,susanMeyers.get_department(), " " ,susanMeyers.get_jobTitle())
    print(markJones.get_name()," " ,markJones.get_idNumber(), " " ,markJones.get_department(), " " ,markJones.get_jobTitle())
    print(joyRogers.get_name()," " ,joyRogers.get_idNumber(), " " ,joyRogers.get_department(), " " ,joyRogers.get_jobTitle())
    print("\n")
    print(joyRogers.get_fullName(joyRogers.get_name())) ## demonstate it works
    print(joyRogers.get_email(joyRogers.get_name()))
main()
