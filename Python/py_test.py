print("센서의 데이터를 입력해 주세요.")
answer = input()
data = float(answer)
# rdata는 움직인 거리
rdata = (125-data)*10/7
# fdata는 시작점과 움직인 거리의 합 (3m+fdata)
fdata = round((300+rdata)/100,2)
print("대상과의 거리는 약 "+str(round((300+rdata)/100,2))+"m입니다.")