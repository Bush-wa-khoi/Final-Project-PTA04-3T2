from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget tu pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong
# Lop trang chu

class HomeDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        # doc giao dien tu file login.ui
        uic.loadUi("Ui-GiaoDien/home.ui", self)
        self.btnHome.clicked.connect(self.showHome)
        self.btnProfile.clicked.connect(self.showProfile)
    def showHome(self):
        self.stackedMenu.setCurrentIndex(1)
    def showProfile(self):
        self.stackedMenu.setCurrentIndex(2)
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui-GiaoDien/signup.ui", self)
        # them su kien khi nhan vao nut dang ky
        self.btnSignUp.clicked.connect(self.registerAccount)
        self.btnLogin.clicked.connect(self.ShowLogin)
    def ShowLogin(self):
        self.close()
        lg.show()

    def registerAccount(self):
        # doc thong tin nguoi dung nhap vao 
        username = self.txtEmail
        password = self.txtpassword
        comfirmPassWord = self.txtcomfirmpassword

        # neu chua nhap thi cho nguoi dung nhap 
        if username.text() == "":
            username.setFocus()
            return
        if password.text() == "":
            password.setFocus()
            return
        if comfirmPassword.text() == "":
            confirmPassWord.setFocus()
            return
        # neu nhu email khong dung dinh dang
        if username.text().find("@gmail.com") == -1:
            username.clear()
            username.setFocus()
            return
        # neu nhu mat khau va nhap lai mat khau thong dung
        if password.text() != confirmPassword.text():
            comfirmPassword.setFocus()
            return
        # them tai khoan moi vao file
        with open("accounts.txt", "a") as file:
             file.write(username.text() + ":" + password.text() + "\n")
        self.close

class Login(QMainWindow):
    # ham khoi tao giao dien UI
    def __init__(self):
        super().__init__()
        # doc giao dien tu file login.ui
        uic.loadUi("Ui-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
        # neu chua co tau khoan,qua trang SignUp
        self.btnSignup.clicked.connect(self.showSignUp)
    def showSignUp(self):
        self.close()
        su.show()
    def checkLogin(self):
   
        # mo file txt len de doc thong tin
        with open("accounts.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)
            
        if self.txtEmail.text() + ":" + self.txtpassword.text() in accounts:
            self.close()
            home.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    su = SignUp()
    home = HomeDashboard()
    lg.show()
    # lg.show()
    app.exec()