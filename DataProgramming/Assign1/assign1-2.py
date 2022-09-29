#Brandon Norwood
#08/17/2021
#Assign1-2

import sys

grade1 = int(sys.argv[1])
grade2 = int(sys.argv[2])
grade3 = int(sys.argv[3])
grade4 = int(sys.argv[4])

mean = (grade1 + grade2 + grade3 + grade4)/4 

print('Grades:', str(grade1)+",", str(grade2)+",", str(grade3)+",", grade4)
print('Average:', round(mean,2))
