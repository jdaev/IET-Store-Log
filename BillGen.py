import os
import sqlite3
from datetime import date,  datetime, time

from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QFormLayout,
                             QPushButton, QSpinBox, QVBoxLayout)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle


class Bill(QDialog):
    db = QSqlDatabase.addDatabase("QSQLITE", "fifth")
    db.setDatabaseName("ProductDB.db")
    model = QSqlRelationalTableModel()

    def __init__(self, c_name, c_type):
        super(Bill, self).__init__()
        self.date = date.today()
        self.time = datetime.now().time().strftime("%I:%M %p")
        self.cname = c_name
        self.buyer = c_type
        self.file = ""
        self.data = []
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()

        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select * from bill')
        self.bill_table = c.fetchall()
        c.execute('Select sum(Total) from bill')
        self.grand_total = int(c.fetchone()[0])
        print(self.bill_table)
        self.filepick()

    def filepick(self):
        filedial = QFileDialog()
        file = str(QFileDialog.getExistingDirectory(
            filedial, "Select Directory"))
        print(file)
        filename = str(self.cname) + ' Invoice.pdf'
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

        tbl_data = [
            [Paragraph("CUIET STORE", styles['LeftData']),
             Paragraph(str(self.date), styles["RightData"])],
            [Paragraph("INVOICE", styles["LeftData"]), Paragraph(
                str(self.time), styles["RightData"])],
            [Paragraph("", styles['LeftData'])],
            [Paragraph("", styles['LeftData'])],
            [Paragraph("Customer Name : " + self.cname,
                       styles["LeftData"])],
            [Paragraph("Customer Type : " +
                       self.buyer, styles["LeftData"])]
        ]
        tbl = Table(tbl_data)
        self.data.append(tbl)
        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))

        data = [['No.', 'Product\nName', 'Quantity',
                 'MRP',  'Total']] + self.bill_table
        data += [['', '', '', '', self.grand_total]]
        t = Table(data)
        t.setStyle(
            TableStyle([('LINEABOVE', (0, 0), (-1, 0), 1, colors.darkgray),
                        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.darkgray),
                        ('LINEABOVE', (0, -1), (-1, -1), 1, colors.darkgray),
                        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.darkgray)])
        )
        # t.setStyle(TableStyle(
        #   [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        #    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        #   ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        #   ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
        self.data.append(t)

        self.data.append(Paragraph("<br/>", styles['Title']))
        self.data.append(Paragraph("<br/>", styles['Title']))

        doc.build(self.data)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    rep = Bill()
    rep.show()
    sys.exit(rep.exec_())
