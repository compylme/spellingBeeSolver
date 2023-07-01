import csv
import json
data = []

with open('400k.csv') as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE)
    for rows in csv_reader:
        row_string = ''.join(rows)
        if len(row_string) > 3:
            data.append(row_string)
            print(row_string)
# print(data)

with open('10000Words.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data))