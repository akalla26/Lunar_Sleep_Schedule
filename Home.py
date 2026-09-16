import sys
from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QLabel

fileData = ""
currdatetime = datetime.now(datetime.utcoffset(None))
second = currdatetime.second
minute = currdatetime.minute
hour = currdatetime.hour
day = currdatetime.day
month = currdatetime.month
year = currdatetime.year

print("Current UTC Time: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day) + "/" + str(month) + "/" + str(year))

try:
    fileData = open("../../../../Downloads/Lunar Sleep Schedule/Lunar_Sleep_Schedule/data.txt", "r")

except:
    fileData = open("../../../../Downloads/Lunar Sleep Schedule/Lunar_Sleep_Schedule/data.txt", "w")
    fileData.write("Sleep Score: 30\nRecommended Sleep Time: 22:30\nRecommended Wake Time: 06:30\nSleep duration in mins: 480")

fileData.close()


fileData = open("../../../../Downloads/Lunar Sleep Schedule/Lunar_Sleep_Schedule/data.txt", "w")
fileData.write("Sleep Score: 30\nRecommended Sleep Time: 22:30\nRecommended Wake Time: 06:30\nSleep duration in mins: 480\n")

app = QApplication(sys.argv)
label = QLabel("Hello, World!")
label.show()
app.exec()