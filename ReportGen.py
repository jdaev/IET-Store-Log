import os
import sqlite3
from datetime import date

from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QFormLayout,
                             QPushButton, QSpinBox, QVBoxLayout)
from PyQt5 import QtGui                             
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle


class Report(QDialog):
    db = QSqlDatabase.addDatabase("QSQLITE", "third")
    db.setDatabaseName("ProductDB.db")
    model = QSqlRelationalTableModel()

    def __init__(self, start_date, end_date):
        super(Report, self).__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.file = ""
        self.data = []
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()

        main_layout = QVBoxLayout()
        form = QFormLayout()
        self.extra = QSpinBox()
        self.extra.setMinimumWidth(250)
        self.sal = QSpinBox()
        self.extra.setMaximum(99999999)
        self.sal.setMaximum(999999999)
        close = QPushButton("Quit")
        rep_b = QPushButton("Generate Report")
        form.addRow("Extra Expenses:", self.extra)
        form.addRow("Employee Salary", self.sal)
        main_layout.addLayout(form)
        main_layout.addWidget(rep_b)
        main_layout.addWidget(close)
        close.clicked.connect(self.close)
        rep_b.clicked.connect(self.filepick)
        self.setLayout(main_layout)
        self.setWindowTitle("Reports")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select products.ID,Name,Type ,Sum(Quantity), Cost_Price, '
                  'Price,Buyer, Total_Price from products '
                  'inner join sales on products.ID=sales.Id '
                  'where sales.Sale_Date between ? and ? '
                  'group by products.ID,Buyer order by products.ID',
                  (str(start_date), str(end_date)))
        self.temp = c.fetchall()
        c.execute('Select sum(Total_Price) from sales '
                  'where sales.Sale_Date between ? and ?',
                  (str(start_date), str(end_date)))
        self.grand_total = int(c.fetchone()[0])
        print(self.temp)
        for i in range(len(self.temp)):
            self.tabledata = [list(item) for item in self.temp]

        for i in range(len(self.tabledata)):
            self.tabledata[i][0] = i + 1
            print(self.tabledata[i])

    def filepick(self):
        filedial = QFileDialog()
        file = str(QFileDialog.getExistingDirectory(
            filedial, "Select Directory"))
        print(file)
        today = date.today()
        filename = 'Report' + today.strftime('%d-%m-%Y') + ' .pdf'
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
        self.data.append(Paragraph("SALES REPORT", styles['Title']))
        if self.start_date == self.end_date:
            self.data.append(Paragraph(str(self.start_date), styles['Title']))
        else:
            self.data.append(Paragraph(str(self.start_date) +
                             " - " + str(self.end_date), styles['Title']))

        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))

        data = [['No.', 'Product\nName', 'Product\nType',
                 'Quantity\nSold', 'Cost\nPrice',
                 'Unit\nPrice', 'Buyer', 'Total\nPrice']] + self.tabledata
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
        exdata += [('Sales Total :', str(self.grand_total))]
        if self.extra.value() != 0:
            exdata += [('Extra Expenses :', str(self.extra.value()))]
        if self.sal.value() != 0:
            exdata += [('Employee Salary :', str(self.sal.value()))]
        gtotal = self.grand_total - (self.extra.value() + self.sal.value())
        if gtotal != self.grand_total:
            exdata += [('Grand Total :', str(gtotal))]

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
    rep.show()
    sys.exit(rep.exec_())
