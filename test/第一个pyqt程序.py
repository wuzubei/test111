import sys

from PyQt6.QtWidgets import (
    QApplication, QDialog, QPushButton, QHBoxLayout, QMessageBox
)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    window.setWindowTitle('Tip')
    window.resize(400, 300)


    def show_msg():
        QMessageBox.information(window, '信息提示', '你点击了我')


    # 布局
    hbox = QHBoxLayout()
    # 按钮
    button = QPushButton('点击我')
    button.clicked.connect(show_msg)
    # 布局里添加按钮
    hbox.addWidget(button)
    # 窗口中添加布局组件
    window.setLayout(hbox)
    # 显示 窗口
    window.show()
    # 窗口停止事件
    sys.exit(app.exec())
