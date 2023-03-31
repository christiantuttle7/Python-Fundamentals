# old school - not preferred!!
fw = open('~/CMU_code/test2.txt', 'w') # w is for write mode
fw.write('words\n=====\n')
fw.write('apple\nball\ncat\ndog\n')
print(fw.write('zebra\n'))
fw.close() #must close the file to actually write data
# to the secondoary storage