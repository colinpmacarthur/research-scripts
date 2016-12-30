import csv

print("#############################################")
print("####### Observation data entry helper #######")
print("")
observerInitials = input("Observer initials: ")
location = input("Location:          ")
filename = input("File name:         ")
continueLoopingSheets = "yes"
with open(filename, 'wt') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Location', 'Observer', 'Sheet ID','Trigger','Observation number','Actor','Action','Content'])
while continueLoopingSheets != "no":
    print("")
    print("+-------------------------------------------+")
    print("|               Observation sheet            ")
    sheetID = input("| Sheet ID: ")
    trigger = input("| Trigger:  ")
    observationSequenceNumber = 0
    continueLoopingObservations = "yes"
    while continueLoopingObservations != "no":
        observationSequenceNumber = observationSequenceNumber + 1
        print("| * Observation number: " + str(observationSequenceNumber))
        actor = input("|   Actor:              ")
        actionCode = input("|   Action code:        ")
        content = input("|   Content:            ")
        preliminaryCode = input("|   Code:            ")
        continueLoopingObservations = input("|   New observation (Type 'no' to stop.) ? ")
        with open(filename, 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([location, observerInitials, sheetID, trigger, observationSequenceNumber,actor,actionCode,content])
    continueLoopingNotes = input("|   Add other notes (Type 'no' to stop.) ? ")
    while continueLoopingNotes != "no":
        observationSequenceNumber = "note"
        print("| * Observation number: note")
        actor = ""
        actionCode = ""
        content = input("|   Content:            ")
        preliminaryCode = input("|   Code:            ")
        with open(filename, 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([location, observerInitials, sheetID, trigger, observationSequenceNumber,actor,actionCode,content])
        continueLoopingNotes = input("|   Add other notes (Type 'no' to stop.) ? ")

    print("+-------------------------------------------+")
    print("")
    continueLoopingSheets = input("New observation sheet? (Type 'no' to stop.) ")
