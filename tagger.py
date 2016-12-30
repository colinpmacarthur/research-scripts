import csv
import re

print("#############################################")
print("#######          Note coder          #######")
print("")

inFilename = input(  "Name of notes file to read:          ")
outFilename = input( "Name of file to output:              ")
tagFilename = input( "Name of file listing codes:          ")
codeColName = input( "Name of the column to put codes in:  ")


tagFile = open(tagFilename,"r")
tags = tagFile.read()
tags = tags.splitlines()

with open(inFilename, 'r') as inputFile:
    inputFileRows = csv.DictReader(inputFile)
    fieldnames = inputFileRows.fieldnames
    newFieldNames = list(fieldnames)
    newFieldNames.append(codeColName)

    for row in inputFileRows:
        print("+-------------------------------------------+")
        print("| ")
        print("|                    Note")
        print("| ")
        for key, value in row.items():
            print("| " + key + " : " +value)
        print("| ")
        print("| Available codes:")
        tagCount = 0
        for tag in tags:
            print("| " + str(tagCount) + " - " + tag)
            tagCount = tagCount + 1
        print("| ")
        code = input("| Enter code number (or a new code's name): ")
        print("| ")

        try:
            row[codeColName] = tags[int(code)]
        except:
            if code!="":
                tags.append(code)
                row[codeColName] = tags[tagCount]
            else:
                row[codeColName] = ""
        with open(outFilename, 'a') as outputFile:
            outputFileRows = csv.DictWriter(outputFile, newFieldNames)
            outputFileRows.writerow(row)
