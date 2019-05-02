import csv

import csv
with open('test.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in file:
        field1 = row[0]
        field2 = row[1]
        print(field1, field2)
