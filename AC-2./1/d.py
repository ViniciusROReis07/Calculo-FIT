from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=int)
y = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=int)

plt.title('1 - d) y = x + 2')
plt.plot(x, y, color="blue")

plt.plot(-2, 0, color="blue" , marker = "o")
plt.plot(0, 2, color="blue" , marker = "o")

plt.plot(-4, -2, color="orange" , marker = "o")
plt.plot(2, 4, color="orange" , marker = "o")
plt.plot(6, 8, color="orange" , marker = "o")

plt.grid(True)

plt.show()