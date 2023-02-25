from ImportExport import *
from PrintData import *
from Note import *
import os
import datetime
os.system('cls')


def inputData(notes):
    idarg = len(notes)
    title = input("Enter title: ")
    body = input("Enter your note: ")
    now = datetime.datetime.now()
    return [title, body, now.strftime("%d-%m-%Y %H:%M"), idarg]


def addNote(notes):
    noteinfo = inputData(notes)
    return Note(noteinfo[0], noteinfo[1], noteinfo[2], noteinfo[3])


def seeNotesAmount(notes):
    print("Notes amount: ", len(notes))


def editNote(notes):
    if (len(notes) > 0):
        index = input("Enter which note you want to edit by it's id: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes[i] = addNote(notes)
                print("Note edited!")
            else:
                print(
                    "Incorrect input, please make sure to not enter a number higher than notes amount!")
        except ValueError:
            print("Incorrect input, please enter a number!")
    else:
        print("Notes are empty!")


def deleteNote(notes):
    if (len(notes) > 0):
        index = input("Enter which note you want to delete by it's id: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes.pop(i)
                print("Note deleted!")
            else:
                print(
                    "Incorrect input, please make sure to not enter a number higher than notes amount!")
        except ValueError:
            print("Incorrect input, please enter a number!")
    else:
        print("Notes are empty!")


def main():
    notes = []
    done = False
    while (done == False):
        print("Welcome to Notepad--\n\
        Here are the options:\n\
        1 - Import Notes from file;\n\
        2 - Export Notes to file;\n\
        3 - Create a new Note;\n\
        4 - View all notes;\n\
        5 - View all notes with the latest showing first;\n\
        6 - View a specific note;\n\
        7 - Check how many notes you have;\n\
        8 - Edit a Note;\n\
        9 - Delete a Note;\n\
        0 - Exit.")
        command = input("Enter command: ")
        match command:
            case "1":
                notes = importFromFile()
            case "2":
                writeToFile(notes)
            case "3":
                notes.append(addNote(notes))
                print("Note saved!")
            case "4":
                printAllData(notes)
            case "5":
                printSortedData(notes)
            case "6":
                printSpecificData(notes)
            case "7":
                seeNotesAmount(notes)
            case "8":
                editNote(notes)
            case "9":
                deleteNote(notes)
            case "0":
                print("Goodbye!")
                done = True
            case _:
                print("Incorrect unput")
