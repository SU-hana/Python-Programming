""" WRITE A PYTHON PROGRAM TO READ SPECIFIC COLUMNS OF GIVEN CSV FILE AND PRINT THE CONTENT OF THE COLUMNS """

import csv
with open('csvfile.csv', 'r')as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        print(line[2])
© 2022 GitHub, Inc.
Terms
Privacy