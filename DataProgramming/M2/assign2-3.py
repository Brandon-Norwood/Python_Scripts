#Brandon Norwood
#08/18/2021
#Assign2-3

import sys

Number1 = int(sys.argv[1])
Number2 = float(sys.argv[2])

a = Number1//Number2
b = Number1/Number2
c = Number1*Number2
d = Number1**Number2
e = Number1//2
f = 3**Number2

print("Number1 is", Number1)
print("Number2 is", Number2)

print(Number1, "//2 =", e,",", "<class 'int'>")
print(Number1, "/", Number2, "=", b, ",", "<class 'float'>")
print(Number1, "*", Number2, "=", c, ",", "<class 'float'>")
print("3 **", Number2, "=", f, ",", "<class 'float'>")