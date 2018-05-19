from PyQt5.QtWidgets import (
    QApplication, QFormLayout, QDoubleSpinBox, QLineEdit, QSpinBox, QDialog, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, )
from PyQt5 import QtGui
import sqlite3


class adder(QDialog):
    def __init__(self):
        super(adder, self).__init__()
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_submit = QPushButton("Add")
        self.name_line = QLineEdit()
        self.type_line = QLineEdit()
        self.stock_line = QSpinBox()
        self.stock_line.setMaximum(999999999)
        self.cost_line = QDoubleSpinBox()
        self.cost_line.setMaximum(9999999999)
        self.mrp_line = QDoubleSpinBox()
        self.mrp_line.setMaximum(9999999999)
        self.price_line = QDoubleSpinBox()
        self.price_line.setMaximum(999999999)
        form_layout.addRow("Product Name ", self.name_line)
        form_layout.addRow("Product Type ", self.type_line)
        form_layout.addRow("Stock", self.stock_line)
        form_layout.addRow("Cost Price", self.cost_line)
        form_layout.addRow("MRP", self.mrp_line)
        form_layout.addRow("Unit Price", self.price_line)
        form_layout.addRow(form_submit)
        main_layout.addLayout(form_layout)
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setLayout(main_layout)
        form_submit.clicked.connect(self.add_product)

    def add_product(self):
        name = self.name_line.text()
        type = self.type_line.text()
        stock = self.stock_line.value()
        cost = self.cost_line.value()
        mrp = self.mrp_line.value()
        price = self.price_line.value()
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select max(ID) from products')
        pidt = c.fetchone()[0]
        if pidt:
            pid = int(pidt) + 1
        else:
            pid = 1
        c.execute(
            'Insert into products(ID,Name,Type,Stock,Cost_Price,MRP,Price) '
            'values(?,?,?,?,?,?,?)', (pid, name, type, stock, cost, mrp, price)
        )
        conn.commit()
        self.close()


if __name__ == '__main__':
    import sys

    APP = QApplication(sys.argv)
    add = adder()
    add.show()
    sys.exit(add.exec_())
