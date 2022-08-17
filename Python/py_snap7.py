import snap7

IP = '192.168.0.95'
RACK = 0
SLOT = 2

plc = snap7.client.Client()
plc.connect(IP,RACK,SLOT)

def getInt_2Byte(data) :
    if data is None :
        return 0
    value = (0x0000ff00 & (data[0] << 8 | (0x000000ff & data[1])))
    return value

plc_info = plc.get_cpu_info()
print(f'Module Type : {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'State : {state}')

data = plc.db_read(59,0,52)

byte_val = b'\x01c'
int_val = int.from_bytes(byte_val,"big",signed="True")
print(int_val)

print(getInt_2Byte([data[2],data[3]]))
    

# result = map(''.join, zip(*[iter(hexdata)]*4))
# print(result)
#plc.db_write