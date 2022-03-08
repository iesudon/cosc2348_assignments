import random
class Student:
    def __init__(self,name,courseGrades):
        self.courseGrades = courseGrades
        self.name = name
    def find_percentage(self, courseGrades):
        tempPercentage = 0
        for m in range(0,6):
            tempPercentage += courseGrades[m]
        return round(tempPercentage/6)    
    def get_name(self):
        return self.name
    def get_grade_at_num(self, num):
        return self.courseGrades[num]
    def get_grades(self):
        return self.courseGrades

def selectionSort(arr, names ,size):
    for i in range(0, size): ## for int i in range 0, till size-1
        unsortedMin = i ## the min value of the list is i
        j = i + 1 # j, another variable is i + 1
        while (j < size): # while  j is less than size
            if arr[j] < arr[unsortedMin]: # and if arr[j] is smaller than arr at min
                unsortedMin = j # min is now equal to j
            j = j + 1 # add one to j
        temp = arr[i] # temporary variable is equal to arr at i
        tempNames = names[i] 
        arr[i] = arr[unsortedMin] ## arr at i is equal to arr at unsortedMin
        names[i] = names[unsortedMin]
        arr[unsortedMin] = temp ## arr at unsorted min is equal to temp
        names[unsortedMin] = tempNames
def main():
    numStudents = 25
    numCourses = 6
    
    studentClasses = []
    courseGrades_temp = []
    
    for i in range(0,numStudents):
        inputStudentName = input("Enter the name of the student: ")
        courseGrades_temp = [ random.randint(10,100) for i in range(0,6) ]
        print(courseGrades_temp)
        studentClasses.append(Student(inputStudentName,courseGrades_temp))
    
    sortedGrades = []
    sortedNames = []
    for temp in range(0,numStudents):
        sortedGrades.append((studentClasses[temp].find_percentage(studentClasses[temp].get_grades())))
        sortedNames.append(studentClasses[temp].get_name())
        
    selectionSort(sortedGrades,sortedNames,numStudents)
    print("Average Grades of all courses " + str(sortedGrades))
    print("Names of the students "+str(sortedNames))
    
    courseAverages = []
    count = 0
    while count != 6:
        avg = 0
        for i in range(0,numStudents):
            avg += studentClasses[i].get_grade_at_num(count)
        courseAverages.append(round((avg/numStudents),2))
        count += 1
    print("\n")
    print("Average course grades "+str(courseAverages))
main()
