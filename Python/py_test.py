from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import time
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

fig = plt.figure()     #figure(도표) 생성



ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))
ax_2 = plt.subplot(212, xlim=(0, 50), ylim=(0, 512))


max_points = 50
max_points_2 = 50


line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)
line_2, = ax_2.plot(np.arange(max_points_2), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1,ms=1)


def init():
    return line
def init_2():
    return line_2


def animate(i):
    y = random.randint(0,1024)
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    print(new_y)
    return line

def animate_2(i):
    y_2 = random.randint(0,512)
    old_y_2 = line_2.get_ydata()
    new_y_2 = np.r_[old_y_2[1:], y_2]
    line_2.set_ydata(new_y_2)
    print(new_y_2)
    return line_2




root = Tk.Tk() #추가
label = Tk.Label(root,text="라벨").grid(column=0, row=0)#추가
canvas = FigureCanvasTkAgg(fig, master=root) #
canvas.get_tk_widget().grid(column=0,row=1) #



anim = animation.FuncAnimation(fig, animate  , init_func= init ,frames=200, interval=50, blit=False)
anim_2 = animation.FuncAnimation(fig, animate_2  , init_func= init_2 ,frames=200, interval=10, blit=False)
Tk.mainloop()

# import tkinter

# window = tkinter.Tk()

# window.title("Seah Test")
# window.geometry("640x400+100+100")
# window.resizable(False, False)

# label = tkinter.Label(window, text= "안녕하세요")
# label.pack()


# window.mainloop()


#data = [200,400,600]

# #int를 2byte로 바꾸는 코드
# def get2Byte_int(data) :
#     data_len = len(data)
#     convertBytes = bytearray(data_len*2)
#     for i in range(data_len) :
#         convertBytes[i*2] = ((data[i] >> 8) & 0x000000ff)
#         convertBytes[i*2+1] = (data[i] & 0x000000ff)
#     return convertBytes



# #int를 2byte로 바꾸는 코드
# def get2Byte_int(data) :
#     data_len = len(data)
#     convertBytes = bytearray(data_len*2)
#     for i in range(data_len) :
#         convertBytes[0] = ((data[data_len-1] >> 8) & 0x000000ff)
#         convertBytes[1] = (data[data_len-1] & 0x000000ff)
#         print(i)
        
    
#     return convertBytes