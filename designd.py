from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 246)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_conf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conf.setGeometry(QtCore.QRect(100, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_conf.setFont(font)
        self.pushButton_conf.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_conf.setObjectName("pushButton_conf")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 51, 29))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_valor.setGeometry(QtCore.QRect(120, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_valor.setFont(font)
        self.lineEdit_valor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_valor.setObjectName("lineEdit_valor")
        self.lineEdit_dsenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dsenha.setGeometry(QtCore.QRect(120, 90, 251, 31))
        self.lineEdit_dsenha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_dsenha.setObjectName("lineEdit_dsenha")
        self.label_erro = QtWidgets.QLabel(self.centralwidget)
        self.label_erro.setGeometry(QtCore.QRect(60, 150, 383, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.label_erro.setFont(font)
        self.label_erro.setText("")
        self.label_erro.setObjectName("label_erro")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(380, 100, 70, 21))
        self.checkBox.setStyleSheet("")
        self.checkBox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/5518752821543238880-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox.setIcon(icon)
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco Lucas Reis"))
        self.pushButton_conf.setText(_translate("MainWindow", "Depositar"))
        self.label_4.setText(_translate("MainWindow", "Valor:"))
        self.label.setText(_translate("MainWindow", "Senha:"))
        self.pushButton.setText(_translate("MainWindow", "Sacar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
