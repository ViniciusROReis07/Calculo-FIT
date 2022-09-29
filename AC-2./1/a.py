from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10],int)
y = np.array([12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8 ],int)

plt.title('1 - a) y = −x + 2')
plt.plot(x, y, color="blue")

plt.plot(0,2, color="blue" , marker = "o")
plt.plot(2,0, color="blue", marker = "o")

plt.plot(-7.5,9.40, color="orange", marker = "o")

plt.plot(-5,6.96, color="orange", marker = "o")

plt.plot(5,-2.98, color="orange", marker = "o")


plt.grid(True)

plt.show()

