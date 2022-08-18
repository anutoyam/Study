from sys import byteorder
import snap7

s7client = snap7.client.Client()
IP = '192.168.0.95'
RACK = 0
SLOT = 2

def plcConnect() :
    s7client.connect(IP,RACK,SLOT)

def plcDisConnect() :
    s7client.disconnect()

def plcIsConnect() :
    status = s7client.get_connected()
    return status

def plcDBRead() :
    data = s7client.db_read(59,51,1)
    bit = list('{0:08b}'.format(data[0]))[::-1]
    return bit

def plcDBWrite(value) :
    s7client.db_write(59,0,value)
    

#int를 2byte로 바꾸는 코드
def get2Byte_int(data) :
    convertBytes = bytearray(2)
    convertBytes[0] = ((data >> 8) & 0x000000ff)
    convertBytes[1] = (data & 0x000000ff)
    return convertBytes
#2byte를 int로 바꾸는 코드
def getInt_2Byte(data) :
    if data is None :
        return 0
    value = (0x0000ff00 & (data[0] << 8) | (0x000000ff & data[1]))
    return value

plcConnect()
bit = plcDBRead()
print(bit[7])
print(get2Byte_int(1001))





# a = int.from_bytes(test,'big', signed=True)
# print(a)

# bit = list('{0:08b}'.format(data[51]))[::-1]
# print(bit[7])