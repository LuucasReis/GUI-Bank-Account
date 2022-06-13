from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 573)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(80, 10, 256, 281))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair.setGeometry(QtCore.QRect(430, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sair.setFont(font)
        self.pushButton_sair.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_sair.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/158970505916276584893773-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sair.setIcon(icon)
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QtCore.QRect(90, 320, 231, 29))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.label_welcome.setFont(font)
        self.label_welcome.setText("")
        self.label_welcome.setObjectName("label_welcome")
        self.label_saldo = QtWidgets.QLabel(self.centralwidget)
        self.label_saldo.setGeometry(QtCore.QRect(80, 380, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        self.label_saldo.setFont(font)
        self.label_saldo.setText("")
        self.label_saldo.setObjectName("label_saldo")
        self.pushButton_foto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_foto.setGeometry(QtCore.QRect(410, 450, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_foto.setFont(font)
        self.pushButton_foto.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_foto.setObjectName("pushButton_foto")
        self.pushButton_depositar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_depositar.setGeometry(QtCore.QRect(410, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_depositar.setFont(font)
        self.pushButton_depositar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_depositar.setObjectName("pushButton_depositar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 480, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_ts = QtWidgets.QLabel(self.centralwidget)
        self.label_ts.setGeometry(QtCore.QRect(50, 520, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_ts.setFont(font)
        self.label_ts.setText("")
        self.label_ts.setObjectName("label_ts")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Perfil "))
        self.pushButton_foto.setText(_translate("MainWindow", "Alterar Foto"))
        self.pushButton_depositar.setText(_translate("MainWindow", "Transações"))
        self.label_2.setText(_translate("MainWindow", "     SUA ULTIMA TRANSAÇÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
