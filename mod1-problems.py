# Write your code here :-)
# 1. Create a program that prints the following output to the screen:
#"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers
#and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

import math
first_number=int(input("What is your first number?"))
second_number=int(input("What is your second number?"))
print("Added:", first_number+second_number)
print("Subtracted:", first_number-second_number)
print("multiplied:", first_number*second_number)
print("divided:", first_number/second_number)



# 3. Create a program that prompts for the side lengths of a triangle
#and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

import math
side_1=int(input("How long is side 1?"))
side_2=int(input("How long is side 2?"))
side_3=int(input("How long is side 3?"))
s=(side_1 + side_2 + side_3)/2
print("Here is the area:", math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3)))


# 4. Create a program that computes different statistics given five numbers
#including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import statistics
num1=int(input("What is your first number?"))
num2=int(input("What is your second number?"))
num3=int(input("What is your third number?"))
num4=int(input("What is your fourth number?"))
num5=int(input("What is your fifth number?"))
allnum=num1,num2,num3,num4,num5
minimum=min(allnum)
maximum=max(allnum)
print("Total:",num1+num2+num3+num4+num5)
print("average:",(num1+num2+num3+num4+num5)//5)
print("maximum:",maximum)
print("minimum:",minimum)
print("range:",maximum-minimum)
print("standard deviation:",statistics.stdev(allnum))



