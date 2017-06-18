# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:57:00 2017
ANACONDA DISTRIBUTION   SPYDER IDE
@author: LALIT ARORA
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(372, 211)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(90, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QLineEdit(Login)
        self.user.setGeometry(QtCore.QRect(160, 60, 121, 20))
        self.user.setObjectName("user")
        self.passw = QtWidgets.QLineEdit(Login)
        self.passw.setGeometry(QtCore.QRect(160, 100, 121, 20))
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw.setObjectName("passw")
        
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(130, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(130, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "Username"))
        self.label_2.setText(_translate("Login", "Password"))
        
        self.label_4.setText(_translate("Login", "LOGIN WINDOW"))
        self.pushButton.setText(_translate("Login", "LOGIN"))
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
    def log(self):
        conn=sqlite3.connect('logincred.sqlite')
        c=conn.cursor()
        conn.commit()
        getuser=str(self.user.text())
        getpass=str(self.passw.text())
        print(getuser)
        accepted=[]
        for val in c.execute("SELECT * FROM cred where user = '%s' "%getuser):
            accepted.append(val)
        print(accepted)
        if len(accepted)!=0:
            if getpass==str(accepted[0][1]) and getuser==str(accepted[0][0]):
                self.showMessageBox('Info','Successful Login!')
                self.user.setText("")
                self.passw.setText("")
            else:
                self.showMessageBox('Warning','Invalid Username or Password!')
                self.user.setText("")
                self.passw.setText("")
        else:
            self.showMessageBox('Warning','Invalid Username or Password!')
            self.user.setText("")
            self.passw.setText("")
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
