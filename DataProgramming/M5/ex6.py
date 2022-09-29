"""read the input for each student from the cmd.   calculate the average for each student and print it out.
sample: Neda,Asl,4,A,B,B,C   Ali,Simmons,2,A,B
output: Neda's gpa is 3
        Ali's gpa is 3.5"""

#A = 4
#B = 3
#C = 2
#D = 1

import sys

lenInput = len(sys.argv)

studentID = 1  #loops through all the inputs
while studentID < lenInput:
    student = sys.argv[studentID]
        
    index = student.find(",")
    name = student[:index]
    student = student[index+1:]
    
    index = student.find(",")
    lname = student[:index]
    student = student[index+1:]
    
    index = student.find(",")
    numCourse = int(student[:index])
    student = student[index+1:]
    
    itr = 1
    total = 0
    while itr < numCourse:
        index = student.find(',')
        if index == -1:
            grade = student
        else:
            grade = student[:index]
        
        if grade == "A":
            grade = 4
        elif grade == "B":
            grade = 3
        else: 
            grade == "C"
            grade = 2

        
        total = total+grade
        
        student = student[index+1:]
    
        itr = itr + 1

    average = total/numCourse
    print(name,"'s gpa is", average)
    studentID = studentID + 1