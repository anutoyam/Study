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
profile = 0
ex_profile = 1
status = True
btnTitle = "UNPROCESSED"
ex_btnTitle = ""

#window 선언
root = tk.Tk()
root.title('SPICA Sensor Comm')
root.columnconfigure(2,weight= 1)

vari1 = tk.IntVar()
vari2 = tk.IntVar()
vari3 = tk.IntVar()
vari4 = tk.IntVar()
vari5 = tk.IntVar()
vari6 = tk.IntVar()

fig = plt.figure(figsize=(12,7.02))
plt.subplots_adjust(left=0.35)
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=1)
anim = None

#region FUNC
def animate(event):
    global profile,vari1,vari2,vari3,vari4,vari5,vari6,cycle
    if profile == 1 or profile == 2 or profile == 3 :
        data = py_Serial_1.serial_recieve(ser,profile)
        Ydata = list(data)
        x = np.linspace(0,127,128)
        y = (Ydata)
        line.set_data(x, y)
        return line,
    elif profile == 4 :
        data = py_Serial_1.serial_recieve(ser,profile) 
        # 슬립타임마다 렉이걸려서 쓰레드 고려
        vari1.set(data[0])
        vari2.set(data[1])
        vari3.set(data[2])
        vari4.set(data[3])
        vari5.set(data[4])
        vari6.set(data[5])
        frame2.update()
    elif profile == 5 or profile == 6 or profile == 7 :
        if cycle == 0 :
            data = py_Serial_1.serial_recieve(ser,profile)
            Ydata = list(data)
            x = np.linspace(0,127,128)
            y = (Ydata)
            line.set_data(x, y)
            cycle = 1
            return line,

def btnfunc(label):
    global status, ax, anim, profile, btnTitle, cycle
    print(status)
    if status == True and btnTitle == label.inaxes._children[0]._text:
        btnpUNPROCESSED.color = 'lightgray'
        btnpLOWER.color = 'lightgray'
        btnpDERIVATIVE.color = 'lightgray'
        anim.event_source.stop()
        status = False
    else : 
        if label.inaxes._children[0]._text == 'UNPROCESSED' : 
            profile = 1
            btnTitle = 'UNPROCESSED'
            btnpUNPROCESSED.color = 'red'
            btnpLOWER.color = 'lightgray'
            btnpDERIVATIVE.color = 'lightgray'
        elif label.inaxes._children[0]._text == 'LOWER' : 
            profile = 2
            btnTitle = 'LOWER'
            btnpUNPROCESSED.color = 'lightgray'
            btnpLOWER.color = 'red'
            btnpDERIVATIVE.color = 'lightgray'
        elif label.inaxes._children[0]._text == 'DERIVATIVE' : 
            profile = 3
            btnTitle = 'DERIVATIVE'
            btnpUNPROCESSED.color = 'lightgray'
            btnpLOWER.color = 'lightgray'
            btnpDERIVATIVE.color = 'red'
        elif label.inaxes._children[0]._text == 'OneShot UNPROCESSED' : 
            profile = 5
            cycle = 0
            btnTitle = 'OneShot UNPROCESSED'
            btnpUNPROCESSED.color = 'lightgray'
            btnpLOWER.color = 'lightgray'
            btnpDERIVATIVE.color = 'lightgray'
        elif label.inaxes._children[0]._text == 'OneShot LOWER' : 
            profile = 6
            cycle = 0
            btnTitle = 'OneShot LOWER'
            btnpUNPROCESSED.color = 'lightgray'
            btnpLOWER.color = 'lightgray'
            btnpDERIVATIVE.color = 'lightgray'
        elif label.inaxes._children[0]._text == 'OneShot DERIVATIVE' : 
            profile = 7
            cycle = 0
            btnTitle = 'OneShot DERIVATIVE'
            btnpUNPROCESSED.color = 'lightgray'
            btnpLOWER.color = 'lightgray'
            btnpDERIVATIVE.color = 'lightgray'
        anim.event_source.start()
        status = True

def openFrame(frame) :
    global profile,ex_profile
    if frame == frame2 :
        ex_profile = profile
        profile = 4
    if frame == frame1 :
        profile = ex_profile
    frame.tkraise()
#endregion

#'''Frame 선언'''
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.grid(column=0, row=0, sticky="nsew")
frame2.grid(column=0, row=0, sticky="nsew")

frame3 = tk.Frame(frame2)
frame3.grid(column=0, row=6, sticky="nsew")

# ''' Add Button '''
# Period BTN
resetax1 = plt.axes([0.05, 0.78, 0.2, 0.04])
btnpUNPROCESSED = Button(resetax1, label= 'UNPROCESSED', color="red", hovercolor='0.975')
resetax2 = plt.axes([0.05, 0.73, 0.2, 0.04])
btnpLOWER = Button(resetax2, label= 'LOWER', color="lightgray", hovercolor='0.975')
resetax3 = plt.axes([0.05, 0.68, 0.2, 0.04])
btnpDERIVATIVE = Button(resetax3, label= 'DERIVATIVE', color="lightgray", hovercolor='0.975')

# OneShot BTN
resetax5 = plt.axes([0.05, 0.35, 0.2, 0.04])
btnoUNPROCESSED = Button(resetax5, label= 'OneShot UNPROCESSED', color="lightgray", hovercolor='0.975')
resetax6 = plt.axes([0.05, 0.3, 0.2, 0.04])
btnoLOWER = Button(resetax6, label= 'OneShot LOWER', color="lightgray", hovercolor='0.975')
resetax7 = plt.axes([0.05, 0.25, 0.2, 0.04])
btnoDERIVATIVE = Button(resetax7, label= 'OneShot DERIVATIVE', color="lightgray", hovercolor='0.975')

# '''TEXT BOX'''
mybox = {'facecolor':'y','edgecolor':'r','boxstyle':'round','alpha':0.5}
plt.text(0.05,15,('Period Scan'),fontsize = 11, bbox=mybox)
plt.text(0.05,4,('OneShot Scan'),fontsize = 11, bbox=mybox)

# '''Measure Scan'''
label1_1 = tk.Label(frame2, text = 'Status 1 :',font=("Arial", 30))
label1_1.grid(column=0,row=0, sticky='e')
label1_2 = tk.Label(frame2, textvariable=vari1 ,font=("Arial", 30))
label1_2.grid(column=1,row=0, sticky='w')

label2_1 = tk.Label(frame2, text = 'Status :',font=("Arial", 30))
label2_1.grid(column=0,row=1, sticky='e')
label2_2 = tk.Label(frame2, textvariable=vari2 ,font=("Arial", 30))
label2_2.grid(column=1,row=1, sticky='w')

label3_1 = tk.Label(frame2, text = 'Position :',font=("Arial", 30))
label3_1.grid(column=0,row=2, sticky='e')
label3_2 = tk.Label(frame2, textvariable=vari3 ,font=("Arial", 30))
label3_2.grid(column=1,row=2, sticky='w')

label4_1 = tk.Label(frame2, text = 'Energy :',font=("Arial", 30))
label4_1.grid(column=0,row=3, sticky='e')
label4_2 = tk.Label(frame2, textvariable=vari4 ,font=("Arial", 30))
label4_2.grid(column=1,row=3, sticky='w')

label5_1 = tk.Label(frame2, text = 'UNDEF :',font=("Arial", 30))
label5_1.grid(column=0,row=4, sticky='e')
label5_2 = tk.Label(frame2, textvariable=vari5 ,font=("Arial", 30))
label5_2.grid(column=1,row=4, sticky='w')

label6_1 = tk.Label(frame2, text = 'UNDEF :',font=("Arial", 30))
label6_1.grid(column=0,row=5, sticky='e')
label6_2 = tk.Label(frame2, textvariable=vari6 ,font=("Arial", 30))
label6_2.grid(column=1,row=5, sticky='w')

label7 = tk.Label(frame2,width=10,height=26)
label7.grid(column=0,row=6,columnspan=2)

# Frame BTN
f = font.Font(size=15, weight='bold')
btnToFrame1 = tk.Button(frame2,
    text= "Change To Profile",
    padx=507,
    pady=10,
    command=lambda:[openFrame(frame1)])
btnToFrame2 = tk.Button(frame1,
    text= "Change To Measure",
    padx=100,
    pady=10,
    command=lambda:[openFrame(frame2)])
btnToFrame1['font'] = f
btnToFrame2['font'] = f

btnToFrame1.grid(column=0,row=7, columnspan=2, sticky='ew')
btnToFrame2.grid(column=0,row=1, sticky='we')

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
    canvas.get_tk_widget().grid(column=0,row=0)
    
    anim = FuncAnimation(fig, animate, interval=500)
    openFrame(frame1)
    

    tk.mainloop()
