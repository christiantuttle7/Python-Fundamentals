f_handle = open('Fierstfile.txt', 'w')
f_handle.write("# My first file test!\n")

for i in range(10):
    my_str = 'i = {}\n'.format(i)
    f_handle.write(my_str)

f_handle.close()
