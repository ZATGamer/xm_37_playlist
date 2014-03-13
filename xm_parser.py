# This will take in a raw CSV file and return a CSV file with all the duplicates removed.

import csv

test_list = []
test_short_list = []
a = 0
with open('test.csv', 'rU') as csvfile:
    test_data = csv.reader(csvfile)
    for row in test_data:
        if row not in test_short_list:
            test_short_list.append(row)

test_short_list.sort()

for item in test_short_list:
    print item
