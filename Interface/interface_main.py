# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(636, 366)
        Dialog.setMinimumSize(QSize(636, 366))
        Dialog.setMaximumSize(QSize(636, 366))
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:rgb(54, 57, 63);\n"
"}\n"
"\"rgb(142, 146, 151)  text\"\n"
"\"rgb(47, 49, 54) back\"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QTabWidget\n"
" {\n"
"     border-top: 1px solid gray;\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(77, 80, 102);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(165, 166, 182);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	heig"
                        "ht: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"	\n"
"QPushButton:hover{\n"
"	background-color: rgb(115, 114, 145);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(165, 166, 182);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 871, 411))
        self.tabWidget.setMinimumSize(QSize(871, 411))
        self.tabWidget.setMaximumSize(QSize(871, 411))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
" {\n"
"     border-top: rgb(47, 49, 54);\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
" }\n"
"\n"
" QTabBar::tab\n"
" {\n"
"\n"
"	float: right;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(89, 94, 104);\n"
"	border-bottom: rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"     min-width: 320px;\n"
"     padding-top : 6px;\n"
"     padding-bottom : 8px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"	color: rgb(170, 176, 186);\n"
"\n"
"\n"
" }\n"
"\n"
"QListWidget{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(104, 110, 121);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
" QTabBar::tab:selected, QTa"
                        "bBar::tab:hover \n"
"{\n"
"     background-color: rgb(77, 80, 102);\n"
" }\n"
"\n"
"QPushButton{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(89, 94, 104);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"	color: rgb(170, 176, 186);\n"
"\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(104, 110, 121);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"	\n"
"QPushButton:hover{\n"
"	background-color: rgb(77, 80, 102);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: silver;\n"
"}\n"
""
                        "\n"
"QLabel{\n"
"	color:rgb(170, 176, 186);\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(104, 110, 121);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(460, 10, 160, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 10, 421, 251))
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 260, 160, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(420, -80, 191, 521))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 50, 391, 21))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 161, 16))
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(280, 80, 121, 23))
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 130, 391, 21))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 161, 16))
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(280, 160, 121, 23))
        self.horizontalLayoutWidget_2 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 260, 160, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"0.0.5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"ID \u0444\u0430\u0439\u043b\u0430 \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0435", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ID \u0432\u0435\u0440\u0441\u0438\u044f \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0435", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"0.0.5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

