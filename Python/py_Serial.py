from socket import timeout
import serial


ser = serial.Serial(
    port='COM4',
    baudrate=115200,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout= 1
)
#version
#command =b'\xA5\x01\x82\x00\x00\x00\x28'
#one shot
command =b'\xA5\x01\x83\x00\x00\x00\x29'
#period
# command =b'\xA5\x01\x83\x11\x00\x00\x3A'

ser.write(serial.to_bytes(command))

rx = ser.readline()

print("Receive Data: ", rx)

# if command == 'P' : #q가 들어오면 serial comm stop을 print하고 while 문 벗어남
#     print('serial comm stop !!!')
#     break 

ser.close()# serial 통신 close