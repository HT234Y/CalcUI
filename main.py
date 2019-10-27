import sys
from ui import Ui_Dialog
from PySide import QtCore, QtGui
#from Qt import QtWidgets

app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def Plus():
    ui.label.setText('+')

def Minus():
    ui.label.setText('-')

def Multiply():
    ui.label.setText('*')

def Tosplit():
    ui.label.setText('/')

def getResult():
    try:
        n1 = int(ui.lineone.text())
        n2 = int(ui.linetwo.text())
        n3 = ui.label.text()

        if str(n3) == '+':
            ui.result.setText(str(n1 + n2))

        if str(n3) == '-':
            ui.result.setText(str(n1 - n2))

        if str(n3) == '*':
            ui.result.setText(str(n1 * n2))

        if str(n3) == '/':
            ui.result.setText(str(n1 / n2))

    except ZeroDivisionError:
        QtGui.QMessageBox.critical(None,'Тобi пiзда тiкай з села!!',"ВЛАД ТЫ ШО @#$% ? НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!!", QtGui.QMessageBox.Abort)
    
ui.equally.clicked.connect(getResult)
ui.plus.clicked.connect(Plus)
ui.minus.clicked.connect(Minus)
ui.multiply.clicked.connect(Multiply)
ui.tosplit.clicked.connect(Tosplit)

sys.exit(app.exec_())
