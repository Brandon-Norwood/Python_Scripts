#Brandon Norwood
#08/18/2021
#Assign2-4
#Converting Fahrenheit to Celcius
import sys

tempF = int(sys.argv[1])
tempC = (tempF-32)*(5/9)

print("The", tempF, "degree Fahrenheit is equal to", round(tempC,2), "degree Celsius.")