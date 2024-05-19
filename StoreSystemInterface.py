# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StoreSystemInterfacefqabII.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 600)
        self.centralwidget = QWidget(MainWindow.centralWidget())
        self.centralwidget.setObjectName(u"centralwidget")
        self.LoginStackeckedWidget = QStackedWidget(self.centralwidget)
        self.LoginStackeckedWidget.setObjectName(u"LoginStackeckedWidget")
        self.LoginStackeckedWidget.setGeometry(QRect(0, 0, 1131, 601))
        self.LoginStackeckedWidget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.label_30 = QLabel(self.LoginPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(380, 100, 621, 391))
        self.label_30.setStyleSheet(u"border-image: url(:/gif /gifsample.gif);\n"
"border-image: url(:/gifsample/gifsample.gif);\n"
"border-top-right-radius: 50px;\n"
"border-bottom-right-radius: 50px;")
        self.label_31 = QLabel(self.LoginPage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(380, 100, 621, 391))
        self.label_31.setStyleSheet(u"background-color:rgba(0, 0, 0, 80);\n"
"border-top-right-radius: 50px;\n"
"border-bottom-right-radius: 50px;")
        self.label_32 = QLabel(self.LoginPage)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(100, 100, 321, 391))
        self.label_32.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-top-left-radius: 50px;\n"
"border-bottom-left-radius: 50px;")
        self.lineEdit_2 = QLineEdit(self.LoginPage)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 280, 221, 40))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_33 = QLabel(self.LoginPage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(220, 160, 100, 40))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEdit = QLineEdit(self.LoginPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 230, 221, 40))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px")
        self.pushButton = QPushButton(self.LoginPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 370, 221, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.LoginStackeckedWidget.addWidget(self.LoginPage)
        self.MainWidget = QWidget()
        self.MainWidget.setObjectName(u"MainWidget")
        self.stackedWidget = QStackedWidget(self.MainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 90, 1131, 511))
        self.DashBoardPage = QWidget()
        self.DashBoardPage.setObjectName(u"DashBoardPage")
        self.frame = QFrame(self.DashBoardPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 80, 181, 91))
        self.frame.setStyleSheet(u"background-color: #F0F0F0")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 91, 16))
        self.TotalUnits = QLabel(self.frame)
        self.TotalUnits.setObjectName(u"TotalUnits")
        self.TotalUnits.setGeometry(QRect(30, 50, 47, 14))
        self.frame_2 = QFrame(self.DashBoardPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(260, 80, 161, 91))
        self.frame_2.setStyleSheet(u"background-color: #F0F0F0")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 91, 16))
        self.TotalTenants = QLabel(self.frame_2)
        self.TotalTenants.setObjectName(u"TotalTenants")
        self.TotalTenants.setGeometry(QRect(20, 50, 47, 14))
        self.frame_3 = QFrame(self.DashBoardPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(530, 80, 161, 91))
        self.frame_3.setStyleSheet(u"background-color: #F0F0F0")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 91, 16))
        self.AvailableUnits = QLabel(self.frame_3)
        self.AvailableUnits.setObjectName(u"AvailableUnits")
        self.AvailableUnits.setGeometry(QRect(10, 50, 47, 14))
        self.frame_4 = QFrame(self.DashBoardPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(870, 80, 161, 91))
        self.frame_4.setStyleSheet(u"background-color: #F0F0F0")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 91, 16))
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 40, 16, 21))
        self.TotalEarnings = QLabel(self.frame_4)
        self.TotalEarnings.setObjectName(u"TotalEarnings")
        self.TotalEarnings.setGeometry(QRect(50, 50, 47, 14))
        self.stackedWidget.addWidget(self.DashBoardPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.DashBoardFrame = QFrame(self.MainWidget)
        self.DashBoardFrame.setObjectName(u"DashBoardFrame")
        self.DashBoardFrame.setGeometry(QRect(0, 0, 1131, 81))
        self.DashBoardFrame.setFrameShape(QFrame.StyledPanel)
        self.DashBoardFrame.setFrameShadow(QFrame.Raised)
        self.DashBoardHolderFrame = QFrame(self.DashBoardFrame)
        self.DashBoardHolderFrame.setObjectName(u"DashBoardHolderFrame")
        self.DashBoardHolderFrame.setGeometry(QRect(0, 20, 1131, 41))
        self.DashBoardHolderFrame.setStyleSheet(u"background-color: #31302E")
        self.DashBoardHolderFrame.setFrameShape(QFrame.StyledPanel)
        self.DashBoardHolderFrame.setFrameShadow(QFrame.Raised)
        self.DashboardButton = QPushButton(self.DashBoardHolderFrame)
        self.DashboardButton.setObjectName(u"DashboardButton")
        self.DashboardButton.setGeometry(QRect(30, 10, 75, 23))
        self.DashboardButton.setStyleSheet(u"background-color: #F0F0F0")
        self.TenantsButton = QPushButton(self.DashBoardHolderFrame)
        self.TenantsButton.setObjectName(u"TenantsButton")
        self.TenantsButton.setGeometry(QRect(180, 10, 75, 23))
        self.UnitsButton = QPushButton(self.DashBoardHolderFrame)
        self.UnitsButton.setObjectName(u"UnitsButton")
        self.UnitsButton.setGeometry(QRect(270, 10, 75, 23))
        self.RentalsButton = QPushButton(self.DashBoardHolderFrame)
        self.RentalsButton.setObjectName(u"RentalsButton")
        self.RentalsButton.setGeometry(QRect(360, 10, 75, 23))
        self.PaymentsButton = QPushButton(self.DashBoardHolderFrame)
        self.PaymentsButton.setObjectName(u"PaymentsButton")
        self.PaymentsButton.setGeometry(QRect(450, 10, 75, 23))
        self.label = QLabel(self.DashBoardHolderFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(880, 10, 201, 20))
        self.label.setStyleSheet(u"color: #FFFFFF")
        self.LoginStackeckedWidget.addWidget(self.MainWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.LoginStackeckedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"L o g  I n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TOTAL UNITS", None))
        self.TotalUnits.setText(QCoreApplication.translate("MainWindow", u"76", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TOTAL TENANTS", None))
        self.TotalTenants.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AVAILABLE UNITS", None))
        self.AvailableUnits.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TOTAL EARNINGS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u20b1", None))
        self.TotalEarnings.setText(QCoreApplication.translate("MainWindow", u"50,000", None))
        self.DashboardButton.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.TenantsButton.setText(QCoreApplication.translate("MainWindow", u"TENANTS", None))
        self.UnitsButton.setText(QCoreApplication.translate("MainWindow", u"UNITS", None))
        self.RentalsButton.setText(QCoreApplication.translate("MainWindow", u"RENTALS", None))
        self.PaymentsButton.setText(QCoreApplication.translate("MainWindow", u"PAYMENTS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"STORE RENTAL MANAGEMENT SYSTEM", None))
    # retranslateUi

