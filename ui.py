# coding=utf-8
import threading
import api
import time
import pynput
import inspect
import ctypes
from PySide import QtGui, QtCore
import sys
    
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def draw(self, key):
	    api.drawKey(key)
    def initUI(self):

        self.t = None
        #self.btn.move(30, 120)
        self.start_btn = QtGui.QPushButton(u'开始画图', self)

        self.pictureEdit = QtGui.QLineEdit()
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.pictureEdit, 1, 1,1,1)
        grid.addWidget(self.start_btn, 2,1)        
        self.setLayout(grid)
        self.start_btn.clicked.connect(self.startAction)
        self.setGeometry(400, 300, 150, 100)
        self.setWindowTitle(u'自动你画我猜')
        self.start_btn.setEnabled(False)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  
        self.setFixedSize(self.width(), self.height())
        self.pictureEdit.textChanged.connect(self.line_edit_text_changed)    
        
        self.show()
        
    def line_edit_text_changed(self, text):
        if text:  # Check to see if text is filled in
            self.start_btn.setEnabled(True)
        else:
            self.start_btn.setEnabled(False)

    def startAction(self):
        key = self.pictureEdit.text()
        self.setWindowState(QtCore.Qt.WindowMinimized)
        self.draw(key)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

    

 