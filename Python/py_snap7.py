import snap7

IP = '192.168.0.95'
RACK = 0
SLOT = 2

plc = snap7.client.Client()
plc.connect(IP,RACK,SLOT)

plc_info = plc.get_cpu_info()
print(f'Module Type : {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'State : {state}')

data = plc.db_read(59,0,52)
print(data)

changeData = plc.ab_write()