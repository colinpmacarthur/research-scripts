import csv
import re

print("#############################################")
print("#######        Notes splitter        #######")
print("")
inFilename = input( "File to be read:     ")
outFilename = input("Name of output file: ")

f = open(inFilename,'r')
splitFile = re.split("\\n|\. ",f.read())
splitFile = list(filter(None, splitFile))
data = []
participant = "Not defined"
for item in splitFile:
    if re.match('[Pp]articipant [0-9]', item):
        participant = item
    else:
        data.append({'participant': participant, 'content': item})

with open(outFilename, 'w') as csvfile:
    fieldnames = ['participant', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("Successfully split notes file " + inFilename + " into " + outFilename)
