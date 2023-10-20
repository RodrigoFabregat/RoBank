from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


def some_function():
    from gui.main import MainWindow


class RegisterWindow():
    def __init__(self):
        self.v = uic.loadUi("gui/register.ui")
        self.v.show()
