import sqlite3

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QDialog,
                             QDialogButtonBox, QHBoxLayout, QInputDialog,
                             QLineEdit, QMessageBox, QPushButton, QTableView)

from addItemDialog import adder


class TableEditor(QDialog):
    def __init__(self, tableName):
        super(TableEditor, self).__init__()

        db = QSqlDatabase.addDatabase("QSQLITE", "second")
        db.setDatabaseName('ProductDB.db')

        self.model = QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.view = QTableView()
        self.view.setSizeAdjustPolicy(2)
        self.view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view.resizeColumnsToContents()
        self.view.setModel(self.model)
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)

        submit_button = QPushButton("Submit")
        submit_button.setDefault(True)
        add_button = QPushButton("Add")
        delete_button = QPushButton('Delete')
        quit_button = QPushButton("Quit")
        revert = QPushButton('Revert')

        buttonBox = QDialogButtonBox(Qt.Vertical)

        if tableName == 'products':
            self.view.setColumnHidden(0, 1)
            buttonBox.addButton(submit_button, QDialogButtonBox.ActionRole)
            buttonBox.addButton(add_button, QDialogButtonBox.ActionRole)
            buttonBox.addButton(delete_button, QDialogButtonBox.ActionRole)
        elif tableName == 'salesview':
            buttonBox.addButton(revert, QDialogButtonBox.ActionRole)
        elif tableName == 'buyer_type':
            buttonBox.addButton(add_button, QDialogButtonBox.ActionRole)
            buttonBox.addButton(delete_button, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quit_button, QDialogButtonBox.RejectRole)

        submit_button.clicked.connect(self.submit)
        if tableName == 'products':
            add_button.clicked.connect(self.add)
            delete_button.clicked.connect(self.remove)
        elif tableName == 'buyer_type':
            add_button.clicked.connect(self.add_buyer)
            delete_button.clicked.connect(self.remove_buyer)

        revert.clicked.connect(self.revert)
        quit_button.clicked.connect(self.close)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        if tableName == 'products':
            self.setWindowTitle("Products & Stock")
        elif tableName == 'buyer_type':
            self.setWindowTitle("Customer Types")
        else:
            self.setWindowTitle("Sales")

    def add(self):
        add = adder()
        add.exec_()
        self.model.select()

    def add_buyer(self):
        text, ok = QInputDialog.getText(self, 'New Buyer',
                                        'Enter customer type:')

        if ok:
            conn = sqlite3.connect('ProductDB.db')
            c = conn.cursor()
            c.execute(
                'Insert into buyer_type(Buyer) values(?)', (text,))
            conn.commit()
            self.model.select()

    def remove(self):
        item = 0
        self.itemindexes = self.view.selectionModel().selectedRows(0)
        for tindex in (self.itemindexes):
            item = (tindex.data())
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        if item:
            c.execute('Delete from products where ID = ?', (item, ))
            c.execute('Delete from purchase_log where Id =  ?', (item, ))
            conn.commit()
        self.model.select()

    def remove_buyer(self):
        self.dateindexes = self.view.selectionModel().selectedRows(0)
        for dindex in (self.dateindexes):
            buyer = (dindex.data())
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Delete from buyer_type where Buyer =  ?',
                  (buyer, ))
        conn.commit()
        self.model.select()

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QMessageBox.warning(self, "Products & Stock",
                                "The database reported an error: %s"
                                % self.model.lastError().text())

    def revert(self):
        self.dateindexes = self.view.selectionModel().selectedRows(0)
        self.itemindexes = self.view.selectionModel().selectedRows(1)
        self.quantityindexes = self.view.selectionModel().selectedRows(3)
        self.buyerindexes = self.view.selectionModel().selectedRows(5)
        for dindex in (self.dateindexes):
            for tindex in (self.itemindexes):
                for qindex in (self.quantityindexes):
                    for rindex in (self.buyerindexes):
                        buyer = (rindex.data())
                        quantity = (qindex.data())
                        date = (dindex.data())
                        item = (tindex.data())
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Delete from sales '
                  'where Sale_Date = ? and Id = ? and Buyer =  ?',
                  (date, item, buyer, ))
        c.execute("Update products Set Stock = Stock + ? Where ID=?",
                  (quantity, item,))
        conn.commit()
        self.model.select()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    editor = TableEditor('products')
    editor.show()
    sys.exit(editor.exec_())
