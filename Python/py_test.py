import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons

fig = plt.subplot()
plt.subplots_adjust(left=0.25, bottom=0.25)
axcolor = 'lightgoldenrodyellow'
ax = plt.axes(xlim=(0, 127), ylim=(0, 255))
line, = ax.plot([], [], lw=3, color = 'red')


def animate(i):
    data = np.random.randint(low = 0, high = 255, size = 128)
    
    x = np.linspace(0,127,128)
    y = (data)
    line.set_data(x, y)
    return line,


# anim = FuncAnimation(fig, animate, frames=200, interval=100)


''' Add RadioButtons '''
radio = RadioButtons(ax, ('red', 'blue', 'green'), active=0)
# axes(rect) -> rect : left, bottom, width, height

def colorfunc(label):
    line.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()

