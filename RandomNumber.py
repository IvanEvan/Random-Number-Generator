#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-2 下午2:24
# @Author  : Evan
# @File    : main.py
# @Software: PyCharm Community Edition
import os
import sys
import random

from PyQt5.QtWidgets import *


from window import Ui_MainWindow

class MyMainClass(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainClass, self).__init__(parent)
        self.setupUi(self)

    def getRandomnum(self):
        min = self.lineEdit.text()
        max = self.lineEdit_2.text()
        if not min or not max:
            self.label_3.setText('Please enter a range !')
        elif min>=max:
            self.label_3.setText('Error: Min>=Max')
        else:
            result = random.randint(int(min), int(max))
            self.label_3.setText('%d' % (result))
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    my_gui = MyMainClass()
    my_gui.show()
    sys.exit(app.exec_())