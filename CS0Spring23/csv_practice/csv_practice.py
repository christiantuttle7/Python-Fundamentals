import datetime

with open('weather.csv') as file:
    line = file.readline() # read in first line as string
    headers = line.strip().split(sep=',')
    headers = headers[0:2] # slicing the first two elements from the headers list 
    print(headers)

    lines = file.readlines() #returns a list of strings for each line

line_num = 0
# finished with file, I have all the data
for row in lines:
    data = row.strip().split(sep=',') # strips the row of newline character, separtes values into list
    data = data[0:2] #slice out the first two elements
    
    now_time = datetime.datetime.strptime(data[0], '%m/%d/%Y %H:%M')
    if(line_num == 0):
        last_time = now_time

    
    if(line_num % 500 == 0):
        diff_time = now_time - last_time
        data_tup = (data[0], float(data[1]), diff_time)
        print(data_tup)
        print(diff_time)

    line_num += 1
    last_time = now_time

    
    
