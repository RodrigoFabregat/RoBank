from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from gui.register import RegisterWindow
from model.movements import Transfer
from data.transfer import TransData
from data.city import CityData
from data.depositData import DepositData, DepositInter
from data.transfer import TransData


class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnRegTransfers.triggered.connect(self.OpenRegister)
        self.main.btnReportTransfers.triggered.connect(self.OpenDeposit)
        self.register = uic.loadUi("gui/register.ui")
        self.deposit = uic.loadUi("gui/deposit.ui")

    def OpenRegister(self):
        self.register.btnRegister.clicked.connect(self.RegisterTrans)
        self.register.show()

    def OpenDeposit(self):
        self.deposit.btnRegister.clicked.connect(self.RegisterTrans)
        self.deposit.show()
        self.FillCitys()

# Tranfers

    def RegisterTrans(self):
        if self.register.cbType.currentText() == "--- Select option":
            mBox = QMessageBox()
            mBox.setText("You must select a type of document")
            mBox.exec()
            self.register.cbType.setFocus()
        elif len(self.register.txtDocument.text()) < 6:
            mBox = QMessageBox()
            mBox.setText("You must enter a valid document")
            mBox.exec()
            self.register.txtDocument.setFocus()

        elif self.register.cbMotive.currentText() == "--- Select option":
            mBox = QMessageBox()
            mBox.setText("You must select a type of reason")
            mBox.exec()
            self.register.cbMotive.setFocus()
        elif not self.register.txtAmount.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("You must enter a valid amount")
            mBox.exec()
            self.register.txtAmount.setText("0")
            self.register.txtAmount.setFocus()
        else:
            transfers = Transfer(
                type=self.register.cbType.currentText(),
                document=self.register.txtDocument.text(),
                amount=self.register.txtAmount.text(),
                motive=self.register.cbMotive.currentText(),
                international=self.register.checkInter.isChecked()
            )
            objData = TransData()
            mBox = QMessageBox()
            if objData.register(info=transfers):
                mBox.setText("Registered transfer")
                self.cleanFieldTrans()
            else:
                mBox.setText("Unregistered transfer")
            mBox.exec()

    def cleanFieldTrans(self):
        self.register.cbType.setCurrentIndex(0)
        self.register.cbMotive.setCurrentIndex(0)
        self.register.txtDocument.setText("")
        self.register.txtAmount.setText("0")
        self.register.checkInter.setChecked(False)
        self.register.txtDocument.setFocus()


###### Deposit ###############


    def FillCitys(self):
        objData = CityData()
        data = objData.CityList()

        for item in data:
            self.deposit.cbPlace.addItem(item[1])

    def ValidateFields(self) -> bool:
        mBox = QMessageBox()
        if not self.deposit.txtDocument.text() or not self.deposit.FirstName.text() or not self.deposit.LastName.text() or not self.deposit.txtAmount.text() or self.deposit.cbMotive.currentText() == "--- Select option" or self.deposit.cbPlace.currentText() == "--- Select option" or self.deposit.cbSex.currentText() == "--- Select option" or self.deposit.cbType.currentText() == "--- Select option":
            return False
        else:
            return True

    def RegisterDeposit(self):
        if not self.ValidateFields():
            mBox = QMessageBox()
            mBox.setText("You must fill out the required fields (*)")
            mBox.exec()

        else:
            dateN = self.deposit.txtBirthdate.date().toPyDate()
            deposit = DepositInter(
                type=self.deposit.cbType.currentText(),
                document=self.deposit.txtDocument.text(),
                amount=self.deposit.txtAmount.text(),
                motive=self.deposit.cbMotive.currentText(),
                birthplace=self.deposit.cbPlace.currentText(),
                birthdate=dateN,
                sex=self.deposit.cbSex.currentText(),
                international=True,
                name=self.deposit.txtFirstName.currentText(),
                lastname=self.deposit.txtLastname.currentText(),
                terms=self.deposit.checkTerms.isChecked()
            )
            objData = DepositData()
            mBox = QMessageBox()
            if objData.register(info=deposit):
                mBox.setText("Registered deposit")
                # self.cleanFieldTrans()
            else:
                mBox.setText("Unregistered deposit")
            mBox.exec()
