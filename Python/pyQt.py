import sys
import py_Serial_1
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

form_class = uic.loadUiType("Python//pyQt_test.ui")[0]

class Worker(QThread) :
    timeout = pyqtSignal(int)
    def __init__(self) :
        super().__init__()
        self.num = 0

    def run(self) :
        while True :
            self.timeout.emit(self.num)
            self.num +=1
            self.sleep(1)
        
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # self.worker = Worker()
        # self.worker.start()
        # self.worker.timeout.connect(self.timeout)

        self.graphWidget.setXRange(0,127, padding =0)
        self.graphWidget.setYRange(0,255, padding =0)

        self.btn_Connect.clicked.connect(py_Serial_1.serial_connect)

    def plot(self, hour, temperature) :
        self.graphWidget.clear()
        self.graphWidget.plot(hour, temperature) 

    def timeout(self,num) :
        self.plot([1,2,3,4,5,6,7,8,9,10],[num,31,32,34,38,29,24,32,35,30])

    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
    

    #프로그램 화면을 보여주는 코드
    myWindow.setWindowTitle('SPICA TEST')
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()