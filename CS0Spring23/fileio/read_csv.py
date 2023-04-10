import csv
from datetime import datetime

def take_second_lst(elem):
    return elem[1]

with open('weather.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    lst = []
    for row in csv_reader:
        if line_count == 0: #if it's the first line, just read in the sting names for each column
            print(f'Column names are {", ".join(row[0:3])}')
            line_count += 1
        else: #for every line excdpt the first
            if(line_count%1 == 0):
                #print(f'{row[0]}\t{row[1]}\t{row[2]}')
                
                datetime_str = row[0]
                datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M')
                #print(datetime_object.timetuple())
                if(datetime_object.timetuple().tm_hour == 12 and datetime_object.timetuple().tm_min == 0 ):
                    lst.append((row[0], float(row[1])))
                    out = row[1]
                    space = int(float(row[1]))
                    for i in range(space):
                        out += " "
                    out += "*"
                    #print(out)
                    #print(datetime_object.timetuple())  # printed in default format
            line_count += 1
            
            
    print(f'Processed {line_count} lines.')
    #print(lst)

    new_sort = sorted(lst, key=take_second_lst)

    for i in range(5):
        print(new_sort[len(new_sort)-i-1])

    # take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
#print('Sorted list:', sorted_list)