import snap7
from snap7.util import *
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class PLCReader:
    def __init__(self, ip, rack, slot, db_number, start, size):
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.db_number = db_number
        self.start = start
        self.size = size
        self.plc = snap7.client.Client()

    def connect(self):
        self.plc.connect(self.ip, self.rack, self.slot)

    def read_data_from_plc(self):
        # Read data from the specified DB
        data = self.plc.db_read(self.db_number, self.start, self.size)

        # Parse the data and return it as a list of values
        values = []
        
        for i in range(0, self.size, 4):
            value = get_dint(data, i)
            values.append(value)

        return values
    
    def get_data_for_plot(self):
        values = self.read_data_from_plc()

        x_values = values[:480]  # 0~1916 (480개의 실수)
        y_values = values[1002:1482]  # 4008~5924 (480개의 실수)
        z_values = [values[1503]] * len(x_values)  # Only use one value for z

        return x_values, y_values, z_values
    
def update_graph(frame_number):
    x_values, y_values, z_values = plc_reader.get_data_for_plot()
    sc._offsets3d = (x_values, y_values, z_values)  # Update the 3D scatter plot

if __name__ == "__main__":
    # PLC connection parameters
    ip = "172.17.7.189"
    rack = 0
    slot = 1

    # Data Block parameters
    db_number = 10
    start = 0
    size = 6020

    plc_reader = PLCReader(ip, rack, slot, db_number, start, size)
    plc_reader.connect()

    x_values, y_values, z_values = plc_reader.get_data_for_plot()

    fig = plt.figure()  # Create a new figure
    ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot
    sc = ax.scatter(x_values, y_values, z_values)  # Create a 3D scatter plot
    ax.set_xlabel('X Values (DBD 0~1916)')
    ax.set_ylabel('Y Values (DBD 4008~5924)')
    ax.set_zlabel('Z Values (DBD 6012)')
    plt.title('PLC Data 3D Scatter Plot')

    ani = FuncAnimation(fig, update_graph, interval=100, blit=False)
    plt.show()