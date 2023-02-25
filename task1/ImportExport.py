from Note import *
import os
import csv
os.system('cls')


def importFromFile():
    notes = []
    with open('task1/Notes.csv', 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            note = Note(row[0], row[1], row[2], row[3])
            notes.append(note)
    print("Notes imported!")
    return notes


def writeToFile(notes):
    if (len(notes) > 0):
        with open('task1/Notes.csv', 'w') as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            for x in notes:
                writer.writerow([x.title, x.body, x.date, x.id])
        print("Notes saved!")
    else:
        print("Notes are empty!")
