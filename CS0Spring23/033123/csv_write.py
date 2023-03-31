import csv

with open('ecsv_out2.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])