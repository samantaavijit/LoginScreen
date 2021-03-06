# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class LoginScreen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 442)
        # Hide action button and title
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # transparent background
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 410))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 410))
        self.label.setStyleSheet("background-color: rgba(16, 30,41,240);\n"
                                 "border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.userName = QtWidgets.QLineEdit(self.widget)
        self.userName.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName.setFont(font)
        self.userName.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "border:1px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color: rgb(46, 82, 101);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding-bottom:7px")
        self.userName.setObjectName("userName")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(20, 260, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "border:1px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color: rgb(46, 82, 101);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding-bottom:7px")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                                      "    background-color: rgba(2, 65, 118,255);\n"
                                      "    color: rgba(255, 255, 255, 200);\n"
                                      "    border-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#pushButton:pressed{\n"
                                      "padding-left:5px;\n"
                                      "padding-top:5px;\n"
                                      "background-color: rgba(2, 65, 118,100);\n"
                                      "background-position:calc(100%-10px)center;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#pushButton:hover{\n"
                                      "    background-color: rgba(2, 65, 118,200);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.adminImage = QtWidgets.QLabel(self.widget)
        self.adminImage.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setPointSize(90)
        self.adminImage.setFont(font)
        self.adminImage.setStyleSheet("color: rgba(0, 125, 236,255);")
        self.adminImage.setAlignment(QtCore.Qt.AlignCenter)
        self.adminImage.setObjectName("adminImage")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(266, 3, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius:10px;")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.close_window)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userName.setPlaceholderText(_translate("Form", " User Name"))
        self.password.setPlaceholderText(_translate("Form", " Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.adminImage.setText(_translate("Form", ""))
        self.closeButton.setText(_translate("Form", "╳"))

    def close_window(self):
        Form.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ''' add Custom font'''
    # app = QtGui.QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('path/to/font')
    # # or load the font data directly
    # # QtGui.QFontDatabase.addApplicationFontFromData(fontdata)
    # stylesheet = open('mystylesheet.qss').read()
    # app.setStyleSheet(stylesheet)
    Form = QtWidgets.QWidget()
    ui = LoginScreen()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
