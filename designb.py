from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 256, 256))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Downloads/12538834121580217334-256.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 380, 32, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Downloads/userlogin (1).png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 330, 32, 35))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../../../Downloads/userpassword.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_entrar.setGeometry(QtCore.QRect(210, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_entrar.setFont(font)
        self.pushButton_entrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(410, 510, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cadastrar.setFont(font)
        self.pushButton_cadastrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 520, 150, 29))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(130, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(130, 390, 251, 31))
        self.lineEdit_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 430, 383, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(390, 396, 70, 21))
        self.checkBox.setStyleSheet("")
        self.checkBox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/5518752821543238880-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox.setIcon(icon)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco Lucas Reis"))
        self.pushButton_entrar.setText(_translate("MainWindow", "Entrar"))
        self.pushButton_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.label_4.setText(_translate("MainWindow", "Não possui cadastro?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
