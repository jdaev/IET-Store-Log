from PyQt5.QtWidgets import (
    QApplication, QDialog, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, )
from PyQt5 import QtGui


class warning(QDialog):
    def __init__(self, isAbout, about):
        super(warning, self).__init__()
        main_layout = QVBoxLayout()
        self.text = QLabel(" Stock too low for purchase")

        main_layout.addWidget(self.text)
        sub_layout = QHBoxLayout()
        sub_layout.addStretch()
        if not isAbout:
            ok_button = QPushButton("OK")
            sub_layout.addWidget(ok_button)
            ok_button.clicked.connect(self.close)
        main_layout.addStretch()
        main_layout.addLayout(sub_layout)

        self.setLayout(main_layout)
        if isAbout:
            self.text.setText(about)
            self.setWindowTitle("About")
        else:
            self.setWindowTitle("WARNING")
        self.setWindowIcon(QtGui.QIcon('icon.png'))


if __name__ == '__main__':
    import sys

    APP = QApplication(sys.argv)
    warn = warning()
    warn.show()
    sys.exit(warn.exec_())
