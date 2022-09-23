#region import
from ast import Num
from glob import glob
from pickle import NONE
from re import X
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
import tkinter.font as font
#endregion

bit = []
data = []
cycle = 0
status = True
profile = 1

#window 선언
root = tk.Tk()
root.title('SPICA Sensor Comm')
root.resizable(width=False, height=False)


fig = plt.figure(figsize=(12,8))
plt.subplots_adjust(left=0.35)
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=1)
anim = None

var = tk.StringVar()

#region FUNC
def animate(event):
    global profile,var,frame2
    if profile != 4 :
        data = py_Serial_1.serial_recieve(ser,profile)
        Ydata = list(data)
        x = np.linspace(0,127,128)
        y = (Ydata)
        line.set_data(x, y)
        return line,
    elif profile == 4 :
        data = py_Serial_1.serial_recieve(ser,profile) 

        # 슬립타임마다 렉이걸려서 쓰레드 고려
        var.set('123123')
        print(data[0])
        frame2.update_idletasks()
        time.sleep(0.5)
        

def btnfunc(label):
    global status, ax, anim, profile
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

def openFrame(frame) :
    global profile,anim
    if frame == frame2 :
        profile = 4
    if frame == frame1 :
        profile = 1
    frame.tkraise()

def measureUpdate(data) :
    global var
    while True :
        var.set('123123')
        frame2.update_idletasks()
        time.sleep(2)

#endregion

#'''Frame 선언'''
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.grid(column=0, row=1, sticky="nsew")
frame2.grid(column=0, row=1, sticky="nsew")


# ''' Add Button '''
# Period BTN
resetax1 = plt.axes([0.05, 0.78, 0.2, 0.04])
btnpUNPROCESSED = Button(resetax1, label= 'UNPROCESSED', color="lightgray", hovercolor='0.975')
resetax2 = plt.axes([0.05, 0.73, 0.2, 0.04])
btnpLOWER = Button(resetax2, label= 'LOWER', color="lightgray", hovercolor='0.975')
resetax3 = plt.axes([0.05, 0.68, 0.2, 0.04])
btnpDERIVATIVE = Button(resetax3, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')

# OneShot BTN
resetax5 = plt.axes([0.05, 0.35, 0.2, 0.04])
btnoUNPROCESSED = Button(resetax5, label= 'UNPROCESSED', color="lightgray", hovercolor='0.975')
resetax6 = plt.axes([0.05, 0.3, 0.2, 0.04])
btnoLOWER = Button(resetax6, label= 'LOWER', color="lightgray", hovercolor='0.975')
resetax7 = plt.axes([0.05, 0.25, 0.2, 0.04])
btnoDERIVATIVE = Button(resetax7, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')

# '''TEXT BOX'''
mybox = {'facecolor':'y','edgecolor':'r','boxstyle':'round','alpha':0.5}
plt.text(0.05,15,('Period Scan'),fontsize = 11, bbox=mybox)
plt.text(0.05,4,('OneShot Scan'),fontsize = 11, bbox=mybox)



label1 = tk.Label(frame2, text = 'Status 1 :',font=(15))
label1.pack(anchor='w')
label7 = tk.Label(frame2, textvariable=var ,font=(15))

label2 = tk.Label(frame2, text = 'Status :',font=(15))
label2.pack(anchor='w')
label3 = tk.Label(frame2, text = 'Position :',font=(15))
label3.pack(anchor='w')
label4 = tk.Label(frame2, text = 'Energy :',font=(15))
label4.pack(anchor='w')
label5 = tk.Label(frame2, text = 'UNDEF :',font=(15))
label5.pack(anchor='w')
label6 = tk.Label(frame2, text = 'UNDEF :',font=(15))
label6.pack(anchor='w')

# Frame BTN
f = font.Font(size=15, weight='bold')
btnToFrame1 = tk.Button(frame2,
    text= "Change To Profile",
    padx=100,
    pady=10,
    command=lambda:[openFrame(frame1)])
btnToFrame2 = tk.Button(frame1,
    text= "Change To Measure",
    padx=100,
    pady=10,
    command=lambda:[openFrame(frame2)])
btnToFrame1['font'] = f
btnToFrame2['font'] = f



if __name__ == '__main__' :
    print("SPICA Sensor 스캔을 시작 합니다.")
    #region PLC 통신 스레드
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
    #endregion

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
    
    btnpUNPROCESSED.on_clicked(btnfunc)
    btnpLOWER.on_clicked(btnfunc)
    btnpDERIVATIVE.on_clicked(btnfunc)

    btnoUNPROCESSED.on_clicked(btnfunc)
    btnoLOWER.on_clicked(btnfunc)
    btnoDERIVATIVE.on_clicked(btnfunc)

    canvas = FigureCanvasTkAgg(fig, master=frame1) 
    canvas.get_tk_widget().pack()
    
    anim = FuncAnimation(fig, animate, interval=500)

    btnToFrame1.pack(fill='x')
    btnToFrame2.pack(fill='x',side='bottom', anchor='s',expand= True)
    openFrame(frame1)
    tk.mainloop()

    # 통신중인지 확인하는 쓰레드. 나중에 추가
    # th_PlcisCon = threading.Thread(target=py_snap7.plcIsConnect, args=(bit,))
    # th_PlcisCon.start()

    
