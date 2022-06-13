from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 595)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 251, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Downloads/12538834121580217334-256.png"))
        self.label.setObjectName("label")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(410, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.pushButton_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastro.setGeometry(QtCore.QRect(360, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cadastro.setFont(font)
        self.pushButton_cadastro.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_cadastro.setObjectName("pushButton_cadastro")
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(110, 300, 241, 31))
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
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(150, 340, 261, 31))
        self.lineEdit_cpf.setMinimumSize(QtCore.QSize(251, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_cpf.setFont(font)
        self.lineEdit_cpf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.label_errocadastro = QtWidgets.QLabel(self.centralwidget)
        self.label_errocadastro.setGeometry(QtCore.QRect(80, 550, 383, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.label_errocadastro.setFont(font)
        self.label_errocadastro.setText("")
        self.label_errocadastro.setObjectName("label_errocadastro")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 390, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 430, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 470, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(190, 380, 251, 31))
        self.lineEdit_nome.setMinimumSize(QtCore.QSize(251, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_senhac = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senhac.setGeometry(QtCore.QRect(230, 420, 251, 31))
        self.lineEdit_senhac.setMinimumSize(QtCore.QSize(251, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_senhac.setFont(font)
        self.lineEdit_senhac.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_senhac.setObjectName("lineEdit_senhac")
        self.lineEdit_cfsenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cfsenha.setGeometry(QtCore.QRect(270, 459, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_cfsenha.setFont(font)
        self.lineEdit_cfsenha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_cfsenha.setObjectName("lineEdit_cfsenha")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco Lucas Reis"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.pushButton_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.label_2.setText(_translate("MainWindow", "       Login:"))
        self.label_3.setText(_translate("MainWindow", "          CPF:"))
        self.label_5.setText(_translate("MainWindow", "Nome Completo:"))
        self.label_6.setText(_translate("MainWindow", "Senha:"))
        self.label_4.setText(_translate("MainWindow", "Confirmação de senha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
