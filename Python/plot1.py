import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Plot data on each subplot
axs[0].plot(x, y1, color='red')
axs[0].set_title('Sin(x)')

axs[1].plot(x, y2, color='blue')
axs[1].set_title('Cos(x)')

axs[2].plot(x, y3, color='green')
axs[2].set_title('Tan(x)')

# Adjust spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()
