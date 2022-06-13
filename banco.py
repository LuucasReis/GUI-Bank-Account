from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
from designb import *
from designc import *
from designprof import Ui_MainWindow3
from validarcpf import validarcpf1
from designd import Ui_MainWindow4

class JanelaLogin(QMainWindow,Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)
        self.__cadastro= []
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.checkBox.stateChanged.connect(lambda:self.checked())
        self.pushButton_cadastrar.clicked.connect(self.pag2)
        self.pushButton_entrar.clicked.connect(self.entrar)
        
    @property
    def cadastro(self):
        return self.__cadastro

    def checked(self):
        if self.checkBox.isChecked():
            self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Normal)
        
        else:
            self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def pag2(self):
        self.segunda_tela= Cadastro()
        self.segunda_tela.show()
        self.lineEdit_login.setText("")
        self.lineEdit_senha.setText("")
        self.label_7.setText("")     
    
    def entrar(self):
        login= self.lineEdit_login.text()
        senha= self.lineEdit_senha.text()

        if cadastro == []:
            self.label_7.setText("                 VOCÊ NÃO POSSUI UM LOGIN")
        
        for dados in self.cadastro:
            if login == dados[0] and senha == dados[3]:
                self.close()
                global terceira_tela
                terceira_tela= ContaBanco(dados[2])
                terceira_tela.show()

            else:
                self.label_7.setText("LOGIN OU SENHA INCORRETOS, TENTE NOVAMENTE!")


class Cadastro(QMainWindow,Ui_MainWindow2):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.lineEdit_senhac.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_cfsenha.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pushButton_cadastro.clicked.connect(self.Cadastrar)
        self.pushButton_voltar.clicked.connect(self.voltar)

    def Cadastrar(self):
        self.login= self.lineEdit_login.text()
        self.cpf= self.lineEdit_cpf.text()
        self.nome_completo= self.lineEdit_nome.text()
        self.senha= self.lineEdit_senhac.text()
        self.cfsenha= self.lineEdit_cfsenha.text()
        cf_cpf= validarcpf1(self.cpf)
        if not cf_cpf :
            return self.label_errocadastro.setText("*CPF INVÁLIDO") 
        else:
            if self.senha == self.cfsenha: 
                primeira_tela.cadastro.append((self.login, self.cpf, self.nome_completo, self.senha))
                self.close()
            
            else:
                return self.label_errocadastro.setText("**SENHA DIFERENTE DA CONFIMAÇÃO")
        
    def voltar(self):
        self.close()  


class ContaBanco(QMainWindow, Ui_MainWindow3):
    def __init__(self,nome, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton_foto.clicked.connect(self.alterar_img)
        self.label_welcome.setText(f"Bem vindo, {nome}!")
        self.valorc= 0.0
        self.label_saldo.setText(f"Saldo: R$ {self.valorc}")
        self.label_ts.setText("Nenhuma transação executada.")
        self.pushButton_depositar.clicked.connect(self.transacoes)
        self.pushButton_sair.clicked.connect(self.deslogar)


    def alterar_img(self):
        self.imagem,_ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "Escolher imagem",
            r'C:\Users\lukes\Pictures',
        )

        self.img = QPixmap(self.imagem)
        self.img = self.img.scaledToHeight(self.label_img.height())

        self.label_img.setPixmap(self.img)
        
    def transacoes(self):
        self.t3= PagTs()
        self.t3.show()
    
    def deslogar(self):
        self.close()
        primeira_tela.lineEdit_login.setText("")
        primeira_tela.lineEdit_senha.setText("")
        primeira_tela.label_7.setText("")
        primeira_tela.show()
    

class PagTs(QMainWindow,Ui_MainWindow4):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.lineEdit_dsenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.checkBox.stateChanged.connect(lambda:self.checar())
        self.valord= 0
        self.pushButton_conf.clicked.connect(self.depositar)
        self.pushButton.clicked.connect(self.sacar)

    def checar(self):
        if self.checkBox.isChecked():
            self.lineEdit_dsenha.setEchoMode(QtWidgets.QLineEdit.Normal)
        
        else:
            self.lineEdit_dsenha.setEchoMode(QtWidgets.QLineEdit.Password)

    def depositar(self):
        self.senha= self.lineEdit_dsenha.text()
        for v in primeira_tela.cadastro:
            if self.senha == v[3]:
                self.valord = float(self.lineEdit_valor.text())
                terceira_tela.valorc += self.valord
                terceira_tela.label_saldo.setText(f"Saldo: R${terceira_tela.valorc:.2f}")
                terceira_tela.label_ts.setText(f"   Despósito de R${self.valord}")
                self.close()
        
            else:
                return self.label_erro.setText("Senha incorreta")
                
    def sacar(self):
        self.senha= self.lineEdit_dsenha.text()
        self.valor_s = float(self.lineEdit_valor.text())
        for v in primeira_tela.cadastro:
            if self.senha == v[3] and self.valor_s <= terceira_tela.valorc:
                terceira_tela.valorc -= self.valor_s
                terceira_tela.label_saldo.setText(f"Saldo: R${terceira_tela.valorc:.2f}")
                terceira_tela.label_ts.setText(f"   Saque de R${self.valor_s}")
                self.close()
        
            elif self.senha != v[3]:
                return self.label_erro.setText("Senha incorreta.")
            
            elif self.valor_s > terceira_tela.valorc:
                return self.label_erro.setText("Valor insuficiente.")


if __name__=="__main__":
    cadastro= []
    qt= QApplication(sys.argv)
    primeira_tela= JanelaLogin()
    
    primeira_tela.show()
    qt.exec_()