from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])

plt.title('1 - e) y = x − 2')
plt.plot(x, y, color="blue")

plt.plot(0, -2, color="blue" , marker = "o")
plt.plot(2, 0, color="blue" , marker = "o")

plt.plot(-4, -6, color="orange" , marker = "o")
plt.plot(6, 4, color="orange" , marker = "o")
plt.plot(-2, -4, color="orange" , marker = "o")


plt.grid(True)
plt.show()