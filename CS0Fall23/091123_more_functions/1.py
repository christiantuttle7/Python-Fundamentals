'''
Example code for built-in Python functions
'''

print("Hello World")
print("Enter in a number: ", end='')

name = input()
numbers = input("Enter two numbers separated by a space: ")
num1, num2 = numbers.split()
print(name)
print(numbers, float(num1)*float(num2))

print()
numbers = input("Enter two numbers separated by a space: ")
num1, num2 = numbers.split()
print(name)
num1 = float(num1)
num2=float(num2)
print(numbers, num1*num2)

#playing more with the print function
print("The value of num1 = ", num1, ", and the value of num2 = ", num2)
answer = "The value of num1 = {}, and the value of num2 = {}".format(num1, num2)
print(answer)

# rounding for varible types
number = 4.999
print(int(number+0.5))
