# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import date, time, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSortFilterProxyModel

import Icons_rc
from dialog import warning
from DBeditor import TableEditor
from DBMan import DBMan
from BillGen import Bill
from InventoryGen import Inventory
from ReportGen import Report


class Ui_MainWindow(object):

    dbman = DBMan()
    dbman.load_tables()
    dbman.clear_undo()

    def setupUi(self, MainWindow):
        self.bill_bool = 2
        self.totalbill = 0
        self.item_price = 0
        self.stock_list = QtWidgets.QTextEdit()
        self.stock_list.setReadOnly(1)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quick_add_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.quick_add_box.sizePolicy().hasHeightForWidth())
        self.quick_add_box.setSizePolicy(sizePolicy)
        self.quick_add_box.setObjectName("quick_add_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.quick_add_box)
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.product_list = QtWidgets.QComboBox(self.quick_add_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.product_list.sizePolicy().hasHeightForWidth())
        self.product_list.setSizePolicy(sizePolicy)
        self.product_list.setObjectName("product_list")
        self.gridLayout.addWidget(self.product_list, 1, 0, 1, 1)
        self.product_label = QtWidgets.QLabel(self.quick_add_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.product_label.sizePolicy().hasHeightForWidth())
        self.product_label.setSizePolicy(sizePolicy)
        self.product_label.setObjectName("product_label")
        self.gridLayout.addWidget(self.product_label, 0, 0, 1, 1)
        self.buyer_list = QtWidgets.QComboBox(self.quick_add_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buyer_list.sizePolicy().hasHeightForWidth())
        self.buyer_list.setSizePolicy(sizePolicy)
        self.buyer_list.setObjectName("buyer_list")
        self.gridLayout.addWidget(self.buyer_list, 1, 1, 1, 1)
        self.buyer_label = QtWidgets.QLabel(self.quick_add_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buyer_label.sizePolicy().hasHeightForWidth())
        self.buyer_label.setSizePolicy(sizePolicy)
        self.buyer_label.setObjectName("buyer_label")
        self.gridLayout.addWidget(self.buyer_label, 0, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.quick_add_box)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 1, 3, 1, 1)
        self.quantity_number = QtWidgets.QSpinBox(self.quick_add_box)
        self.quantity_number.setObjectName("quantity_number")
        self.gridLayout.addWidget(self.quantity_number, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.quick_add_box)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.total_label = QtWidgets.QLabel(self.quick_add_box)
        self.total_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout_4.addWidget(self.total_label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.start_button = QtWidgets.QPushButton(self.quick_add_box)
        self.start_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/start/ic_play_arrow_black_18dp_2x.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.start_button.setIcon(icon)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_4.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.quick_add_box)
        self.stop_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/stop/ic_stop_black_18dp_2x.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon1)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_4.addWidget(self.stop_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.quick_add_box)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bill_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bill_box.sizePolicy().hasHeightForWidth())
        self.bill_box.setSizePolicy(sizePolicy)
        self.bill_box.setObjectName("bill_box")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.bill_box)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bill_name_label = QtWidgets.QLabel(self.bill_box)
        self.bill_name_label.setObjectName("bill_name_label")
        self.gridLayout_2.addWidget(self.bill_name_label, 0, 0, 1, 1)
        self.bill_product_list = QtWidgets.QComboBox(self.bill_box)
        self.bill_product_list.setObjectName("bill_product_list")
        self.gridLayout_2.addWidget(self.bill_product_list, 2, 1, 1, 1)
        self.bill_buyer_type_label = QtWidgets.QLabel(self.bill_box)
        self.bill_buyer_type_label.setObjectName("bill_buyer_type_label")
        self.gridLayout_2.addWidget(self.bill_buyer_type_label, 1, 0, 1, 1)
        self.bill_buyer_list = QtWidgets.QComboBox(self.bill_box)
        self.bill_buyer_list.setObjectName("bill_buyer_list")
        self.gridLayout_2.addWidget(self.bill_buyer_list, 1, 1, 1, 1)
        self.bill_product_label = QtWidgets.QLabel(self.bill_box)
        self.bill_product_label.setObjectName("bill_product_label")
        self.gridLayout_2.addWidget(self.bill_product_label, 2, 0, 1, 1)
        self.bill_name_line = QtWidgets.QLineEdit(self.bill_box)
        self.bill_name_line.setObjectName("bill_name_line")
        self.gridLayout_2.addWidget(self.bill_name_line, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bill_quantity_no = QtWidgets.QSpinBox(self.bill_box)
        self.bill_quantity_no.setObjectName("bill_quantity_no")
        self.horizontalLayout_2.addWidget(self.bill_quantity_no)
        self.bill_add_button = QtWidgets.QPushButton(self.bill_box)
        self.bill_add_button.setObjectName("bill_add_button")
        self.horizontalLayout_2.addWidget(self.bill_add_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.tableView = QtWidgets.QTableView(self.bill_box)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_7.addWidget(self.tableView)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.delete_button = QtWidgets.QPushButton(self.bill_box)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_6.addWidget(self.delete_button)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.bill_total_label = QtWidgets.QLabel(self.bill_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bill_total_label.sizePolicy().hasHeightForWidth())
        self.bill_total_label.setSizePolicy(sizePolicy)
        self.bill_total_label.setObjectName("bill_total_label")
        self.horizontalLayout_6.addWidget(self.bill_total_label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.print_check = QtWidgets.QCheckBox(self.bill_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.print_check.sizePolicy().hasHeightForWidth())
        self.print_check.setSizePolicy(sizePolicy)
        self.print_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.print_check.setObjectName("print_check")
        self.horizontalLayout_5.addWidget(self.print_check)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.submit_button = QtWidgets.QPushButton(self.bill_box)
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout_5.addWidget(self.submit_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addWidget(self.bill_box)
        self.stock_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stock_box.sizePolicy().hasHeightForWidth())
        self.stock_box.setSizePolicy(sizePolicy)
        self.stock_box.setObjectName("stock_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.stock_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addWidget(self.stock_box)
        self.stock_layout = QtWidgets.QHBoxLayout()
        self.verticalLayout_6.addWidget(self.stock_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuOptionis = QtWidgets.QMenu(self.menubar)
        self.menuOptionis.setObjectName("menuOptionis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionEdit_Products_Stock = QtWidgets.QAction(MainWindow)
        self.actionEdit_Products_Stock.setObjectName(
            "actionEdit_Products_Stock")
        self.actionEdit_Sales = QtWidgets.QAction(MainWindow)
        self.actionEdit_Sales.setObjectName("actionEdit_Sales")
        self.actionEdit_Buyer = QtWidgets.QAction(MainWindow)
        self.actionEdit_Buyer.setObjectName("actionEdit_Buyer")
        self.actionMonthly_Report = QtWidgets.QAction(MainWindow)
        self.actionMonthly_Report.setObjectName("actionMonthly_Report")
        self.actionWeekly_Report = QtWidgets.QAction(MainWindow)
        self.actionWeekly_Report.setObjectName("actionWeekly_Report")
        self.actionDaily_Report = QtWidgets.QAction(MainWindow)
        self.actionDaily_Report.setObjectName("actionDaily_Report")
        self.actionInventory = QtWidgets.QAction(MainWindow)
        self.actionInventory.setObjectName("actionInventory")
        self.actionClear_Old_Records = QtWidgets.QAction(MainWindow)
        self.actionClear_Old_Records.setObjectName("actionClear_Old_Records")
        # self.actionSettings = QtWidgets.QAction(MainWindow)
        # self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEdit_Products_Stock)

        self.menuEdit.addAction(self.actionEdit_Sales)
        self.menuEdit.addAction(self.actionEdit_Buyer)

        self.menuReports.addAction(self.actionMonthly_Report)

        self.menuReports.addAction(self.actionWeekly_Report)
        self.menuReports.addAction(self.actionDaily_Report)
        self.menuReports.addAction(self.actionInventory)
        self.menuOptionis.addAction(self.actionClear_Old_Records)
        # self.menuOptionis.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuOptionis.menuAction())
        self.product_list.setEditable(1)
        self.buyer_list.setEditable(1)
        self.bill_buyer_list.setEditable(1)
        self.bill_product_list.setEditable(1)

        self.dbman.products_model.select()
        self.proxy_product_model = QSortFilterProxyModel()
        self.proxy_product_model.setSourceModel(self.dbman.products_model)
        self.proxy_product_model.insertRow(0)
        self.proxy_product_model.setFilterKeyColumn(1)
        self.product_list.setModel(self.proxy_product_model)
        self.product_list.setModelColumn(
            self.proxy_product_model.filterKeyColumn())

        self.dbman.buyer_model.select()
        self.proxy_buyer_model = QSortFilterProxyModel()
        self.proxy_buyer_model.setSourceModel(self.dbman.buyer_model)
        self.proxy_buyer_model.insertRow(0)
        self.proxy_buyer_model.setFilterKeyColumn(0)
        self.buyer_list.setModel(self.proxy_buyer_model)
        self.buyer_list.setModelColumn(
            self.proxy_buyer_model.filterKeyColumn())

        self.bill_product_list.setModel(self.proxy_product_model)
        self.bill_product_list.setModelColumn(
            self.proxy_product_model.filterKeyColumn())

        self.bill_buyer_list.setModel(self.proxy_buyer_model)
        self.bill_buyer_list.setModelColumn(
            self.proxy_buyer_model.filterKeyColumn())
        self.bill_quantity_no.setValue(1)
        self.start_button.clicked.connect(self.bill_start)
        self.stop_button.clicked.connect(self.bill_stop)
        self.add_button.clicked.connect(self.tally)
        self.bill_add_button.clicked.connect(self.bill_item)
        self.product_list.currentIndexChanged.connect(self.reset_tally)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IET Store Log"))
        self.quick_add_box.setTitle(_translate("MainWindow", "Quick Add"))
        self.product_label.setText(_translate("MainWindow", "Product"))
        self.buyer_label.setText(_translate("MainWindow", "Customer  Type"))
        self.add_button.setText(_translate("MainWindow", "Submit"))
        self.total_label.setText(_translate("MainWindow", "Total : 0"))
        self.label_5.setText(_translate(
            "MainWindow", "<b> Last Added : None </b>"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.bill_box.setTitle(_translate("MainWindow", "Bill"))
        self.bill_name_label.setText(_translate("MainWindow", "Customer Name"))
        self.bill_buyer_type_label.setText(
            _translate("MainWindow", "Customer Type"))
        self.bill_product_label.setText(_translate("MainWindow", "Product"))
        self.bill_add_button.setText(_translate("MainWindow", "Add"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.bill_total_label.setText(_translate("MainWindow", "Total : 0"))
        self.print_check.setText(_translate("MainWindow", "Print"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.stock_box.setTitle(_translate("MainWindow", "Lowest Stock"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuReports.setTitle(_translate("MainWindow", "&Reports"))
        self.menuOptionis.setTitle(_translate("MainWindow", "Opt&ions"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionEdit_Products_Stock.setText(
            _translate("MainWindow", "Edit Products & Stock"))
        self.actionEdit_Sales.setText(_translate("MainWindow", "Edit Sales"))
        self.actionEdit_Buyer.setText(
            _translate("MainWindow", "Edit Customer Type"))
        self.actionMonthly_Report.setText(
            _translate("MainWindow", "Monthly Report"))
        self.actionWeekly_Report.setText(
            _translate("MainWindow", "Weekly Report"))
        self.actionDaily_Report.setText(
            _translate("MainWindow", "Daily Report"))
        self.actionInventory.setText(_translate("MainWindow", "Inventory"))
        self.actionClear_Old_Records.setText(
            _translate("MainWindow", "Clear Old Records"))
        # self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.triggered.connect(self.close_window)
        self.actionAbout.triggered.connect(self.about_dialog)
        self.actionUndo.triggered.connect(self.undo)
        self.actionEdit_Products_Stock.triggered.connect(
            self.dialog_edit_products)
        self.actionEdit_Sales.triggered.connect(self.dialog_edit_sales)
        self.actionEdit_Buyer.triggered.connect(self.dialog_edit_buyer)
        self.actionMonthly_Report.triggered.connect(self.gen_month_report)
        self.actionWeekly_Report.triggered.connect(self.gen_weekly_report)
        self.actionDaily_Report.triggered.connect(self.gen_daily_report)
        self.actionInventory.triggered.connect(self.inventory)
        self.actionClear_Old_Records.triggered.connect(self.cleaner)
        self.delete_button.clicked.connect(self.delete)
        self.submit_button.clicked.connect(self.billmaker)
        self.stock_list.setText(self.dbman.load_low_stock())

    def close_window(self):
        self.close()
        pass

    def bill_start(self):
        self.bill_bool = 0
        self.totalbill = 0
        self.total_label.setText("Total : " + str(self.totalbill))

    def bill(self):
        stock = int(self.dbman.return_stock(self.product_list.currentText()))
        price = int(self.dbman.return_price(self.product_list.currentText()))
        tally = int(self.quantity_number.value())
        if stock >= tally:
            if self.bill_bool == 0:
                self.totalbill = self.totalbill + (tally * price)
                print(self.totalbill)
                self.total_label.setText("Total : " + str(self.totalbill))

    def bill_stop(self):
        self.bill_bool = 1

    def reset_tally(self):
        self.quantity_number.setValue(1)

    def tally(self):
        if self.product_list.currentIndex() != 0:
            tally = self.quantity_number.value()
            pname = str(self.product_list.currentText())
            print(pname)
            self.buyer_type = str(self.buyer_list.currentText())
            sale = self.dbman.update_sales(pname, tally, self.buyer_type)
            self.bill()
            if sale:
                self.label_5.setText("<b>" + "Last Added : " + sale + "</b>")

    def dialog_edit_products(self):
        products_dialog = TableEditor('products')
        products_dialog.exec_()
        self.stock_list.setText(self.dbman.load_low_stock())
        self.dbman.products_model.select()

    def about_dialog(self):

        about = """
                <h2 style="text-align: center;">Created By,</h2>
                <h4 style="text-align: center;">Javed Hussain</h4>
                <h4 style="text-align: center;">Neethu KT</h4>
                <h4 style="text-align: center;">Shahma P</h4>
                <h4 style="text-align: center;">Anu Krishna</h4>
                <h3 style="text-align: center;">&nbsp;</h3>
                <h3 style="text-align: center;">IT 2015 - 2019</h3>
                <h3 style="text-align: center;"><a href="https://github.com/trailblazer42">Github</a></h3>
                """
        dial = warning(1, about)
        dial.exec_()

    def dialog_edit_sales(self):
        sales_dialog = TableEditor('salesview')
        sales_dialog.exec_()

    def dialog_edit_buyer(self):
        sales_dialog = TableEditor('buyer_type')
        sales_dialog.exec_()

    def gen_month_report(self):
        sdate = date.today().replace(day=1)
        edate = date.today()
        rep_dialog = Report(sdate, edate)
        rep_dialog.exec_()

    def gen_weekly_report(self):
        edate = date.today()
        sdate = edate - timedelta(7)
        rep_dialog = Report(sdate, edate)
        rep_dialog.exec_()

    def gen_daily_report(self):
        edate = date.today()
        rep_dialog = Report(edate, edate)
        rep_dialog.exec_()

    def cleaner(self):
        self.dbman.clean()

    def undo(self):
        self.dbman.undo_sale()

    def inventory(self):
        inv = Inventory()
        inv.filepick()

    def billmaker(self):
        cname = self.bill_name_line.text()
        buyer = self.bill_buyer_list.currentText()
        to_print = self.print_check.isChecked()
        if to_print:
            bill_generate = Bill(cname, buyer)
            self.dbman.update_bill_sales(buyer)
            self.dbman.bill_model.select()

        else:
            self.dbman.update_bill_sales(buyer)
            self.dbman.bill_model.select()
        self.bill_product_list.setCurrentIndex(-1)
        self.label_5.setText("<b>" + "Last Added: Bill for " + cname + "</b>")
        self.bill_name_line.clear()

    def bill_item(self):
        self.tableView.setModel(self.dbman.bill_model)
        self.tableView.setColumnHidden(0, True)
        pname = self.bill_product_list.currentText()
        buyer = self.bill_buyer_list.currentText()
        quantity = self.bill_quantity_no.value()
        total = self.dbman.update_bill(pname, quantity, buyer)
        self.bill_total_label.setText("Total : " + str(total))
        self.dbman.bill_model.select()

    def delete(self):
        self.rowindexes = self.tableView.selectionModel().selectedRows(0)
        for rindex in (self.rowindexes):
            row = (rindex.data())
            self.dbman.bill_delete(row)
            self.dbman.bill_model.select()


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())
