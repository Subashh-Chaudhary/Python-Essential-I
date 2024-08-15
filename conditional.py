num1 = int(input("Please enter the first value : "))
num2 = int(input("Please enter the second value : "))
num3 = int(input("Please enter the third value : "))

largestNum = num1

if num2 > largestNum:
          largestNum = num2

if num3 > largestNum:
          largestNum = num3


print("The largest num between ", num1 , ",", num2, " and ", num3, " is", largestNum,".")