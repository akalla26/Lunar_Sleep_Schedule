from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QLineEdit, QGroupBox, QDateEdit
import sys

class MyWindow(QMainWindow):
    
    def __init__(self):
        
        super(MyWindow, self).__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(0, 0, 1920, 1080)
        self.setup_ui()
        
    def setup_ui(self):

        self.label = QLabel("Hello, World!", self)
        self.label.setGeometry(50, 50, 200, 30)

        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(50, 100, 100, 30)
        self.button.clicked.connect(self.clicked)
        
    def clicked(self):
        
        self.label.setText("Button clicked!")
        self.label.adjustSize()
        
def window():
    
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
    
window()