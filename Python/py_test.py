import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=3)


def animate(i):
    data = np.random.randint(low = 0, high = 255, size = 128)
    
    x = np.linspace(0,127,128)
    y = (data)
    line.set_data(x, y)
    return line,


# anim = FuncAnimation(fig, animate, frames=200, interval=50)
anim = FuncAnimation(fig, animate, frames=200, interval=100)

plt.show()


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