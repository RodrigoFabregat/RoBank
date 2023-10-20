
# Convierto el archivo de Qt6 en un archivo de python
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from model.userModel import User
from data.user import UserData
from gui.main import MainWindow


def some_function():
    from gui.main import MainWindow


class Login():
    def __init__(self):
        self.login = uic.loadUi("gui/Login.ui")
        self.initGUI()
        self.login.lblError.setText("")
        self.login.show()

    def Enter(self):
        if len(self.login.txtUser.text()) < 5:
            self.login.lblError.setText("Enter a valid username")
            self.login.txtUser.setFocus()
        elif len(self.login.txtPassword.text()) < 5:
            self.login.lblError.setText("Enter a valid password")
            self.login.txtPassword.setFocus()
        else:
            self.login.lblError.setText("")
            usu = User(user=self.login.txtUser.text(),
                       key=self.login.txtPassword.text())
            usuData = UserData()
            res = usuData.login(usu)
            if res:
                self.main = MainWindow()  # Abro la ventana maximizada
                self.login.hide()  # Oculto la ventana LOGIN
            else:
                self.login.lblError.setText("incorrect access data")

    def initGUI(self):
        self.login.btnAccess.clicked.connect(self.Enter)
