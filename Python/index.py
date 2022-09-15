import itertools

buf = []
a = bytes([10,20,30])
b = bytes([40,50,60])
print(list(a))
buf.append(a)
buf.append(b)
buf = list(itertools.chain(*buf))
print(buf)
