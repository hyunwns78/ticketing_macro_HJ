from PyQt5 import QtWidgets
from PyQt5 import uic
from srt_rsrv import SRT
from PyQt5.QtCore import *
import sys
import time
import datetime
from login import *

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.ui = uic.loadUi("gui.ui")
        self.dep = self.ui.depCity                  # 출발지
        self.arr = self.ui.arrCity                  # 도착지
        self.date = self.ui.depDate                 # 출발일
        self.hour = self.ui.depHour                 # 출발시간
        self.map = self.ui.route_map                # SRT/KTX 노선도
        self.table = self.ui.resTable               # 검색결과 표
        self.check_list = [self.ui.checkBox_01,     # 체크박스 10개
                            self.ui.checkBox_02,
                            self.ui.checkBox_03,
                            self.ui.checkBox_04,
                            self.ui.checkBox_05,
                            self.ui.checkBox_06,
                            self.ui.checkBox_07,
                            self.ui.checkBox_08,
                            self.ui.checkBox_09,
                            self.ui.checkBox_10
        ]

        self.srt = SRT()
        self.srt.srt_login()
        time.sleep(3)
        
        today_date = str(datetime.datetime.today().date()).replace('-', '/')
        self.date.setDate(QDate.fromString(today_date, "yyyy/MM/dd"))
        self.ui.searchSeat.clicked.connect(self.find_seat)
        #self.ui.tryReservation.clicked.connect(self.try_seat)

        self.ui.show()

    def find_seat(self):
        self.selected_dep = self.dep.currentText()
        self.selected_arr = self.arr.currentText()

        self.selected_date = self.date.date().toString("yyyyMMdd")
        self.selected_hour = self.hour.currentText() + '0000'

        result = self.srt.plan(self.selected_dep, self.selected_arr, self.selected_date, self.selected_hour)

        for row in range(10):
            for col in range(4):
                self.table.setItem(row, col, QtWidgets.QTableWidgetItem(result[row][col]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = WindowClass()
    #form = Form()
    form.show()
    sys.exit(app.exec())
