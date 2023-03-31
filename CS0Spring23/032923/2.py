# newer and better syntax - preferred way!!
alist = [1, 2, 3]
with open('words.txt', 'w') as fout:
    fout.write('apple\nball\ncat\ndog\n')
    fout.write('elephant\n')
    fout.write('zebra\n')
    fout.write(str(1))
    fout.write('\n')
    fout.write(str(alist))
    

# file will be automatically closed when with block is finished executing
# fout.write('test\n') # this will not be written as the file is closed; and throws I/O error