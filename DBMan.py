import sqlite3
from datetime import date, timedelta, datetime

from PyQt5.QtSql import (QSqlDatabase, QSqlRelationalTableModel)

from dialog import warning


class DBMan(object):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("ProductDB.db")

    def __init__(self):
        super(DBMan, self).__init__()

        self.products_model = QSqlRelationalTableModel()
        self.buyer_model = QSqlRelationalTableModel()
        self.sales_model = QSqlRelationalTableModel()
        self.bill_model = QSqlRelationalTableModel()
        self.check_stock = 0
        self.last_added = " "

    def load_tables(self):
        self.products_model.setTable("products")
        self.buyer_model.setTable("buyer_type")
        self.sales_model.setTable("sales")
        self.bill_model.setTable("bill")
        self.bill_model.setEditStrategy(
            QSqlRelationalTableModel.OnManualSubmit)

    def update_sales(self, pname, count, buyer_type):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select ID from products where Name = ?', [pname])
        pid = int(c.fetchone()[0])
        print(pid)
        sdate = str(date.today())
        stime = str(datetime.now().time())
        print(stime)
        c.execute('Insert into purchase_log values(?,?,?,?)',
                  (stime, pid, count, buyer_type,))
        c.execute('Select * from sales where Id = ? and Sale_Date = ?  and Buyer = ?',
                  (pid, sdate, buyer_type,))
        check_id_date_buyer = c.fetchone()
        c.execute(
            'Select * from sales where Id = ? and Sale_Date = ? ', (pid, sdate,))
        check_id_date = c.fetchone()
        c.execute('Select * from sales where Id = ? and Sale_Date = ?  and Buyer = ?',
                  (pid, sdate, buyer_type,))
        check_buyer = c.fetchone()
        c.execute('Select Price from products where ID=?', (pid,))
        price = int(c.fetchone()[0])
        total = count * price
        c.execute('Select Stock from products where ID=?', (pid,))
        check_stock = int(c.fetchone()[0])
        self.last_added = pname + ' x' + str(count)
        if check_stock == 0 | check_stock < count:
            self.warner()
            return None
        else:
            if check_id_date_buyer is not None:
                c.execute(
                    "Update sales Set Quantity = Quantity + ? , Total_Price = Total_Price + ? where Id= ? and Sale_Date= ? and Buyer= ?", (count, total, pid, sdate, buyer_type))
                c.execute(
                    "Update products Set Stock = Stock - ? Where ID=?", (count, pid,))
                conn.commit()
            else:
                c.execute('Insert into sales values(?,?,?,?,?)',
                          (sdate, pid, count, total, buyer_type,))
                c.execute(
                    "Update products Set Stock = Stock - ? Where ID=?", (count, pid,))
                conn.commit()
        return self.last_added

    def undo_sale(self):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select * from purchase_log')
        check_empty = c.fetchall()
        print(check_empty)
        if not check_empty:
            return
        c.execute(
            "Select Id from purchase_log where Time = (Select max(Time) from purchase_log)")
        pid = int(c.fetchone()[0])
        print(pid)

        c.execute(
            "Select Count from purchase_log where Time = (Select max(Time) from purchase_log)")
        count = int(c.fetchone()[0])
        c.execute(
            "Select Buyer from purchase_log where Time = (Select max(Time) from purchase_log)")
        buyer_type = str(c.fetchone()[0])
        sdate = str(date.today())
        c.execute('Select Price from products where ID=?', (pid,))
        price = int(c.fetchone()[0])
        total = count * price

        c.execute(
            "Update sales Set Quantity = Quantity - ? , Total_Price = Total_Price - ? where Id= ? and Sale_Date= ? and Buyer= ?", (
                count, total, pid, sdate, buyer_type)
        )
        c.execute(
            "Update products Set Stock = Stock + ? Where ID=?", (count, pid,)
        )
        c.execute(
            "Select Quantity from sales where Id= ? and Sale_Date= ? and Buyer= ?", (
                pid, sdate, buyer_type)
        )
        check_quantity = int(c.fetchone()[0])
        if check_quantity is 0:
            c.execute("Delete from sales where Id= ? and Sale_Date= ? and Buyer= ?",
                      (pid, sdate, buyer_type))

        c.execute(
            "Delete from purchase_log where Time = (Select max(Time) from purchase_log)"
        )
        conn.commit()

    def warner(self):
        warn = warning(0, " ")
        warn.exec_()

    def clear_undo(self):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select * from purchase_log')
        check_empty = c.fetchall()
        print(check_empty)
        #if not check_empty:
            #return
        c.execute('Delete from purchase_log where Time not in (Select Time from purchase_log order by Time desc LIMIT 10)'
                  )
        conn.commit()

    def return_stock(self, pname):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select ID from products where Name = ?', [pname])
        pid = int(c.fetchone()[0])       
        c.execute('Select Stock from products where ID=?', (pid,))
        stock = c.fetchone()[0]
        return stock

    def return_price(self, pname):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select ID from products where Name = ?', [pname])
        pid = int(c.fetchone()[0])
        c.execute('Select Price from products where ID=?', (pid,))
        price = c.fetchone()[0]
        return price

    def clean(self):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        today = date.today()
        lastmonth = today - timedelta(30)
        c.execute('Delete from sales where Sale_Date<?', (lastmonth,))
        conn.commit()

    def update_bill(self, name, count, buyer_type):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select ID from products where Name = ?', [name])
        pid = int(c.fetchone()[0])
        c.execute('Select * from bill where Name = ?', (name,))
        check_item = c.fetchone()
        c.execute("Select max(No) from bill")
        max_no = c.fetchone()[0]
        if max_no == None:
            max_no = 0
        else:
            max_no = int(max_no)
        c.execute('Select Price from products where ID=?', (pid,))
        price = int(c.fetchone()[0])
        total = count * price
        c.execute('Select Stock from products where ID=?', (pid,))
        check_stock = int(c.fetchone()[0])
        if check_stock == 0 | check_stock < count:
            self.warner()
        else:
            if check_item is not None:
                c.execute(
                    "Update bill Set Quantity = Quantity + ? , Total = Total + ? where Name = ?", (count, total, name))
                conn.commit()
                c.execute(
                    "Update products Set Stock = Stock - ? Where ID=?", (count, pid,))
                conn.commit()
                self.bill_model.select()
            else:
                c.execute('Insert into bill values(?,?,?,?,?)',
                          (max_no+1, name, count, price, total,))
                c.execute(
                    "Update products Set Stock = Stock - ? Where ID=?", (count, pid,))
                conn.commit()
                self.bill_model.select()
        c.execute('Select sum(Total) from bill')
        bill_total = c.fetchone()[0]
        if bill_total:
            return int(bill_total)
        else:
            return 0

    def bill_delete(self, row):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Delete from bill where No = ?',
                  (row, ))
        conn.commit()
        pass

    def update_bill_sales(self, buyer):

        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select * from bill')
        bill_data = c.fetchall()
        for i in range(len(bill_data)):
            bill_list = [list(item) for item in bill_data]
        for bill_row in bill_list:
            pname = bill_row[1]
            quantity = bill_row[2]
            self.update_sales(pname, quantity, buyer)
        c.execute('Delete from bill')
        conn.commit()

    def load_low_stock(self):
        conn = sqlite3.connect('ProductDB.db')
        c = conn.cursor()
        c.execute('Select Stock,Name from products ORDER BY STOCK  limit 50')
        low_list = c.fetchall()
        stock_list = ""
        for row in low_list:
            print(row)
            stock_list += str(row[0])
            stock_list += "x "
            stock_list += str(row[1])
            stock_list += "\n"
        return stock_list


if __name__ == '__main__':
    pdb = DBMan()
