# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mashtabirovanie.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem
from datetime import datetime

class BankInterest(object):

    def __init__(self, summ, period, perc):
        self.summ = summ
        self.period = period
        self.perc = perc

    def diff_int(self):
        arr = []
        ost = []
        mp_cnt = self.period
        rest = self.summ
        mp_real = self.summ / (self.period)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2))
            ost.append(round(rest, 2))
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr, round(sum(arr), 2), ost 

    def ann_int(self):
        mp_cnt = self.period
        r = self.perc / 1200.0
        ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
        mp = self.summ * ak
        total = mp * mp_cnt
        return round(mp, 2), round(total, 2)


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(937, 857)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
                MainWindow.setSizePolicy(sizePolicy)
                MainWindow.setMinimumSize(QtCore.QSize(877, 824))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                font = QtGui.QFont()
                font.setFamily("Niagara Engraved")
                self.centralwidget.setFont(font)
                self.centralwidget.setStyleSheet("background-color: rgb(37, 39, 48);")
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.gridtab2Layout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridtab2Layout.setObjectName("gridtab2Layout")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
                self.tab.setSizePolicy(sizePolicy)
                self.tab.setObjectName("tab")
                self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.gridLayout_2 = QtWidgets.QGridLayout()
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.widget = QtWidgets.QWidget(self.tab)
                self.widget.setObjectName("widget")
                self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.srok = QtWidgets.QLineEdit(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.srok.sizePolicy().hasHeightForWidth())
                self.srok.setSizePolicy(sizePolicy)
                self.srok.setStyleSheet(self.stylelineedit())
                self.srok.setObjectName("srok")
                self.gridLayout_4.addWidget(self.srok, 8, 0, 1, 1)
                self.summ = QtWidgets.QLineEdit(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.summ.sizePolicy().hasHeightForWidth())
                self.summ.setSizePolicy(sizePolicy)
                self.summ.setStyleSheet(self.stylelineedit())
                self.summ.setObjectName("summ")
                self.gridLayout_4.addWidget(self.summ, 2, 0, 1, 1)
                self.vvsum = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vvsum.sizePolicy().hasHeightForWidth())
                self.vvsum.setSizePolicy(sizePolicy)
                self.vvsum.setStyleSheet(self.styletext())
                self.vvsum.setAlignment(QtCore.Qt.AlignCenter)
                self.vvsum.setObjectName("vvsum")
                self.gridLayout_4.addWidget(self.vvsum, 1, 0, 1, 1)
                self.sinm = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sinm.sizePolicy().hasHeightForWidth())
                self.sinm.setSizePolicy(sizePolicy)
                self.sinm.setStyleSheet(self.styletext())
                self.sinm.setAlignment(QtCore.Qt.AlignCenter)
                self.sinm.setObjectName("sinm")
                self.gridLayout_4.addWidget(self.sinm, 14, 0, 1, 1)
                self.sinmred = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sinmred.sizePolicy().hasHeightForWidth())
                self.sinmred.setSizePolicy(sizePolicy)
                self.sinmred.setStyleSheet(self.styletext2())
                self.sinmred.setAlignment(QtCore.Qt.AlignCenter)
                self.sinmred.setObjectName("sinmred")
                self.gridLayout_4.addWidget(self.sinmred, 15, 0, 1, 1)
                self.vvsum_5 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vvsum_5.sizePolicy().hasHeightForWidth())
                self.vvsum_5.setSizePolicy(sizePolicy)
                self.vvsum_5.setStyleSheet(self.styletext())
                self.vvsum_5.setAlignment(QtCore.Qt.AlignCenter)
                self.vvsum_5.setObjectName("vvsum_5")
                self.gridLayout_4.addWidget(self.vvsum_5, 4, 3, 1, 1)
                self.vvsum_2 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vvsum_2.sizePolicy().hasHeightForWidth())
                self.vvsum_2.setSizePolicy(sizePolicy)
                self.vvsum_2.setStyleSheet(self.styletext())
                self.vvsum_2.setAlignment(QtCore.Qt.AlignCenter)
                self.vvsum_2.setObjectName("vvsum_2")
                self.gridLayout_4.addWidget(self.vvsum_2, 3, 0, 1, 1)
                self.diff = QtWidgets.QRadioButton(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.diff.sizePolicy().hasHeightForWidth())
                self.diff.setSizePolicy(sizePolicy)
                self.diff.setStyleSheet("background-color: rgb(43, 45, 56);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 87 18pt \"Arial Black\";")
                self.diff.setObjectName("diff")
                self.gridLayout_4.addWidget(self.diff, 2, 2, 1, 2)
                self.annuit = QtWidgets.QRadioButton(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.annuit.sizePolicy().hasHeightForWidth())
                self.annuit.setSizePolicy(sizePolicy)
                self.annuit.setStyleSheet("background-color: rgb(43, 45, 56);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 87 18pt \"Arial Black\";")
                self.annuit.setObjectName("annuit")
                self.gridLayout_4.addWidget(self.annuit, 3, 2, 1, 2)
                self.label = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
                self.label.setSizePolicy(sizePolicy)
                self.label.setBaseSize(QtCore.QSize(100, 100))
                self.label.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "font: 87 23pt \"Arial Black\";")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.gridLayout_4.addWidget(self.label, 0, 0, 1, 4)
                self.vvsum_3 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vvsum_3.sizePolicy().hasHeightForWidth())
                self.vvsum_3.setSizePolicy(sizePolicy)
                self.vvsum_3.setMinimumSize(QtCore.QSize(50, 100))
                self.vvsum_3.setStyleSheet(self.styletext())
                self.vvsum_3.setAlignment(QtCore.Qt.AlignCenter)
                self.vvsum_3.setObjectName("vvsum_3")
                self.gridLayout_4.addWidget(self.vvsum_3, 1, 2, 1, 2)
                self.sumnedred = QtWidgets.QLineEdit(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sumnedred.sizePolicy().hasHeightForWidth())
                self.sumnedred.setSizePolicy(sizePolicy)
                self.sumnedred.setStyleSheet(self.stylelineedit())
                self.gridLayout_4.addWidget(self.sumnedred, 5, 3, 1, 1)
                self.vvsum_4 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vvsum_4.sizePolicy().hasHeightForWidth())
                self.vvsum_4.setSizePolicy(sizePolicy)
                self.vvsum_4.setStyleSheet(self.styletext())
                self.vvsum_4.setAlignment(QtCore.Qt.AlignCenter)
                self.vvsum_4.setObjectName("vvsum_4")
                self.gridLayout_4.addWidget(self.vvsum_4, 5, 0, 1, 1)
                self.pushButton = QtWidgets.QPushButton(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                self.pushButton.setSizePolicy(sizePolicy)
                self.pushButton.setStyleSheet("background-color: rgb(43, 45, 56);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 87 18pt \"Arial Black\";")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.raschet)
                self.gridLayout_4.addWidget(self.pushButton, 11, 3, 1, 1)
                self.vseg = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vseg.sizePolicy().hasHeightForWidth())
                self.vseg.setSizePolicy(sizePolicy)
                self.vseg.setStyleSheet(self.styletext())
                self.vseg.setAlignment(QtCore.Qt.AlignCenter)
                self.vseg.setObjectName("vseg")
                self.gridLayout_4.addWidget(self.vseg, 14, 2, 1, 2)
                self.pereplata = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pereplata.sizePolicy().hasHeightForWidth())
                self.pereplata.setSizePolicy(sizePolicy)
                self.pereplata.setStyleSheet(self.styletext2())
                self.pereplata.setAlignment(QtCore.Qt.AlignCenter)
                self.pereplata.setObjectName("pereplata")
                self.gridLayout_4.addWidget(self.pereplata, 17, 0, 1, 4)
                self.vsegred = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vsegred.sizePolicy().hasHeightForWidth())
                self.vsegred.setSizePolicy(sizePolicy)
                self.vsegred.setStyleSheet(self.styletext2())
                self.vsegred.setAlignment(QtCore.Qt.AlignCenter)
                self.vsegred.setObjectName("vsegred")
                self.gridLayout_4.addWidget(self.vsegred, 15, 2, 1, 2)
                self.vseg_2 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.vseg_2.sizePolicy().hasHeightForWidth())
                self.vseg_2.setSizePolicy(sizePolicy)
                self.vseg_2.setStyleSheet(self.styletext())
                self.vseg_2.setAlignment(QtCore.Qt.AlignCenter)
                self.vseg_2.setObjectName("vseg_2")
                self.gridLayout_4.addWidget(self.vseg_2, 16, 0, 1, 4)
                self.proc = QtWidgets.QLineEdit(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.proc.sizePolicy().hasHeightForWidth())
                self.proc.setSizePolicy(sizePolicy)
                self.proc.setStyleSheet(self.stylelineedit())
                self.proc.setObjectName("proc")
                self.gridLayout_4.addWidget(self.proc, 4, 0, 1, 1)
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout.addItem(spacerItem)
                self.comboBox = QtWidgets.QComboBox(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
                self.comboBox.setSizePolicy(sizePolicy)
                self.comboBox.setStyleSheet("background-color: rgb(43, 45, 56);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 87 13pt \"Arial Black\";")
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.verticalLayout.addWidget(self.comboBox)
                spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout.addItem(spacerItem1)
                self.gridLayout_4.addLayout(self.verticalLayout, 8, 1, 1, 1)
                self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
                self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab, "")


                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.gridtabLayout = QtWidgets.QGridLayout(self.tab_2)
                self.gridtabLayout.setObjectName("gridtabLayout")
                self.table = QtWidgets.QTableWidget(self.tab_2)
                self.table.setObjectName("table")
                self.table.setGeometry(QtCore.QRect(0, 0, 861, 781))
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(
                ["Дата платежа", "Сумма платежа", "В погашение долга", "В погашение процентов", "Остаток задолженности"])
                self.table.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                self.tabWidget.addTab(self.tab_2, "")

                self.tabWidget.setStyleSheet("""color: rgb(0, 0, 0); 

                """)
                self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
                self.gridtabLayout.addWidget(self.table, 0, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Кредитный калькулятор"))
                self.vvsum.setText(_translate("MainWindow", "Введите первый взнос"))
                self.sinm.setText(_translate("MainWindow", "Сумма в месяц"))
                self.sinmred.setText(_translate("MainWindow", "~"))
                self.vvsum_5.setText(_translate("MainWindow", "Введите сумму ипотеки"))
                self.vvsum_2.setText(_translate("MainWindow", "Введите процент"))
                self.diff.setText(_translate("MainWindow", "Дифференцированные "))
                self.annuit.setText(_translate("MainWindow", "Аннуитентные"))
                self.label.setText(_translate("MainWindow", "Кредитный калькулятор"))
                self.vvsum_3.setText(_translate("MainWindow", "Выберите тип платежей"))
                self.vvsum_4.setText(_translate("MainWindow", "Введите срок кредита"))
                self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
                self.vseg.setText(_translate("MainWindow", "Сумма с процентами "))
                self.pereplata.setText(_translate("MainWindow", "~"))
                self.vsegred.setText(_translate("MainWindow", "~"))
                self.vseg_2.setText(_translate("MainWindow", "Переплата"))
                self.comboBox.setItemText(0, _translate("MainWindow", "г\\лет"))
                self.comboBox.setItemText(1, _translate("MainWindow", "мес"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Калькулятор"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Таблица выплат"))


        def styletext(self):
                return """
                color: rgb(255, 255, 255);
                font: 87 16pt \"Arial Black\";
                """

        def styletext2(self):
                return """
                background-color: rgb(43, 45, 56);
                color: rgb(255, 255, 255);
                border: 2px solid rgb(37, 39, 48); border-radius: 5px;
                border: 2px solid rgb(48, 50, 62);
                border: 2px solid rgb(85, 170, 255); background-color: rgb(43, 45, 56);
                font: 87 15pt \"Arial Black\";
                """

        def stylelineedit(self):
                return """
                border: 2px solid rgb(37, 39, 48); border-radius: 20px;
                color: #FFF;
                padding-left: 20px;
                padding-right: 20px;
                background-color: rgb(34, 36, 44);
                border: 2px solid rgb(48, 50, 62);
                border: 2px solid rgb(85, 170, 255); background-color: rgb(43, 45, 56);
                color: rgb(255, 255, 255);
                font: 87 13pt \"Arial Black\";

                """

        def oshibka(self, toshibka):
                dlg = QMessageBox()
                dlg.setWindowTitle("Ошибка")
                dlg.setText(toshibka)
                button = dlg.exec()

                if button == QMessageBox.Ok:
                        print("OK!")


        def checker_perv(self, s):
                k = 0
                try:
                    perv = int(self.summ.text())
                except ValueError:
                    perv = -1
                    k += 1
                try:
                    a = list(self.summ.text())
                except IndexError:
                    a[0] = 1
                try:
                    if a[0] == '-':
                        perv = -1
                        k += 1
                except IndexError:
                    k += 1
                c = self.summ.text()
                print(c)
                if c == '':
                    perv = 0
                    k = 0
                if k > 0:
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Первый взнос введен некорректно\n'
                return perv, s

        def checker_procenty(self, s):
                k = 0
                try:
                    procenty = int(self.proc.text())
                except ValueError:
                    procenty = -1
                    k += 1
                try:
                    procenty = float(self.proc.text())
                except ValueError:
                    procenty = -1
                    k += 1
                try:
                    a = list(self.proc.text())
                except IndexError:
                    a[0] = 1
                try:
                    if a[0] == '-':
                        procenty = -1
                        k += 1
                except IndexError:
                    k += 1
                if procenty > 100 or procenty == 0:
                    procenty = -1
                    k += 1
                if k > 0:
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Процент введен некорректно\n'
                return procenty, s

        def checker_srok(self, s):
                k = 0
                try:
                    srok = int(self.srok.text())
                except ValueError:
                    srok = -1
                    k += 1
                try:
                    a = list(self.srok.text())
                except IndexError:
                    a[0] = 1
                try:
                    if a[0] == '-':
                        srok = -1
                        k += 1
                except IndexError:
                    k += 1
                comboValue = self.comboBox.currentText()
                print(comboValue)
                if comboValue == 'г\лет' and srok != -1:
                    srok = srok * 12
                if k > 0:
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Срок введен некорректно\n'
                else:
                    if srok == 0 or srok > 720:
                        srok = -1
                        self.sinmred.setText('Ошибка')
                        self.vsegred.setText('Ошибка')
                        self.pereplata.setText('Ошибка')
                        s = s + 'Срок укажите в диапазоне от 1 месяца до 60 лет\n'

                return srok, s

        def checker_ipoteca(self, s, perv):
                k = 0
                try:
                    ipoteca = int(self.sumnedred.text())
                except ValueError:
                    ipoteca = -1
                    k += 1
                try:
                    a = list(self.sumnedred.text())
                except IndexError:
                    a[0] = 1
                try:
                    if a[0] == '-':
                        ipoteca = -1
                        k += 1
                except IndexError:
                    k += 1
                if k > 0:
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Сумма ипотеки введена некорректно\n'
                elif ipoteca == 0 or ipoteca > 100000000:
                    ipoteca = -1
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Сумма ипотеки не может быть равна 0 или больше 100 000 000 \n'
                else:
                    if perv >= ipoteca:
                        ipoteca = -1
                        self.sinmred.setText('Ошибка')
                        self.vsegred.setText('Ошибка')
                        self.pereplata.setText('Ошибка')
                        s = s + 'Первый взнос больше или равен cумме ипотеки\n'

                return ipoteca, s

        def checker_tipplat(self, s):
                plat = 1
                if not (self.diff.isChecked() or self.annuit.isChecked()):
                    plat = -1
                    self.sinmred.setText('Ошибка')
                    self.vsegred.setText('Ошибка')
                    self.pereplata.setText('Ошибка')
                    s = s + 'Тип платежей не выбран\n'

                return plat, s

        def diff_table(self, srok, arr, ost):
                currentMonth = datetime.now().month + 1
                currentYear = datetime.now().year
                list_calendar = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                                 "Ноябрь", "Декабрь"]
                self.table.setRowCount(srok)
                for i in range(srok):
                    data = (list_calendar[(currentMonth % 12 - 1)] + ', ' + str(currentYear))
                    currentMonth += 1
                    if currentMonth % 12 == 1:
                        currentYear += 1
                    self.table.setItem(i, 0, QTableWidgetItem(data))
                for i in range(srok):
                    self.table.setItem(i, 1, QTableWidgetItem(str(arr[i])))
                ost[srok-1]  = 0                  
                for i in range(srok):
                    self.table.setItem(i, 4, QTableWidgetItem(str(round(ost[i], 1))))

        def annuit_table(self, srok, mp, total):
                currentMonth = datetime.now().month + 1
                currentYear = datetime.now().year
                list_calendar = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                                 "Ноябрь", "Декабрь"]
                self.table.setRowCount(srok)
                for i in range(srok):
                    data = (list_calendar[(currentMonth % 12 - 1)] + ', ' + str(currentYear))
                    currentMonth += 1
                    if currentMonth % 12 == 1:
                        currentYear += 1
                    self.table.setItem(i, 0, QTableWidgetItem(data))
                for i in range(srok):
                    self.table.setItem(i, 1, QTableWidgetItem(str(mp)))
                ost = total
                for i in range(srok):
                    if i != srok-1:
                        ost = ost - mp
                        self.table.setItem(i, 4, QTableWidgetItem(str(round(ost, 1))))
                    else:
                        ost = 0
                        self.table.setItem(i, 4, QTableWidgetItem(str(round(ost, 1))))    

        def raschet(self):
                s = ''
                perv, s = self.checker_perv(s)
                procenty, s = self.checker_procenty(s)
                srok, s = self.checker_srok(s)
                ipoteca, s = self.checker_ipoteca(s, perv)
                plat, s = self.checker_tipplat(s)
                try:
                    if (perv != -1 and procenty != -1 and srok != -1 and ipoteca != -1 and plat != -1):
                        cymma = ipoteca - perv
                        a = BankInterest(cymma, srok, procenty)
                        if self.diff.isChecked():
                            arr, total, ost = a.diff_int()
                            self.sinm.setText("Сумма в месяц")
                            itog = srok - 1
                            itog = str(arr[itog])
                            self.sinmred.setText(str(arr[0]) + '...' + itog + ' р')
                            self.vsegred.setText(str(total) + ' р')
                            perepl = total - (ipoteca - perv)
                            self.pereplata.setText(str(round(perepl, 2)) + ' р')
                            self.diff_table(srok, arr, ost)

                        if self.annuit.isChecked():
                            mp, total = a.ann_int()
                            self.sinm.setText("Сумма в месяц")
                            self.sinmred.setText(str(mp) + ' р')
                            self.vsegred.setText(str(total) + ' р')
                            perepl = total - (ipoteca - perv)
                            self.pereplata.setText(str(round(perepl, 2)) + ' р')
                            self.annuit_table(srok, mp, total)
                    else:
                        self.oshibka(s)
                except:
                    pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
