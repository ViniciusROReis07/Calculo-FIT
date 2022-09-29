from turtle import color
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-6, 6, 1)
y = np.arange(12, -12, -2)

plt.title('1 - g) y = −2x')
plt.plot(x, y, color="blue")
plt.plot(0, 0, color="blue" , marker = "o")

plt.plot(-3, 6, color="orange" , marker = "o")
plt.plot(-2, 4, color="orange" , marker = "o")
plt.plot(2, -4, color="orange" , marker = "o")


plt.grid(True)
plt.show()