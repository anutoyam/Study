#region import
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
from matplotlib.widgets import Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
#endregion

bit = []
cycle = 0
data = []
status = True
profile = 1

fig = plt.figure()
plt.subplots_adjust(left=0.35)
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=1)
anim = None
root = tk.Tk()

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
        status = True
        if label.inaxes._children[0]._text == 'UNPROCESSED' : 
            profile = 1
        elif label.inaxes._children[0]._text == 'LOWER' : 
            profile = 2
        elif label.inaxes._children[0]._text == 'DERIVATIVE' : 
            profile = 3
        
        anim.event_source.start()


# ''' Add Button '''
# Period BTN
resetax1 = plt.axes([0.05, 0.75, 0.2, 0.04])
btnUNPROCESSED = Button(resetax1, label= 'UNPROCESSED', color="lightgray", hovercolor='0.975')
resetax2 = plt.axes([0.05, 0.7, 0.2, 0.04])
btnLOWER = Button(resetax2, label= 'LOWER', color="lightgray", hovercolor='0.975')
resetax3 = plt.axes([0.05, 0.65, 0.2, 0.04])
btnDERIVATIVE = Button(resetax3, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')
resetax4 = plt.axes([0.05, 0.6, 0.2, 0.04])
btnDERIVATIVE = Button(resetax4, label= 'MEASURE', color="lightgray", hovercolor='0.975')
# OneShot BTN
resetax5 = plt.axes([0.05, 0.3, 0.2, 0.04])
btnUNPROCESSED = Button(resetax5, label= 'UNPROCESSED', color="lightgray", hovercolor='0.975')
resetax6 = plt.axes([0.05, 0.25, 0.2, 0.04])
btnLOWER = Button(resetax6, label= 'LOWER', color="lightgray", hovercolor='0.975')
resetax7 = plt.axes([0.05, 0.2, 0.2, 0.04])
btnDERIVATIVE = Button(resetax7, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')
resetax8 = plt.axes([0.05, 0.15, 0.2, 0.04])
btnDERIVATIVE = Button(resetax8, label= 'MEASURE', color="lightgray", hovercolor='0.975')

# '''TEXT BOX'''
mybox = {'facecolor':'y','edgecolor':'r','boxstyle':'round','alpha':0.5}
plt.text(0.05,17.2,('Period Scan'),fontsize = 11, bbox=mybox)
plt.text(0.05,6,('OneShot Scan'),fontsize = 11, bbox=mybox)

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
        
        # btnUNPROCESSED.on_clicked(btnfunc)
        # btnLOWER.on_clicked(btnfunc)
        # btnDERIVATIVE.on_clicked(btnfunc)
        
        
        # plt.show()
        label = tk.Label(root,text="라벨").grid(column=0, row=1)
        canvas = FigureCanvasTkAgg(fig, master=root) 
        canvas.get_tk_widget().grid(column=0,row=0) 

        anim = FuncAnimation(fig, animate, interval=500)

        tk.mainloop()

        # 통신중인지 확인하는 쓰레드. 나중에 추가
        # th_PlcisCon = threading.Thread(target=py_snap7.plcIsConnect, args=(bit,))
        # th_PlcisCon.start()


    else :
        print("1 또는 2로 입력 해 주세요 : ")
    
