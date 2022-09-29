#Brandon Norwood
#09/14/2021
#Assign3-11

import sys

number1 = float(sys.argv[1])
number2 = float(sys.argv[2])
number3 = float(sys.argv[3])

if number1 >= number2 and number1 >= number3:
    print("Max:", number1)
elif number2 >= number1 and number2 >= number3:
    print("Max:", number2)
elif number3 >= number1 and number3 >= number2:
    print("Max:", number3)

if number1 <= number2 and number1 <= number3:
    print("Min:", number1)
elif number2 <= number1 and number2 <= number3:
    print("Min:", number2)
elif number3 <= number1 and number3 <= number2:
    print("Min:", number3)