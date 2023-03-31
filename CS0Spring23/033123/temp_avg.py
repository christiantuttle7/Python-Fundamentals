import csv
import math

with open("weather.csv") as file:
    csv_read = csv.reader(file, delimiter=',') # Reads in whole csv file in csv_read

    # step through each row, first the headers
    temps = []
    line_num=0
    for row in csv_read:
        if( line_num == 0): # If we are reading the header line
            print(','.join(row[0:1]))
        elif(line_num%1 == 0):
            #print(','.join(row))
            #print(csv_read.line_num)
            out = ""
            for j in range(0,int(float(row[1]))):
                out = out + ' '
            out = out + '*'
            print(out)
            temps.append(float(row[1]))
        line_num += 1
    
    #print(temps)
    #print("Average Temperature = {}".format(sum(temps)/len(temps)))
    
    
