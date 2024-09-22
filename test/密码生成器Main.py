import string
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from 密码生成器 import Ui_PasswordGenerate
import sys

class MyPwdSC(Ui_PasswordGenerate, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn_newPwd.clicked.connect(self.new_pwd)

    def new_pwd(self):
        words = (
            string.digits
            + string.ascii_uppercase
            + string.ascii_lowercase
            + string.punctuation
        )
        words = random.sample(list(words),20)
        pwd="".join(words)
        self.lineEdit.setText(pwd)
        QMessageBox.information(self,'信息提示','密码生成成功')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myPwdSC = MyPwdSC()


    sys.exit(app.exec())
