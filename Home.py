# Importing the necessary modules
from time import sleep
from os import read
import sys
from datetime import datetime, timezone, timedelta
from PySide6.QtWidgets import QApplication, QLabel
from datetime import datetime, UTC
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QApplication, QPushButton, QInputDialog, QLineEdit, QGroupBox, QDateEdit
from PySide6.QtCore import Qt
import ctypes

# File path and file data
filePath = "../../../../Downloads/Lunar Sleep Schedule/Lunar_Sleep_Schedule/.hidden_data.txt"
fileData = ""

# Stores the data for the current time
currDateTime = 0

# Stores the basic data for the user
# These values are placeholders, their proper values are derived from the save file
# In order: fatigue score, 0 >= fatigueScore >= 100, higher indicates more fatigue
# Time to sleep, time to wake, target time, last slept, time slept, starting day
# When sleep is recorded, and it starts on a new day, hrSlept and minSlept are wiped and replaced with the new values
fatigueScore = 0
hrToSleep = 0
minToSleep = 0
hrToWake = 0
minToWake = 0
hrTarget = 0
minTarget = 0
hrLastSlept = 0
minLastSlept = 0
dayLastSlept = 0
monthLastSlept = 0
yearLastSlept = 0
hrSlept = 0
minSlept = 0
firstDay = 0
firstMonth = 0
firstYear = 0

# Slightly more complex but still basic data
# This is not stored within the file, it is determined based on existing data
shouldExercise = False
canEat = False
canHaveCaffiene = False
canHaveLight = False

# Sometime in the future, there will be an actual interface where the user gets to upload data and see proper visualizations
# For now, all inputs and other stuff of the like will be handled via text based prompting

# Prompts user to input a command
textInput = ""
def Command():

    print("Enter one of the following commands")
    print("Recommendations (recommend)")
    print("Enter Sleep Log (log)")
    print("Stats (stats)")
    print("Kill program (kill)")
    textInput = input("> ")

    if textInput.lower() == "recommend":
        Recommendations()

    elif textInput.lower() == "log":
        Log_Sleep()

    elif textInput.lower() == "stats":
        Stats()

    elif textInput.lower() == "kill":
        Kill()

    else:
        print("Invalid command")

# Enters a sleep log
def Log_Sleep():
    
    fileData = open(filePath, "r")
    line = fileData.readline()
    index = 0

    lastSleptTime = ""

    # Sets the time last slept
    while line:

        if index == 6:
            
            newLine = line.split(": ")
            newLine = newLine[1]
            newLine = newLine.split(" ")
            timeLine = newLine[0].split(":")
            dateLine = newLine[1].split("/")
            
            hr = int(timeLine[0])
            mins = int(timeLine[1])
            sec = int(timeLine[2])

            day = int(dateLine[0])
            month = int(dateLine[1])
            yr = int(dateLine[2])

            lastSleptTime = datetime(yr, month, day, hr, mins, sec)
            print(lastSleptTime)
                
        line = fileData.readline()
        index += 1

    fileData.close()

    timeSlept = input("Enter when you slept using the 24 hour clock time\n> ")

    try:
        pass 

    except:
        pass

    dateSlept = input("Enter the day this occured in D/M/Y format\n> ")

# Prints out recommendations
def Recommendations():

    Update_Time()

# Shows stats
def Stats():
    
    Update_Time()
    Remove_Protection()

    fileData = open(filePath, "r")
    line = fileData.readline()

    index = 0

    # Reads data and initializes it
    while line:

        print(line, end="")
        line = fileData.readline()
        index += 1

    fileData.close()
    Add_Protection()

    Remove_Protection()    

# Closes program
def Kill():

    sys.exit()

# Updates the current time
def Update_Time():

    global currDateTime

    currDateTime = datetime.now(UTC)

# Removes protections, allows the overwriting of data
# Protection should be removed first, then readded
def Remove_Protection():

    FILE_ATTRIBUTE_PROTECTED = None
    ctypes.windll.kernel32.SetFileAttributesW(filePath, FILE_ATTRIBUTE_PROTECTED)

# Readds protections, prevents overwriting of data
# Protection should be removed first, then readded
def Add_Protection():

    FILE_ATTRIBUTE_PROTECTED = 0x02 | 0x04
    ctypes.windll.kernel32.SetFileAttributesW(filePath, FILE_ATTRIBUTE_PROTECTED)

# Set up
Update_Time()
Remove_Protection()

# Attempts to open the file
# If it exists, it closes it, if it doesn't it sets it up again before closing it
try:
    fileData = open(filePath, "r")  
except:
    fileData = open(filePath, "w")
    fileData.write("Starting Date: " + str(currDateTime.day) + "/" + str(currDateTime.month) + "/" + str(currDateTime.year) + "\nFatigue Score: 30\nRecommended Sleep Time: 22:30\nRecommended Wake Time: 06:30\nSleep duration in mins: 480\nTime slept: 0\nLast slept: " + str(currDateTime.hour) + ":" + str(currDateTime.minute) + ":" + str(currDateTime.second) + " " + str(currDateTime.day) + "/" + str(currDateTime.month) + "/" + str(currDateTime.year))

fileData.close()
Add_Protection()

Remove_Protection()

fileData = open(filePath, "r")
line = fileData.readline()
index = 0

# Reads data and initializes it
while line:

    # Gets the starting date
    if index == 0:

        newLine = line.split(" ")
        splitLine = newLine[-1].split("/")
        firstDay = int(splitLine[0])
        firstMonth = int(splitLine[1])
        firstYear = int(splitLine[2])

    # Gets the fatigue score
    elif index == 1:

        newLine = line.split(" ")
        fatigueScore = int(newLine[2])        

    # Gets the sleep start time
    elif index == 2:

        newLine = line.split(" ")
        splitLine = newLine[-1].split(":")
        hrToSleep = int(splitLine[0])
        minToSleep = int(splitLine[1])

    # Gets the sleep end time
    elif index == 3:

        newLine = line.split(" ")
        splitLine = newLine[-1].split(":")
        hrToWake = int(splitLine[0])
        minToWake = int(splitLine[1])

    # Gets the target sleep time
    elif index == 4:

        newLine = line.split(" ")
        minTarget = int(newLine[-1]) % 60
        hrTarget = int(newLine[-1]) // 60

    # Gets the time slept
    elif index == 5:

        newLine = line.split(" ")
        minSlept = int(newLine[-1]) % 60
        hrSlept = int(newLine[-1]) // 60
            
    line = fileData.readline()
    index += 1

fileData.close()

Add_Protection()

while True:

    sleep(0.5)
    Update_Time()
    Command()