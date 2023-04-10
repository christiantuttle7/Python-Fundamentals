with open('weather.csv') as csv_file:
    
    line_count = 0
    lst = []
    line = csv_file.readline()
    
    header = (line.split(sep=',')[0], line.split(sep=',')[1])
    print(header)

    lines = csv_file.readlines()
    data = []
    for row in lines:
        if(line_count%500 == 0):
            items = row.strip().split(sep=',')
            data_tup = (items[0], float(items[1]))
            data.append(data_tup)
            
            #print(f'{row[0]}\t{row[1]}\t{row[2]}')
                
            #datetime_str = row[0]
            #datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M')
        line_count += 1
    
    print(data)