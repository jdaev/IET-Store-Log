import os
import sqlite3
from datetime import date

from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QFormLayout,
                             QPushButton, QSpinBox, QVBoxLayout)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle


class Inventory(QDialog):
    db = QSqlDatabase.addDatabase("QSQLITE", "fourth")
    db.setDatabaseName("ProductDB.db")
    model = QSqlRelationalTableModel()

    def __init__(self):
        super(Inventory, self).__init__()
        self.file = ""
        self.data = []
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()

        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select * from productview')
        self.temp = c.fetchall()
        c.execute('Select sum(Stock_Price) from productview')
        self.grand_total = int(c.fetchone()[0])
        print(self.temp)
        for i in range(len(self.temp)):
            self.tabledata = [list(item) for item in self.temp]

    def filepick(self):
        filedial = QFileDialog()
        file = str(QFileDialog.getExistingDirectory(
            filedial, "Select Directory"))
        print(file)
        today = date.today()
        filename = 'Inventory on ' + today.strftime('%d-%m-%Y') + ' .pdf'
        self.filepath = os.path.join(file, filename)
        self.run()

    def run(self):
        doc = SimpleDocTemplate(
            self.filepath,
            rightMargin=72,
            leftMargin=72,
            topMargin=30,
            bottomMargin=72,
        )

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="LeftData",
                                  fontSize=11, alignment=TA_LEFT))
        styles.add(ParagraphStyle(name="RightData",
                                  fontSize=11, alignment=TA_RIGHT))
        styles.add(ParagraphStyle(name="CenterData",
                                  fontSize=11, alignment=TA_CENTER))

        self.data.append(Paragraph("CUIET STORE", styles['Title']))
        self.data.append(Paragraph("INVENTORY", styles['Title']))
       
        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))

        data = [['No.', 'Product\nName', 'Product\nType', 'Stock', 'Cost\nPrice',
                 'MRP', 'Price', 'Stock \n Price']] + self.tabledata
        t = Table(data)
        t.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
             ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
        self.data.append(t)

        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))

        exdata = []
        exdata += [('Stock Total Cost:', str(self.grand_total))]
        

        s = Table(exdata, hAlign='RIGHT')
        print(exdata)

        tstyle = [('ALIGN', (0, 0), (0, -1), "RIGHT"),
                  ('ALIGN', (1, 0), (1, -1), "LEFT"), ]

        s.setStyle(TableStyle(tstyle))
        self.data.append(s)

        doc.build(self.data)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    rep = Report()
    rep.filepick()
    sys.exit(rep.exec_())
