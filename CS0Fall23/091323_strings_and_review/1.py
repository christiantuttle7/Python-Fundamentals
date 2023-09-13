'''
Some string formatting examples
and strings declarations
'''

import string

fname = "Corin\"'"
lname = 'Chepko\''
message = '''A little message w
ith """"""" ' qoutes inside''' # multiline strings using triples quotes
message2 = """Another message"""

card = '''
/\\
\\/
'''

print(fname)
print(message)
print(message2)

print(card)

age = 42
gpa = 2.1

answer = "Name is {} {} and he is {} and has a gpa of {}".format(fname, lname, age, gpa)
answer2 = f"Name is {fname} {lname} and he is {age} and has a gpa of {gpa}"
print(answer)
print(answer2)

str_width_20_name = fname.center(20)
print(str_width_20_name, lname)

print(string.ascii_letters)