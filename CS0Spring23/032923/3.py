# read whole file as list of lines
with open('words.txt', 'r') as fr: # 'r' or read mode by default; file must exist
    data = fr.readlines()
    fr.close()

for el in data:
    print(el.strip())

data[0] = "Changed!"

with open('words1.txt', 'w') as newFile: 
    for word in data:
        newFile.write(word)