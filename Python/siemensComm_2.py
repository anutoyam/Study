import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# 초기 데이터 생성
x = np.random.rand(480)  # x 좌표 (크기: 480)
z = np.random.rand(480)  # z 좌표 (크기: 480)
y = np.arange(480)      # y 좌표 (시간)

# 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot(x, y, z, '-o')

# 업데이트 함수 정의
def update(frame):
    # 데이터 업데이트
    x = np.random.rand(480)  # x 좌표 업데이트
    z = np.random.rand(480)  # z 좌표 업데이트
    
    # 그래프 업데이트
    line.set_data(x, y)
    line.set_3d_properties(z)

# 애니메이션 생성
ani = FuncAnimation(fig, update, frames=range(10), interval=200)

# 그래프 출력
plt.show()