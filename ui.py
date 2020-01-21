# coding=utf-8
import threading
import api
import time
import pynput
import inspect
import ctypes
from PySide import QtGui, QtCore
import sys


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
    

# ...or, in a non-blocking fashion:


def draw(key):
    api.drawKey(key)

class Worker(QtCore.QThread):

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.key = None
        self.listener = pynput.keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.thread = None
    def __del__(self):
        self.working = False
        self.wait()
    def on_press(self, key):
        #print key
        try:
            if key == pynput.keyboard.Key.enter:
                stop_thread(self.thread)
                self.thread = None
        except AttributeError:
            pass
    def run(self):
        self.thread = threading.Thread(target=draw, args=(self.key,))
        self.thread.start()

    
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.t = None
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
        self.thread = Worker()
        self.show()
        
    def line_edit_text_changed(self, text):
        if text:  # Check to see if text is filled in
            self.start_btn.setEnabled(True)
        else:
            self.start_btn.setEnabled(False)
    def startAction(self):
        key = self.pictureEdit.text()
        self.setWindowState(QtCore.Qt.WindowMinimized)
        self.thread.key = key
        self.thread.start()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

    

 
