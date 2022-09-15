from asyncio.windows_events import NULL
from posixpath import split
import threading
import serial
import time


exitThread = False # 쓰레드 종료용 변수
line = [] #라인 단위로 데이터 가져올 리스트 변수


#region Function
#시리얼 통신 접속
def serial_connect(port = 'COM4', baudrate = 115200, bytesize = serial.EIGHTBITS, parity = serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout = 0.1) :
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.open()
    return ser

#시리얼 통신 확인
def serial_isconnect(ser) :
    status = ser.isOpen()
    return status

#시리얼 통신 Send
def serial_send(ser) :
    #cancel measure
    # command = b'\xA5\x01\x84\x00\x00\x00\x2A'
    #period SYNC
    #command = b'\xA5\x01\x83\x01\x00\x00\x2A'
    #period ASYNC
    #command = b'\xA5\x01\x83\x03\x00\x00\x2C'
    # one shot
    command = b'\xA5\x01\x83\x00\x00\x00\x29'
    ser.write(serial.to_bytes(command))
    time.sleep(0.1)
    # read buffer
    command = b'\xA5\x01\x92\x00\x00\x00\x38'
    ser.write(serial.to_bytes(command))

#시리얼 통신 Recieve
def serial_recieve(ser) :
    serial_send(ser)
    rx = ser.readline()
    # #rx = rx[20:32]
    # split_data = list(map(''.join, zip(*[iter(rx)]*2)))
    # print(split_data)
    splitRX = rx[11:139]
    return splitRX
        
def handle_exit(ser):
    command = b'\xA5\x01\x84\x00\x00\x00\x2A'
    ser.write(serial.to_bytes(command))

#endregion

#region Debug용 코드

# print("SPICA Sensor 스캔을 시작할까요?(Yes - 1, No - 2) : ")
# ser = serial_connect()

# answer = input()
# if answer == '1' :   
#     if ser.isOpen() == False :
#         ser.open()
        
#     #serial_send(ser)
#     thread = threading.Thread(target=serial_recieve, args=(ser,))
#     thread.start()
# elif answer == '2':
#     print("취소하셨습니다.")
#     ser.close()
#     if ser.isOpen() == False :
#         print("서버가 닫혔습니다.")
#     else :
#         print("안닫혔어요 확인점.")
# else :
#     print("1 또는 2로 입력 해 주세요 : ")
    
#endregion