from turtle import color
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-4, 5, 1)
y = np.arange(12, -13, -3)

plt.title('1 - i) y = -3x')
plt.plot(x, y, color="blue")
plt.plot(0, 0, color="blue" , marker = "o")

plt.plot(-1, 3, color="orange" , marker = "o")
plt.plot(1, -3, color="orange" , marker = "o")
plt.plot(2, -6, color="orange" , marker = "o")


plt.grid(True)
plt.show()