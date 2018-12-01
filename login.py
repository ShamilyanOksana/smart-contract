# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import main
import Estate
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(232, 358)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.login_line_edit = QtWidgets.QLineEdit(Dialog)
        self.login_line_edit.setMaxLength(42)
        self.login_line_edit.setObjectName("login_line_edit")
        self.verticalLayout_2.addWidget(self.login_line_edit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.password_line_edit = QtWidgets.QLineEdit(Dialog)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.verticalLayout.addWidget(self.password_line_edit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Login = QtWidgets.QPushButton(Dialog)
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# Мой Код Начинается отстюда

        self.Login.clicked.connect(self.open_main_window) #вызываем Авторизацию
        self.pushButton.clicked.connect(quit)
        self.Error_Msg = QMessageBox()

        self.Estate_object = Estate.Estate() # класс для работы с web3
        self.Temp_login =0
        self.Temp_pass = 0
        self.pass_file = open("pass.txt","w")
        self.login_file = open("login.txt","w")

    def open_main_window(self):
        self.Temp_login = self.login_line_edit.text()
        self.Temp_pass = self.password_line_edit.text()
        print(self.Temp_login)

        State =  self.Estate_object.auth(self.Temp_login,self.Temp_pass)
        print(self.Estate_object.passfrase, self.Estate_object.user_address)
        if State == True:
            self.pass_file.writelines(self.Temp_pass)
            self.login_file.writelines(self.Temp_login)

            self.pass_file.close()
            self.login_file.close()
            self.Mainw_window = QtWidgets.QDialog()
            self.ui = main.Ui_Dialog()
            self.ui.setupUi(self.Mainw_window)
            self.Mainw_window.show()
        else:
            #print("error") Debug
            self.Error_Msg.setIcon(QMessageBox.Information)
            self.Error_Msg.setText("Ошибка не верно введен логин или пароль")
            self.Error_Msg.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.label_2.setText(_translate("Dialog", "Логин:"))
        self.label.setText(_translate("Dialog", "Пароль:"))
        self.pushButton.setText(_translate("Dialog", "Выход"))
        self.Login.setText(_translate("Dialog", "Войти"))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

