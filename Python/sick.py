from siemensComm import PLCReader
import time

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
plc_reader.start_reading()

# Keep the main thread running
while True:
    time.sleep(1)