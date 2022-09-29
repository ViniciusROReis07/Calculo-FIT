from turtle import color
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-5, 5, 1)
y = np.arange(-10, 10, 2)

plt.title('1 - f) y = 2x')
plt.plot(x, y, color="blue")
plt.plot(0, 0, color="blue" , marker = "o")

plt.plot(-2, -4, color="orange" , marker = "o")
plt.plot(2, 4, color="orange" , marker = "o")
plt.plot(-4, -8, color="orange" , marker = "o")

plt.grid(True)
plt.show()