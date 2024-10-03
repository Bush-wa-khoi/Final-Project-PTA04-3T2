from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget tu pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong

class Login(QMainWindow):
    # ham khoi tao giao dien UI
    def __init__(self):
        super().__init__()
        # doc giao dien tu file login.ui
        uic.loadUi("Ui-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        if self.txtemail.text() == "DoMinhKhoi" and self.txtpassword.text() == "123":
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    lg.show()
    app.exec()