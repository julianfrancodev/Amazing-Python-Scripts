from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_guiVersion(object):
    def setupUi(self, guiVersion):
        guiVersion.setObjectName("guiVersion")
        guiVersion.resize(360, 390)
        guiVersion.setMinimumSize(QtCore.QSize(360, 390))
        guiVersion.setMaximumSize(QtCore.QSize(360, 390))
        self.label = QtWidgets.QLabel(guiVersion)
        self.label.setGeometry(QtCore.QRect(160, 10, 41, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_n1 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n1.setEnabled(True)
        self.pushButton_n1.setGeometry(QtCore.QRect(70, 90, 60, 50))
        self.pushButton_n1.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n1.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n1.setFlat(False)
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.pushButton_convert = QtWidgets.QPushButton(guiVersion)
        self.pushButton_convert.setEnabled(True)
        self.pushButton_convert.setGeometry(QtCore.QRect(70, 330, 220, 50))
        self.pushButton_convert.setMinimumSize(QtCore.QSize(220, 50))
        self.pushButton_convert.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.pushButton_convert.setFont(font)
        self.pushButton_convert.setStyleSheet(
            "background-color: rgb(27, 226, 52);")
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.pushButton_del = QtWidgets.QPushButton(guiVersion)
        self.pushButton_del.setGeometry(QtCore.QRect(230, 270, 60, 50))
        self.pushButton_del.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_del.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setStyleSheet(
            "background-color: rgb(110, 202, 222);")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_n3 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n3.setEnabled(True)
        self.pushButton_n3.setGeometry(QtCore.QRect(230, 90, 60, 50))
        self.pushButton_n3.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n3.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n3.setFlat(False)
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.pushButton_n2 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n2.setEnabled(True)
        self.pushButton_n2.setGeometry(QtCore.QRect(150, 90, 60, 50))
        self.pushButton_n2.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n2.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n2.setFlat(False)
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.pushButton_n9 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n9.setEnabled(True)
        self.pushButton_n9.setGeometry(QtCore.QRect(230, 210, 60, 50))
        self.pushButton_n9.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n9.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n9.setFlat(False)
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.pushButton_n8 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n8.setEnabled(True)
        self.pushButton_n8.setGeometry(QtCore.QRect(150, 210, 60, 50))
        self.pushButton_n8.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n8.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n8.setFlat(False)
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.pushButton_n7 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n7.setEnabled(True)
        self.pushButton_n7.setGeometry(QtCore.QRect(70, 210, 60, 50))
        self.pushButton_n7.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n7.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n7.setFlat(False)
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.pushButton_n6 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n6.setEnabled(True)
        self.pushButton_n6.setGeometry(QtCore.QRect(230, 150, 60, 50))
        self.pushButton_n6.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n6.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n6.setFlat(False)
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.pushButton_n5 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n5.setEnabled(True)
        self.pushButton_n5.setGeometry(QtCore.QRect(150, 150, 60, 50))
        self.pushButton_n5.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n5.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n5.setFlat(False)
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.pushButton_n4 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n4.setEnabled(True)
        self.pushButton_n4.setGeometry(QtCore.QRect(70, 150, 60, 50))
        self.pushButton_n4.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n4.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n4.setFlat(False)
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.pushButton_n0 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n0.setEnabled(True)
        self.pushButton_n0.setGeometry(QtCore.QRect(150, 270, 60, 50))
        self.pushButton_n0.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n0.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n0.setFlat(False)
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.label_1 = QtWidgets.QLabel(guiVersion)
        self.label_1.setGeometry(QtCore.QRect(10, 50, 140, 30))
        self.label_1.setMinimumSize(QtCore.QSize(140, 30))
        self.label_1.setMaximumSize(QtCore.QSize(140, 30))
        self.label_1.setStyleSheet("background-color: rgb(245, 121, 0, 65);")
        self.label_1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_1.setIndent(-1)
        self.label_1.setMargin(5)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(guiVersion)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 140, 30))
        self.label_2.setMinimumSize(QtCore.QSize(140, 30))
        self.label_2.setMaximumSize(QtCore.QSize(140, 30))
        self.label_2.setStyleSheet("background-color: rgb(52, 101, 164, 65);")
        self.label_2.setText("")
        self.label_2.setIndent(-1)
        self.label_2.setMargin(5)
        self.label_2.setObjectName("label_2")
        self.pushButton_n10 = QtWidgets.QPushButton(guiVersion)
        self.pushButton_n10.setEnabled(True)
        self.pushButton_n10.setGeometry(QtCore.QRect(70, 270, 60, 50))
        self.pushButton_n10.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_n10.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_n10.setFont(font)
        self.pushButton_n10.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_n10.setFlat(False)
        self.pushButton_n10.setObjectName("pushButton_n10")
        self.comboBox_2 = QtWidgets.QComboBox(guiVersion)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 10, 140, 30))
        self.comboBox_2.setMinimumSize(QtCore.QSize(140, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(140, 30))
        self.comboBox_2.setMaxVisibleItems(6)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox = QtWidgets.QComboBox(guiVersion)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 140, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(140, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(140, 30))
        self.comboBox.setMaxVisibleItems(6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(guiVersion)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(guiVersion)

    def retranslateUi(self, guiVersion):
        _translate = QtCore.QCoreApplication.translate
        guiVersion.setWindowTitle(_translate(
            "guiVersion", "Cryptocurrency Converter"))
        self.label.setText(_translate(
            "guiVersion", "<html><head/><body><p><span >To</span></p></body></html>"))
        self.pushButton_n1.setText(_translate("guiVersion", "1"))
        self.pushButton_convert.setText(_translate("guiVersion", "Convert"))
        self.pushButton_del.setText(_translate("guiVersion", "del"))
        self.pushButton_n3.setText(_translate("guiVersion", "3"))
        self.pushButton_n2.setText(_translate("guiVersion", "2"))
        self.pushButton_n9.setText(_translate("guiVersion", "9"))
        self.pushButton_n8.setText(_translate("guiVersion", "8"))
        self.pushButton_n7.setText(_translate("guiVersion", "7"))
        self.pushButton_n6.setText(_translate("guiVersion", "6"))
        self.pushButton_n5.setText(_translate("guiVersion", "5"))
        self.pushButton_n4.setText(_translate("guiVersion", "4"))
        self.pushButton_n0.setText(_translate("guiVersion", "0"))
        self.label_1.setToolTip(_translate(
            "guiVersion", "Enter a value to Convert it."))
        self.label_1.setText(_translate("guiVersion", "0"))
        self.label_2.setToolTip(_translate("guiVersion", "Converted value"))
        self.label_2.setText(_translate("guiVersion", "0"))
        self.pushButton_n10.setText(_translate("guiVersion", "."))
        self.comboBox_2.setItemText(0, _translate("guiVersion", "USD"))
        self.comboBox_2.setItemText(1, _translate("guiVersion", "EUR"))
        self.comboBox_2.setItemText(2, _translate("guiVersion", "------"))
        self.comboBox_2.setItemText(3, _translate("guiVersion", "BTC"))
        self.comboBox_2.setItemText(4, _translate("guiVersion", "ETH"))
        self.comboBox_2.setItemText(5, _translate("guiVersion", "XRP"))
        self.comboBox_2.setItemText(6, _translate("guiVersion", "BCH"))
        self.comboBox_2.setItemText(7, _translate("guiVersion", "EOS"))
        self.comboBox_2.setItemText(8, _translate("guiVersion", "XLM"))
        self.comboBox_2.setItemText(9, _translate("guiVersion", "LTC"))
        self.comboBox_2.setItemText(10, _translate("guiVersion", "USDT"))
        self.comboBox_2.setItemText(11, _translate("guiVersion", "ADA"))
        self.comboBox_2.setItemText(12, _translate("guiVersion", "XMR"))
        self.comboBox_2.setItemText(13, _translate("guiVersion", "DASH"))
        self.comboBox_2.setItemText(14, _translate("guiVersion", "MIOTA"))
        self.comboBox_2.setItemText(15, _translate("guiVersion", "TRX"))
        self.comboBox_2.setItemText(16, _translate("guiVersion", "ETC"))
        self.comboBox_2.setItemText(17, _translate("guiVersion", "NEO"))
        self.comboBox_2.setItemText(18, _translate("guiVersion", "XTZ"))
        self.comboBox_2.setItemText(19, _translate("guiVersion", "BNB"))
        self.comboBox_2.setItemText(20, _translate("guiVersion", "XEM"))
        self.comboBox_2.setItemText(21, _translate("guiVersion", "VET"))
        self.comboBox_2.setItemText(22, _translate("guiVersion", "DOGE"))
        self.comboBox_2.setItemText(23, _translate("guiVersion", "ZEC"))
        self.comboBox_2.setItemText(24, _translate("guiVersion", "OMG"))
        self.comboBox_2.setItemText(25, _translate("guiVersion", "LSK"))
        self.comboBox_2.setItemText(26, _translate("guiVersion", "BTG"))
        self.comboBox_2.setItemText(27, _translate("guiVersion", "BCN"))
        self.comboBox_2.setItemText(28, _translate("guiVersion", "ONT"))
        self.comboBox_2.setItemText(29, _translate("guiVersion", "NANO"))
        self.comboBox_2.setItemText(30, _translate("guiVersion", "BTC"))
        self.comboBox_2.setItemText(31, _translate("guiVersion", "DCR"))
        self.comboBox_2.setItemText(32, _translate("guiVersion", "QTUM"))
        self.comboBox_2.setItemText(33, _translate("guiVersion", "MKR"))
        self.comboBox_2.setItemText(34, _translate("guiVersion", "ZRX"))
        self.comboBox_2.setItemText(35, _translate("guiVersion", "DGB"))
        self.comboBox_2.setItemText(36, _translate("guiVersion", "BCD"))
        self.comboBox_2.setItemText(37, _translate("guiVersion", "ZIL"))
        self.comboBox_2.setItemText(38, _translate("guiVersion", "ICX"))
        self.comboBox_2.setItemText(39, _translate("guiVersion", "STEEM"))
        self.comboBox.setCurrentText(_translate("guiVersion", "BTC"))
        self.comboBox.setItemText(0, _translate("guiVersion", "BTC"))
        self.comboBox.setItemText(1, _translate("guiVersion", "------"))
        self.comboBox.setItemText(2, _translate("guiVersion", "USD"))
        self.comboBox.setItemText(3, _translate("guiVersion", "EUR"))
        self.comboBox.setItemText(4, _translate("guiVersion", "------"))
        self.comboBox.setItemText(5, _translate("guiVersion", "ETH"))
        self.comboBox.setItemText(6, _translate("guiVersion", "XRP"))
        self.comboBox.setItemText(7, _translate("guiVersion", "BCH"))
        self.comboBox.setItemText(8, _translate("guiVersion", "EOS"))
        self.comboBox.setItemText(9, _translate("guiVersion", "XLM"))
        self.comboBox.setItemText(10, _translate("guiVersion", "LTC"))
        self.comboBox.setItemText(11, _translate("guiVersion", "USDT"))
        self.comboBox.setItemText(12, _translate("guiVersion", "ADA"))
        self.comboBox.setItemText(13, _translate("guiVersion", "XMR"))
        self.comboBox.setItemText(14, _translate("guiVersion", "DASH"))
        self.comboBox.setItemText(15, _translate("guiVersion", "MIOTA"))
        self.comboBox.setItemText(16, _translate("guiVersion", "TRX"))
        self.comboBox.setItemText(17, _translate("guiVersion", "ETC"))
        self.comboBox.setItemText(18, _translate("guiVersion", "NEO"))
        self.comboBox.setItemText(19, _translate("guiVersion", "XTZ"))
        self.comboBox.setItemText(20, _translate("guiVersion", "BNB"))
        self.comboBox.setItemText(21, _translate("guiVersion", "XEM"))
        self.comboBox.setItemText(22, _translate("guiVersion", "VET"))
        self.comboBox.setItemText(23, _translate("guiVersion", "DOGE"))
        self.comboBox.setItemText(24, _translate("guiVersion", "ZEC"))
        self.comboBox.setItemText(25, _translate("guiVersion", "OMG"))
        self.comboBox.setItemText(26, _translate("guiVersion", "LSK"))
        self.comboBox.setItemText(27, _translate("guiVersion", "BTG"))
        self.comboBox.setItemText(28, _translate("guiVersion", "BCN"))
        self.comboBox.setItemText(29, _translate("guiVersion", "ONT"))
        self.comboBox.setItemText(30, _translate("guiVersion", "NANO"))
        self.comboBox.setItemText(31, _translate("guiVersion", "BTC"))
        self.comboBox.setItemText(32, _translate("guiVersion", "DCR"))
        self.comboBox.setItemText(33, _translate("guiVersion", "QTUM"))
        self.comboBox.setItemText(34, _translate("guiVersion", "MKR"))
        self.comboBox.setItemText(35, _translate("guiVersion", "ZRX"))
        self.comboBox.setItemText(36, _translate("guiVersion", "DGB"))
        self.comboBox.setItemText(37, _translate("guiVersion", "BCD"))
        self.comboBox.setItemText(38, _translate("guiVersion", "ZIL"))
        self.comboBox.setItemText(39, _translate("guiVersion", "ICX"))
        self.comboBox.setItemText(40, _translate("guiVersion", "STEEM"))
