from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget tu pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong
# Lop trang chu
import webbrowser
class Home(QMainWindow): 
    def __init__(self):
        super().__init__() 
        uic.loadUi("Ui-GiaoDien/homenote.ui", self)
        self.btnPush1.clicked.connect(self.takenote)
    def takenote(self):
        takenote.show()

class Takenote(QMainWindow): 
     def __init__(self):
        super().__init__() 
        uic.loadUi("Ui-GiaoDien/takenote.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    takenote = Takenote()
    home.show()
    app.exec()