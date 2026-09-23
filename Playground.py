# Importing the necessary modules
from os import read
import sys
from datetime import datetime, UTC
from PySide6.QtWidgets import QApplication, QLabel
import ctypes

# File path and file data
filePath = "../../../../Downloads/Lunar Sleep Schedule/Lunar_Sleep_Schedule/.hidden_data.txt"
fileData = ""

# Stores the data for the current time
currDateTime = 0
second = 0
minute = 0
hour = 0
day = 0
month = 0
year = 0

# Stores the basic data for the user
# These values are placeholders, their proper values are derived from the save file
# In order: fatigue score, 0 >= fatigueScore >= 100, higher indicates more fatigue
# Time to sleep, time to wake, target time, last slept, time slept
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
hrSlept = 0
minSlept = 0

# Slightly more complex but still basic data
# This is not stored within the file, it is determined based on existing data
shouldExercise = False
canEat = False
canHaveCaffiene = False
canHaveLight = False

# Updates the current time
def Update_Time():

    global currDateTime
    global second
    global minute
    global hour
    global day
    global month
    global year

    currDateTime = datetime.now(UTC)
    second = currDateTime.second
    minute = currDateTime.minute
    hour = currDateTime.hour
    day = currDateTime.day
    month = currDateTime.month
    year = currDateTime.year

# Removes protections, allows the overwriting of data
def Remove_Protection():

    FILE_ATTRIBUTE_PROTECTED = None
    ctypes.windll.kernel32.SetFileAttributesW(filePath, FILE_ATTRIBUTE_PROTECTED)

# Readds protections, prevents overwriting of data
def Add_Protection():

    FILE_ATTRIBUTE_PROTECTED = 0x02 | 0x04
    ctypes.windll.kernel32.SetFileAttributesW(filePath, FILE_ATTRIBUTE_PROTECTED)

Update_Time()
Remove_Protection()

# Attempts to open the file
# If it exists, it closes it, if it doesn't it sets it up again before closing it
###### CREATES A NEW FILE REGARDLESS FOR NOW #######
try:
    #fileData = open(filePath, "r")
    fileData = open(filePath, "w")
    fileData.write("Starting Date: " + str(day) + "/" + str(month) + "/" + str(year) + "\nFatigue Score: 30\nRecommended Sleep Time: 22:30\nRecommended Wake Time: 06:30\nSleep duration in mins: 480\nTime slept: 0\nLast slept: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day) + "/" + str(month) + "/" + str(year))

except:
    fileData = open(filePath, "w")
    fileData.write("Starting Date: " + str(day) + "/" + str(month) + "/" + str(year) + "\nFatigue Score: 30\nRecommended Sleep Time: 22:30\nRecommended Wake Time: 06:30\nSleep duration in mins: 480\nTime slept: 0\nLast slept: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day) + "/" + str(month) + "/" + str(year))

fileData.close()
Add_Protection()

Remove_Protection()

fileData = open(filePath, "r")
line = fileData.readline()

while line:
    print(line)
    line = fileData.readline()

fileData.close()

Add_Protection()

app = QApplication(sys.argv)
label = QLabel("Hello, World!")
label.show()
app.exec()