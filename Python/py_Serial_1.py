from ast import arg
from asyncio.windows_events import NULL
from concurrent.futures import thread
from socket import timeout
import threading
import serial
import time
import signal

exitThread = False # 쓰레드 종료용 변수
line = [] #라인 단위로 데이터 가져올 리스트 변수

#region Function
#시리얼 통신 접속
def serial_connect(port, baudrate = 115200, bytesize = serial.EIGHTBITS, parity = serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout = 0) :
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    return ser
#시리얼 통신 Send
def serial_send(ser) :
    #version
    #command = b'\xA5\x01\x82\x00\x00\x00\x28'
    #one shot
    #command = b'\xA5\x01\x83\x00\x00\x00\x29'
    #period
    command = b'\xA5\x01\x83\x11\x00\x00\x3A'

    ser.write(serial.to_bytes(command))
#시리얼 통신 Recieve
def serial_recieve(ser) :
    # 본코드
    # rx = ser.readline()
    # print(rx.hex())

    global line
    global exitThread

    # 쓰레드 종료될때까지 계속 돌림
    while not exitThread:
        #데이터가 있있다면
        for c in ser.readline():
            #line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10: #라인의 끝을 만나면..
                #데이터 처리 함수로 호출
                parsing_data(line)

                #line 변수 초기화
                del line[:]       

def parsing_data(data):
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침
    tmp = ''.join(data)

    #출력!
    print(tmp)

#쓰레드 종료용 시그널 함수
def handler(signum, frame):
     exitThread = True

#endregion




ser = serial_connect('COM4')

print("SPICA Sensor 스캔을 시작할까요?(Yes - 1, No - 2) : ")
answer = input()
if answer == '1' :
    #종료 시그널 등록
    signal.signal(signal.SIGINT, handler)
    
    #시리얼 통신 시작
    ser.open()

    #명령어 입력
    #serial_send(ser)

    #시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=serial_recieve, args=(ser,))

    #시작!
    thread.start()