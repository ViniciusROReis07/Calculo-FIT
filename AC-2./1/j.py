from turtle import color
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-10, 9, 1)
y = np.arange(45, -11, -3)

# print(len(x))
# print(len(y))

plt.title('1 - j) y = 15 −3x')
plt.plot(x, y, color="blue")
plt.plot(0, 15, color="blue" , marker = "o")
plt.plot(5, 0, color="blue" , marker = "o")


plt.plot(-5, 30, color="orange" , marker = "o")
plt.plot(-7.5, 37.5, color="orange" , marker = "o")
plt.plot(2.5, 7.5, color="orange" , marker = "o")


plt.grid(True)
plt.show()