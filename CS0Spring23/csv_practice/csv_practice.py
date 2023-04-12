import datetime

with open('weather.csv') as file:
    line = file.readline() # read in first line as string
    headers = line.strip().split(sep=',')
    headers = headers[0:2] # slicing the first two elements from the headers list 
    print(headers)

    lines = file.readlines() #returns a list of strings for each line

line_num = 0
new_data = []
# finished with file, I have all the data
for row in lines:
    data = row.strip().split(sep=',') # strips the row of newline character, separtes values into list
    data = data[0:2] #slice out the first two elements
    
    now_time = datetime.datetime.strptime(data[0], '%m/%d/%Y %H:%M')
    now_temp = float(data[1])
    if(line_num == 0):
        last_time = now_time
        last_temp = now_temp

    
    if(line_num % 288 == 0):
        diff_time = last_time - now_time
        diff_temp = now_temp - last_temp
        last_time = now_time
        last_temp = now_temp
        data_tup = (diff_time, diff_temp)
        new_data.append(data_tup)
        #print(diff_time, diff_temp)

    line_num += 1

data_list = []
for t in new_data:
    time = str(t[0])
    time = time.replace(',', '')
    data_line = "%-20s%6.1f%10d" % (time, t[1], 10)
    
    print(data_line)
    data_list.append(data_line)

new_file = open('out.csv', 'w')
new_file.writelines(data_list)
new_file.close()

    


    
    
