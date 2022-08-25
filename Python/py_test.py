data = [200,400,600]

# #int를 2byte로 바꾸는 코드
# def get2Byte_int(data) :
#     data_len = len(data)
#     convertBytes = bytearray(data_len*2)
#     for i in range(data_len) :
#         convertBytes[i*2] = ((data[i] >> 8) & 0x000000ff)
#         convertBytes[i*2+1] = (data[i] & 0x000000ff)
#     return convertBytes








# #int를 2byte로 바꾸는 코드
# def get2Byte_int(data) :
#     data_len = len(data)
#     convertBytes = bytearray(data_len*2)
#     for i in range(data_len) :
#         convertBytes[0] = ((data[data_len-1] >> 8) & 0x000000ff)
#         convertBytes[1] = (data[data_len-1] & 0x000000ff)
#         print(i)
        
    
#     return convertBytes