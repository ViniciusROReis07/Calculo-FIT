from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8,8, 1)
y = np.arange(-8,8, 1)


plt.title('1 - b) y = x')
plt.plot(x, y, color="blue")

plt.plot(0, 0, color="blue" , marker = "o")

plt.plot(-6, -6, color="orange", marker = "o")

plt.plot(-2, -2, color="orange", marker = "o")

plt.plot(4,4, color="orange", marker = "o")


plt.grid(True)

plt.show()

