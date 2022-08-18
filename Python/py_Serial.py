import threading
import serial

exitThread = False # 쓰레드 종료용 변수
line = [] #라인 단위로 데이터 가져올 리스트 변수

#region Function
#시리얼 통신 접속
def serial_connect(port, baudrate = 115200, bytesize = serial.EIGHTBITS, parity = serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout = 2) :
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
    while not exitThread :
        rx = ser.read(18)
        print(rx.hex())
#endregion


ser = serial_connect('COM4')

print("SPICA Sensor 스캔을 시작할까요?(Yes - 1, No - 2) : ")

answer = input()
if answer == '1' :   
    if ser.isOpen() == False :
        ser.open()    
    thread = threading.Thread(target=serial_recieve, args=(ser,))
    thread.start()
    
elif answer == '2':
    print("취소하셨습니다.")
    ser.close()
    if ser.isOpen() == False :
        print("서버가 닫혔습니다.")
    else :
        print("안닫혔어요 확인점.")
else :
    print("1 또는 2로 입력 해 주세요 : ")
    

