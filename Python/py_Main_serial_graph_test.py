from ast import Num
from glob import glob
from pickle import NONE
import py_Serial_1
#import py_snap7_1
from concurrent.futures import thread
import threading
import time
import threading
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons

bit = []
cycle = 0
data = []
status = True
profile = 1

fig = plt.figure()
plt.subplots_adjust(left=0.35)
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=3)
anim = None

def animate(event):
    
    global profile
    data = py_Serial_1.serial_recieve(ser,profile)
    Ydata = list(data)
    x = np.linspace(0,127,128)
    y = (Ydata)
    line.set_data(x, y)

    return line,

def btnfunc(label):
    global status, ax, anim, profile
    # print(label.inaxes._children[0]._text)
    if status == True :
        anim.event_source.stop()
        status = False
    else : 
        anim.event_source.start()
        status = True
        if label.inaxes._children[0]._text == 'UNPROCESSED' : 
            profile = 1
            print(profile)
        elif label.inaxes._children[0]._text == 'LOWER' : 
            profile = 2
            print(profile)
        elif label.inaxes._children[0]._text == 'DERIVATIVE' : 
            profile = 3
            print(profile)


# ''' Add Button '''
resetax1 = plt.axes([0.05, 0.8, 0.2, 0.04])
btnUNPROCESSED = Button(resetax1, label= 'UNPROCESSED', color="lightgray", hovercolor='0.975')

resetax2 = plt.axes([0.05, 0.7, 0.2, 0.04])
btnLOWER = Button(resetax2, label= 'LOWER', color="lightgray", hovercolor='0.975')

resetax3 = plt.axes([0.05, 0.6, 0.2, 0.04])
btnDERIVATIVE = Button(resetax3, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')

if __name__ == '__main__' :
    print("SPICA Sensor 스캔을 시작 하시겠습니까? (Yes - 1 , No - 2)")
    answer = input()

    if answer == '1' :   
        # try :
        #     print("PLC 와 연결을 시작합니다...")
        #     py_snap7_1.plcConnect()
        #     time.sleep(1)
        #     if py_snap7_1.plcIsConnect() == True :
        #         print("PLC 연결 성공. 데이터 갱신 동작")
        #         # th_PlcRead = threading.Thread(target=py_snap7_1.plcDBRead, args=(data,))
        #         # th_PlcRead.start()  
        #         # while True :
        #         #     data = py_snap7_1.plcDBRead()
        #         #     print(data)
        #         #     time.sleep(1)
        # except :
        #     print("PLC 연결 실패 다시 시도 해주세요")
        #     sys.exit(0)

        try  :
            print("SPICA 와 연결을 시작합니다...")
            ser = py_Serial_1.serial_connect()
            time.sleep(1)
            if py_Serial_1.serial_isconnect(ser) == True :
                print("Sensor 연결 성공. 데이터 갱신 쓰레드 동작")
                # th_SPICARead = threading.Thread(target=py_Serial_1.serial_recieve , args=(ser,))
                # th_SPICARead.start()
        except :
            print("Sensor 연결 실패 다시 시도 해주세요")
            sys.exit(0)
        
        btnUNPROCESSED.on_clicked(btnfunc)
        btnLOWER.on_clicked(btnfunc)
        btnDERIVATIVE.on_clicked(btnfunc)
        
        anim = FuncAnimation(fig, animate, interval=1000)
        plt.show()

        while True :
            cycle += 1
            print("사이클 : ", cycle)
            time.sleep(2)
        
        # 통신중인지 확인하는 쓰레드. 나중에 추가
        # th_PlcisCon = threading.Thread(target=py_snap7.plcIsConnect, args=(bit,))
        # th_PlcisCon.start()


    else :
        print("1 또는 2로 입력 해 주세요 : ")
    
