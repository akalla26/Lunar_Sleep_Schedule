# Importing the necessary modules
import gc
from time import sleep
from os import read
import sys
from datetime import datetime, timezone, timedelta
from unittest import loader
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from datetime import datetime, UTC
from PySide6.QtWidgets import QMainWindow, QPushButton, QInputDialog, QLineEdit, QGroupBox, QDateEdit, QDateTimeEdit
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QTimeZone, QByteArray
import ctypes

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

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
lastSleptTime = 0
hrSlept = 0
minSlept = 0
firstDate = 0

# Slightly more complex but still basic data
# This is not stored within the file, it is determined based on existing data
shouldExercise = False
canEat = False
canHaveCaffiene = False
canHaveLight = False

# Related to override information
overrideStartDate = ""
overrideEndDate = ""
overrideOffsets = [0, 0]

# Sets up some stuff
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = ""
stats_window = ""
log_window = ""

# Writes the data into the file
def Write_Data():
    
    global firstDate, fatigueScore, hrToSleep, minToSleep, hrToWake, minToWake, hrTarget, minTarget, minSlept, hrSlept, lastSleptTime, overrideStartDate, overrideEndDate, overrideOffsets
    
    Remove_Protection()
    
    fileData = open(filePath, "w")

    fileData.write(f"Starting Date: {firstDate.month}/{firstDate.day}/{firstDate.year}\n")
    fileData.write(f"Fatigue Score: {fatigueScore}\n")
    fileData.write(f"Recommended Sleep Time: {hrToSleep}:{minToSleep:02d}\n")
    fileData.write(f"Recommended Wake Time: {hrToWake}:{minToWake:02d}\n")
    fileData.write(f"Sleep duration in mins: {hrTarget * 60 + minTarget}\n")                    
    fileData.write(f"Time slept: {hrSlept * 60 + minSlept}\n")               
    fileData.write(f"Last slept: {lastSleptTime.hour}:{lastSleptTime.minute:02d}:{lastSleptTime.second:02d} {lastSleptTime.month}/{lastSleptTime.day}/{lastSleptTime.year}\n")

    if type(overrideStartDate) == str:
        fileData.write(f"Override start: 0/0/0\n")

    else:
        fileData.write(f"Override start: {overrideStartDate.month}/{overrideStartDate.day}/{overrideStartDate.year}\n")

    if type(overrideEndDate) == str:
        fileData.write(f"Override end: 0/0/0\n")

    else:
        fileData.write(f"Override end: {overrideEndDate.month}/{overrideEndDate.day}/{overrideEndDate.year}\n")    

    if type(overrideOffsets) == str:
        fileData.write(f"Override offset: 0,0")

    else:
        fileData.write(f"Override offset: {overrideOffsets[0]},{overrideOffsets[1]}")
            
    fileData.close()
    Add_Protection()

# Loads the data from the file
def Load_Data():
     
    global firstDate, fatigueScore, hrToSleep, minToSleep, hrToWake, minToWake, hrTarget, minTarget, minSlept, hrSlept, lastSleptTime, overrideStartDate, overrideEndDate, overrideOffsets
        
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
            firstDate = datetime(int(splitLine[2]), int(splitLine[0]), int(splitLine[1]))

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
            
        # Gets the time slept
        elif index == 6:
                    
            newLine = line.split(": ")
            newLine = newLine[1]
            newLine = newLine.split(" ")
            timeLine = newLine[0].split(":")
            dateLine = newLine[1].split("/")

            lastSleptTime = datetime(int(dateLine[2]), int(dateLine[1]), int(dateLine[0]), int(timeLine[0]), int(timeLine[1]), int(timeLine[2]))

        # Gets override
        elif index == 7:

            newLine = line.split(": ")
            dateLine = newLine[0].split("/")
            overrideStartDate = datetime(int(splitLine[2]), int(splitLine[0]), int(splitLine[1]))

        # Gets override
        elif index == 8:

            newLine = line.split(": ")
            dateLine = newLine[0].split("/")
            overrideEndDate = datetime(int(splitLine[2]), int(splitLine[0]), int(splitLine[1]))

        # Gets override
        elif index == 9:

            newLine = line.split(": ")
            newLine = newLine[1].split(",")
            overrideOffsets = int(newLine)

        line = fileData.readline()
        index += 1

    fileData.close()

    Add_Protection() 

def Reset_Data():
                
    global firstDate, fatigueScore, hrToSleep, minToSleep, hrToWake, minToWake, hrTarget, minTarget, minSlept, hrSlept, lastSleptTime, overrideStartDate, overrideEndDate, overrideOffsets
    Load_Data()
    Write_Data()

# Main window class, this is where the user will be able to interact with the program
class UI_MainWindow(QMainWindow):
    
    def __init__(self):
        
        super(UI_MainWindow, self).__init__()
        self.setWindowTitle("Universal Sleep Tracker")
        self.setGeometry(200, 200, 800, 600)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 300, 30))
        self.logButton = QPushButton(self.centralwidget)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(50, 100, 150, 30))
        self.recButton = QPushButton(self.centralwidget)
        self.recButton.setObjectName(u"recButton")
        self.recButton.setGeometry(QRect(50, 150, 150, 30))
        self.statsButton = QPushButton(self.centralwidget)
        self.statsButton.setObjectName(u"statsButton")
        self.statsButton.setGeometry(QRect(50, 200, 150, 30))
        self.overrideButton = QPushButton(self.centralwidget)
        self.overrideButton.setObjectName(u"overrideButton")
        self.overrideButton.setGeometry(QRect(50, 250, 150, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    
        self.logButton.clicked.connect(self.enter_sleep_log)
            
        self.recButton.clicked.connect(self.show_recommendations)
        
        self.statsButton.clicked.connect(self.show_stats)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Universal Sleep Tracker", None))
        self.logButton.setText(QCoreApplication.translate("MainWindow", u"Log Sleep", None))
        self.recButton.setText(QCoreApplication.translate("MainWindow", u"Show Recommendations", None))
        self.statsButton.setText(QCoreApplication.translate("MainWindow", u"Show Stats", None))
        self.overrideButton.setText(QCoreApplication.translate("MainWindow", u"Override", None))

    def enter_sleep_log(self):
        global widget
        
        widget.setCurrentIndex(2)  # Switch to the log window
        
        if type(log_window) is QLabel:
            log_window.notif.setText("Error: Sleep start time must be before sleep end time on the same day.")

    def manual_override(self):
        pass # Manually overrides sleep schedule
    
    def show_recommendations(self):
        pass # Placeholder for the function that will show recommendations based on the user's sleep data
    
    def show_stats(self):
        
        global widget
        
        widget.setCurrentIndex(1)  # Switch to the stats window
        
        if type(stats_window) is QLabel:
            stats_window.update_stats()
    
    def closeEvent(self, event):
        pass # Possibly does something when the window is closed, like saving data or cleaning up resources

# Stats window, shows the stats of the user
class Stats_Window(QMainWindow):
    
    def __init__(self):
        
        super(Stats_Window, self).__init__()
        self.setWindowTitle("Stats")
        self.setGeometry(200, 200, 800, 600)
        self.setupUi(self)
        
    def update_stats(self):
        
        Update_Time()
        Remove_Protection()

        Reset_Data()

        fileData = open(filePath, "r")
        line = fileData.readline()

        index = 0

        # Reads data and initializes it
        while line:

            if index == 1:
                
                self.fatigue.setText(f"Fatigue Score: {fatigueScore}")
            
            if index == 2:
                
                self.recSleep.setText(f"Recommended Sleep Time: {hrToSleep + int(overrideOffsets[0] / 60)}:{int(overrideOffsets[0] % 60) + minToSleep:02d}")
            
            if index == 3:
                
                self.recWake.setText(f"Recommended Wake Time: {hrToWake + int(overrideOffsets[1] / 60)}:{int(overrideOffsets[1] % 60) + minToWake:02d}")
            
            if index == 4:
                
                self.targetSleep.setText(f"Sleep target: {hrTarget}:{minTarget:02d}")
            
            if index == 5:
                
                self.sleepDuration.setText(f"Time slept: {hrSlept}:{minSlept:02d}")
            
            if index == 6:
                                
                self.lastSlept.setText(f"Last Slept: {lastSleptTime.hour}:{lastSleptTime.minute:02d} {lastSleptTime.month}/{lastSleptTime.day}/{lastSleptTime.year}")
            
            line = fileData.readline()
            index += 1

        fileData.close()
        Add_Protection()
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 200, 30))
        font = QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.fatigue = QLabel(self.centralwidget)
        self.fatigue.setObjectName(u"fatigue")
        self.fatigue.setGeometry(QRect(50, 115, 200, 30))
        self.recSleep = QLabel(self.centralwidget)
        self.recSleep.setObjectName(u"recSleep")
        self.recSleep.setGeometry(QRect(50, 175, 200, 30))
        self.recWake = QLabel(self.centralwidget)
        self.recWake.setObjectName(u"recWake")
        self.recWake.setGeometry(QRect(50, 235, 200, 30))
        self.targetSleep = QLabel(self.centralwidget)
        self.targetSleep.setObjectName(u"targetSleep")
        self.targetSleep.setGeometry(QRect(50, 295, 200, 30))
        self.sleepDuration = QLabel(self.centralwidget)
        self.sleepDuration.setObjectName(u"sleepDuration")
        self.sleepDuration.setGeometry(QRect(50, 355, 200, 30))
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(50, 500, 150, 30))
        self.lastSlept = QLabel(self.centralwidget)
        self.lastSlept.setObjectName(u"lastSlept")
        self.lastSlept.setGeometry(QRect(50, 415, 200, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.update_stats()
        self.exit.clicked.connect(self.back_to_main)
        
    def back_to_main(self):
        global widget
        widget.setCurrentIndex(0)  # Switch back to the main window

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.fatigue.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.recSleep.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.recWake.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.sleepDuration.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.lastSlept.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# Logs the sleep data, this is where the user will enter when they slept and when they woke up
class Log_Window(QMainWindow):
    
    def __init__(self):
        
        super(Log_Window, self).__init__()
        self.setWindowTitle("Log Sleep Data")
        self.setGeometry(200, 200, 800, 600)
        self.setupUi(self)
                
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sleepStartLog = QDateTimeEdit(self.centralwidget)
        self.sleepStartLog.setObjectName(u"sleepStartLog")
        self.sleepStartLog.setGeometry(QRect(50, 200, 200, 30))
        self.sleepEndLog = QDateTimeEdit(self.centralwidget)
        self.sleepEndLog.setObjectName(u"sleepEndLog")
        self.sleepEndLog.setGeometry(QRect(50, 350, 200, 30))
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 300, 30))
        font = QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.logSleep = QPushButton(self.centralwidget)
        self.logSleep.setObjectName(u"logSleep")
        self.logSleep.setGeometry(QRect(50, 450, 150, 30))
        palette = QPalette()
        brush = QBrush(QColor(5, 77, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.logSleep.setPalette(palette)
        self.cancelLog = QPushButton(self.centralwidget)
        self.cancelLog.setObjectName(u"cancelLog")
        self.cancelLog.setGeometry(QRect(50, 500, 150, 30))
        palette1 = QPalette()
        brush1 = QBrush(QColor(240, 0, 4, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.cancelLog.setPalette(palette1)
        self.sleepStartTitle = QLabel(self.centralwidget)
        self.sleepStartTitle.setObjectName(u"sleepStartTitle")
        self.sleepStartTitle.setGeometry(QRect(50, 150, 300, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.sleepStartTitle.setFont(font1)
        self.sleepEndTitle = QLabel(self.centralwidget)
        self.sleepEndTitle.setObjectName(u"sleepEndTitle")
        self.sleepEndTitle.setGeometry(QRect(50, 300, 300, 30))
        self.sleepEndTitle.setFont(font1)
        self.notif = QLabel(self.centralwidget)
        self.notif.setObjectName(u"notif")
        self.notif.setGeometry(QRect(500, 200, 200, 100))
        self.notif.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.logSleep.clicked.connect(self.log_sleep)
        
        self.cancelLog.clicked.connect(self.back_to_main)
        
    # setupUi
    
    def log_sleep(self):
        
        global lastSleptTime, hrSlept, minSlept, fatigueScore
        
        # Create a timezone using an IANA text ID
        tz_id = QByteArray(b"Europe/Paris")
        time_zone = QTimeZone(tz_id)
        
        sleep_start = self.sleepStartLog.dateTime().toPython().replace(tzinfo=timezone.utc)
        sleep_end = self.sleepEndLog.dateTime().toPython().replace(tzinfo=timezone.utc)
        
        sleep_start_adjusted = QDateTime(sleep_start).toTimeZone(time_zone)
        sleep_end_adjusted = QDateTime(sleep_end).toTimeZone(time_zone)
        
        Update_Time()  # Update the current time to ensure we have the latest time for validation
        
        if (sleep_start >= sleep_end):
            self.notif.setText("Error: Sleep start time must be before sleep end time.")
            self.notif.setStyleSheet("color: red;")
            return
        
        elif sleep_start_adjusted.secsTo(sleep_end_adjusted) > 24 * 3600:
            self.notif.setText("Error: Sleep duration cannot exceed 24 hours.")
            self.notif.setStyleSheet("color: red;")
            return
        
        elif (sleep_start_adjusted > currDateTime) or (sleep_end_adjusted > currDateTime):
            self.notif.setText("Error: Sleep times cannot be in the future.")
            self.notif.setStyleSheet("color: red;")
            return
        
        elif (sleep_start_adjusted < lastSleptTime) or (sleep_end_adjusted < lastSleptTime):
            self.notif.setText("Error: Sleep times cannot be before the last slept time. (Last slept: " + str(lastSleptTime.hour) + ":" + str(lastSleptTime.minute) + " " + str(lastSleptTime.month) + "/" + str(lastSleptTime.day) + "/" + str(lastSleptTime.year) + ")")
            self.notif.setStyleSheet("color: red;")
            return
        
        elif (sleep_start == sleep_end):
            self.notif.setText("Error: Sleep start and end times cannot be the same.")
            self.notif.setStyleSheet("color: red;")
            return
        
        elif (sleep_start.date() == sleep_end.date()) and (sleep_start.time() > sleep_end.time()):
            self.notif.setText("Error: Sleep start time must be before sleep end time on the same day.")
            self.notif.setStyleSheet("color: red;")
            return
        
        else:
            
            self.notif.setText("Successfully logged!")
            self.notif.setStyleSheet("color: green;")           
                 
            if (sleep_start.date() == sleep_end.date()):                
                
                lastSleptTime = sleep_end
                hrSlept += (sleep_end - sleep_start).seconds // 3600
                minSlept += ((sleep_end - sleep_start).seconds % 3600) // 60
                
                Reset_Data()
                
            else:
                                
                lastSleptTime = sleep_end
                
                hrDiff = hrSlept - hrTarget
                minDiff = minSlept - minTarget
                
                # Limits on fatigue score, it cannot go below 0 or above 100
                # The fatigue score is calculated based on the difference between the actual sleep duration and the target sleep duration
                
                if (hrDiff < 0):
                    hrDiff = -hrDiff
                    
                if (minDiff < 0):
                    minDiff = -minDiff
                    
                if (hrDiff == 0):
                    if (minDiff == 0):
                        fatigueScore -= 0  # No change in fatigue score if the sleep duration matches the target duration
                    else:
                        fatigueScore -= minDiff // 15  # Each 15 minutes of difference changes the fatigue score by 1 point
                    
                fatigueScore -= (hrDiff * 60 + minDiff) // 15  # Each 15 minutes of difference changes the fatigue score by 1 point
                
                if (fatigueScore < 0):
                    fatigueScore = 0
                    
                elif (fatigueScore > 100):
                    fatigueScore = 100
                
                hrSlept = 0
                minSlept = 0          
                    
                Reset_Data()
                
                hrSlept += (sleep_end - sleep_start).seconds // 3600
                minSlept += ((sleep_end - sleep_start).seconds % 3600) // 60
        
    def back_to_main(self):
        global widget
        widget.setCurrentIndex(0)  # Switch back to the main window

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Enter Sleep Log", None))
        self.logSleep.setText(QCoreApplication.translate("MainWindow", u"Log Sleep", None))
        self.cancelLog.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.sleepStartTitle.setText(QCoreApplication.translate("MainWindow", u"Enter start time of sleep", None))
        self.sleepEndTitle.setText(QCoreApplication.translate("MainWindow", u"Enter end time of sleep", None))
        self.notif.setText("")
    # retranslateUi

# Actually runs the program, this is where the main window is created and shown
def window():
    
    widget.setWindowTitle("Universal Sleep Tracker")
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    main_window = UI_MainWindow()
    widget.addWidget(main_window)
    stats_window = Stats_Window()
    widget.addWidget(stats_window)
    log_window = Log_Window()
    widget.addWidget(log_window)
    widget.show()
    sys.exit(app.exec())

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

    FILE_ATTRIBUTE_PROTECTED = None
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
    fileData.write("Starting Date: " + str(currDateTime.month) + "/" + str(currDateTime.day) + "/" + str(currDateTime.year) + "\n")
    fileData.write("Fatigue Score: 30\n")
    fileData.write("Recommended Sleep Time: 22:30\n")
    fileData.write("Recommended Wake Time: 06:30\n")
    fileData.write("Sleep duration in mins: 480\n")
    fileData.write("Time slept: 0\n")
    fileData.write("Last slept: " + str(currDateTime.hour) + ":" + str(currDateTime.minute) + ":" + str(currDateTime.second) + " " + str(currDateTime.month) + "/" + str(currDateTime.day) + "/" + str(currDateTime.year) + "\n")
    fileData.write("Override start: 0/0/0 \n")
    fileData.write("Override end: 0/0/0 \n")
    fileData.write("Override offset: " + str(overrideOffsets[0]) + "," + str(overrideOffsets[1]))
                

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
        firstDate = datetime(int(splitLine[2]), int(splitLine[1]), int(splitLine[0]))

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
        
    # Gets the time slept
    elif index == 6:
                
        newLine = line.split(": ")
        newLine = newLine[1]
        newLine = newLine.split(" ")
        timeLine = newLine[0].split(":")
        dateLine = newLine[1].split("/")

        lastSleptTime = datetime(int(dateLine[2]), int(dateLine[1]), int(dateLine[0]), int(timeLine[0]), int(timeLine[1]), int(timeLine[2]))

    line = fileData.readline()
    index += 1

fileData.close()

Add_Protection()

window()