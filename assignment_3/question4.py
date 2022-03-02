class Student:
    def __init__(self, name,courseGrades):
        self.__courseGrades = courseGrades
        self.__name = name
    def find_percentage(self):
        return sum((self.get_grades())/6)
    def get_name(self):
        return self.__name
    def get_grades(self):
        return self.__courseGrades

def selectionSort(arr, names ,size):
    i = 0
    for i in range(0, size-1): ## for int i in range 0, till size-1
        unsortedMin = i ## the min value of the list is i
        j = i + 1 # j, another variable is i + 1
        while (j < size): # while  j is less than size
            if arr[j] < arr[unsortedMin]: # and if arr[j] is smaller than arr at min
                unsortedMin = j # min is now equal to j
            j = j + 1 # add one to j
        temp = arr[i] # temporary variable is equal to arr at i
        tempNames = names[i] 
        arr[i] = arr[unsortedMin] ## arr at i is equal to arr at unsortedMin
        names[i] = tempNames
        arr[unsortedMin] = temp ## arr at unsorted min is equal to temp
        names[unsortedMin] = tempNames
def main():
    numStudents = 25
    numCourses = 6
    
    studentClasses = []
    courseGrades = []
    
    for i in range(0,numStudents):
        inputStudentName = input("Enter the name of the student: ")
        for j in range(0,numCourses):
            inputCourseGrade = int(input("Enter the course grade for course "+ str(j+1) + ": "))
            while(inputCourseGrade > 100 or inputCourseGrade < 0):
                print("Enter a valid grade: ")
                inputCourseGrade = int(input("Enter the course grade for course "+ str(j+1) + ": "))
            courseGrades.append(inputCourseGrade)
        studentClasses.append(Student(inputStudentName,courseGrades))

    print("\n")
    print(studentClasses[0].get_grades())
    print("\n")
    sortedPercentageList = []
    sortedNames = []

    for m in range(0,numStudents):
        tempPercentage  = studentClasses[m].find_percentage()
        sortedPercentageList.append(tempPercentage)
        print(studentClasses[m].find_percentage())
        sortedNames.append(studentClasses[m].get_name())


    print(sortedPercentageList)
    selectionSort(sortedPercentageList, sortedNames, numStudents)
    print(sortedPercentageList)

    for k in range(0,numStudents):
            print("Student " + studentClasses[k].get_name() + " percentage average is " + str(sortedPercentageList[k]))
main()


