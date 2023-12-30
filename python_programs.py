# Python Program to Find the Largest Among Three Numbers

num1 = 34
num2 = 89
num3 = 9

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else: 
    largest = num3

print("The largest number is", largest)

