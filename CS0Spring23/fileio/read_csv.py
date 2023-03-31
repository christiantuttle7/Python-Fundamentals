import csv

with open('weather.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row[0:3])}')
            line_count += 1
        else:
            if(line_count%100 == 0):
                print(f'{row[0]}\t{row[1]}\t{row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')