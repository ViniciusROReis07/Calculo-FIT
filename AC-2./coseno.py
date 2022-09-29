import numpy as np
import matplotlib.pyplot as plt

t2 = np.arange(0.0, 5.0, 0.02)

plt.plot(t2, np.cos(2*np.pi*t2))

plt.plot()

plt.show()
plt.grid(True)