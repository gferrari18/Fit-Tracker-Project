# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reguserscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegUserScreen(object):
    def setupUi(self, RegUserScreen):
        RegUserScreen.setObjectName("RegUserScreen")
        RegUserScreen.resize(792, 171)
        self.pushButton = QtWidgets.QPushButton(RegUserScreen)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(RegUserScreen)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.entername = QtWidgets.QLabel(RegUserScreen)
        self.entername.setGeometry(QtCore.QRect(100, 10, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setKerning(False)
        self.entername.setFont(font)
        self.entername.setAlignment(QtCore.Qt.AlignCenter)
        self.entername.setObjectName("entername")
        self.pushButton_2 = QtWidgets.QPushButton(RegUserScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(RegUserScreen)
        QtCore.QMetaObject.connectSlotsByName(RegUserScreen)

    def retranslateUi(self, RegUserScreen):
        _translate = QtCore.QCoreApplication.translate
        RegUserScreen.setWindowTitle(_translate("RegUserScreen", "Dialog"))
        self.pushButton.setText(_translate("RegUserScreen", "Submit"))
        self.entername.setText(_translate("RegUserScreen", "Please enter your name (as registered):"))
        self.pushButton_2.setText(_translate("RegUserScreen", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegUserScreen = QtWidgets.QDialog()
    ui = Ui_RegUserScreen()
    ui.setupUi(RegUserScreen)
    RegUserScreen.show()
    sys.exit(app.exec_())
