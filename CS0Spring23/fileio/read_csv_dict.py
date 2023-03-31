import csv

with open('weather.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if(line_count%100 == 0):
                print(f'\t{row["Date"]}: {row["Temp"]}, feels like {row["Feels_Like"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')