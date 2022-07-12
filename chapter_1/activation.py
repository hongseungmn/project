import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int32)

x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0,1.0,2.0])
print(sigmoid(x))

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

def relu(x):
    return np.maximum(0,x)
#maximum : 두 입력중 큰 값을 선택해 반환하는 함수
x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

