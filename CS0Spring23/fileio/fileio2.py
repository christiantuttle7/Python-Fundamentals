import random

f_handle = open('Fierstfile.txt', 'r', newline='\n')

data = f_handle.read(-1)
print(data)

data2 = data.split()
print(data2)

print("Hi")

#f_handle.close()

#f_handle = open('Fierstfile.txt', 'r')
f_handle.seek(0)

while True:
    data = f_handle.readline()
    if data != '' and data[0] != '#':
        print(data, end='')
    elif data == '':
        break

f_handle.close()

f_handle = open('Fierstfile.txt', 'r')

data = f_handle.readlines()
print(data)

f_handle.close()