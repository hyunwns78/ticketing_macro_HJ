import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
import __init__

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('login.ui') 
form_class = uic.loadUiType(form)[0]

form_second = resource_path('gui.ui')
form_secondwindow = uic.loadUiType(form_second)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
	
    def Loginclick(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = secondwindow()    #
        #self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        print('test')
    #여기에 시그널-슬롯 연결 설정 및 함수 설정.
class secondwindow(QMainWindow,form_secondwindow):
    def __init__(self):
        super(secondwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

