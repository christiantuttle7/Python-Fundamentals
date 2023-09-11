'''
Example code for built-in Python functions
'''

message = "The temperature is 85" + chr(176) + " outside."

print(message)

print(ord('~'))
degrees = chr(176)
print(degrees)
print(ord(degrees))

print()

a=5
b=a
print(id(5))
print(id(a))
print(id(b))
print(id(message))
message = a
print(id(message))
b=6
print(a)

