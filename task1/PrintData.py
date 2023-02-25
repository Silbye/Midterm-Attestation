from datetime import datetime
from Note import *
import os
import datetime
os.system('cls')


def printAllData(data):
    if len(data) > 0:
        for object in data:
            print(object.printNote())
    else:
        print("Notes are empty!")


def printSortedData(data):
    if len(data) > 0:
        data = sorted(data, key=lambda x: datetime.datetime.strptime(
            x.date, '%d-%m-%Y %H:%M'), reverse=True)
        for object in data:
            print(object.printNote())
    else:
        print("Notes are empty!")


def printSpecificData(data):
    if len(data) > 0:
        index = input("Enter which note you want to see by it's id: ")
        try:
            i = int(index)
            if (i < len(data)):
                print(data[i].printNote())
            else:
                print(
                    "Incorrect input, please make sure to not enter a number higher than notes amount!")
        except ValueError:
            print("Incorrect input, please enter a number!")
    else:
        print("Notes are empty!")
