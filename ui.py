# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\calculatorInvalid\preUI.ui'
#
# Created: Wed May  1 17:23:33 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 164)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0.335, y1:0.766682, x2:1, y2:0, stop:0.0965909 rgba(31, 31, 31, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: white;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: green;\n"
"}")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 120, 161, 32))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineone = QtGui.QLineEdit(Dialog)
        self.lineone.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.lineone.setStyleSheet("")
        self.lineone.setObjectName("lineone")
        self.linetwo = QtGui.QLineEdit(Dialog)
        self.linetwo.setGeometry(QtCore.QRect(210, 30, 151, 31))
        self.linetwo.setStyleSheet("")
        self.linetwo.setObjectName("linetwo")
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 100, 381, 60))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plus = QtGui.QPushButton(self.gridLayoutWidget)
        self.plus.setObjectName("plus")
        self.gridLayout.addWidget(self.plus, 0, 0, 1, 1)
        self.minus = QtGui.QPushButton(self.gridLayoutWidget)
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 0, 1, 1, 1)
        self.multiply = QtGui.QPushButton(self.gridLayoutWidget)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 0, 2, 1, 1)
        self.tosplit = QtGui.QPushButton(self.gridLayoutWidget)
        self.tosplit.setObjectName("tosplit")
        self.gridLayout.addWidget(self.tosplit, 0, 3, 1, 1)
        self.result = QtGui.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(450, 30, 111, 31))
        self.result.setText("")
        self.result.setObjectName("result")
        self.equally = QtGui.QPushButton(Dialog)
        self.equally.setGeometry(QtCore.QRect(380, 30, 41, 31))
        self.equally.setStyleSheet("")
        self.equally.setObjectName("equally")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 16, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.minus.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.multiply.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.tosplit.setText(QtGui.QApplication.translate("Dialog", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.equally.setText(QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))

