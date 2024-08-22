# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CSVDeal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(483, 350)
        self.actSelect = QAction(Form)
        self.actSelect.setObjectName(u"actSelect")
        icon = QIcon()
        icon.addFile(u":/icons/icons/open1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actSelect.setIcon(icon)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editDir = QLineEdit(self.groupBox)
        self.editDir.setObjectName(u"editDir")

        self.gridLayout.addWidget(self.editDir, 0, 0, 1, 1)

        self.tbtnSelect = QToolButton(self.groupBox)
        self.tbtnSelect.setObjectName(u"tbtnSelect")

        self.gridLayout.addWidget(self.tbtnSelect, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rbtnCSV2MAP = QRadioButton(self.groupBox_2)
        self.rbtnCSV2MAP.setObjectName(u"rbtnCSV2MAP")

        self.gridLayout_2.addWidget(self.rbtnCSV2MAP, 0, 0, 1, 1)

        self.rbtnMAP2TXT = QRadioButton(self.groupBox_2)
        self.rbtnMAP2TXT.setObjectName(u"rbtnMAP2TXT")

        self.gridLayout_2.addWidget(self.rbtnMAP2TXT, 0, 1, 1, 1)

        self.rbtnCSV2TIME = QRadioButton(self.groupBox_2)
        self.rbtnCSV2TIME.setObjectName(u"rbtnCSV2TIME")

        self.gridLayout_2.addWidget(self.rbtnCSV2TIME, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(13, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbtnDo = QToolButton(Form)
        self.tbtnDo.setObjectName(u"tbtnDo")

        self.horizontalLayout.addWidget(self.tbtnDo)

        self.tbtnClose = QToolButton(Form)
        self.tbtnClose.setObjectName(u"tbtnClose")

        self.horizontalLayout.addWidget(self.tbtnClose)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(13, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.pBar = QProgressBar(Form)
        self.pBar.setObjectName(u"pBar")
        self.pBar.setValue(0)
        self.pBar.setTextVisible(False)

        self.gridLayout_3.addWidget(self.pBar, 5, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.actSelect.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actSelect.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actSelect.setShortcut(QCoreApplication.translate("Form", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u76ee\u5f55", None))
        self.tbtnSelect.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u7c7b\u578b\u9009\u62e9", None))
        self.rbtnCSV2MAP.setText(QCoreApplication.translate("Form", u"CSV\u8f6cTXTMAP", None))
        self.rbtnMAP2TXT.setText(QCoreApplication.translate("Form", u"\u5ba2\u4f9bMAP\u8f6cTXT", None))
        self.rbtnCSV2TIME.setText(QCoreApplication.translate("Form", u"TIMELOG\u8f6cMAP/TIME", None))
        self.tbtnDo.setText(QCoreApplication.translate("Form", u"\u6267\u884c", None))
        self.tbtnClose.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

