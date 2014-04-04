import csv

fd = open('file.csv', 'rb')
reader = csv.reader(fd)
for row in reader:
    print row
