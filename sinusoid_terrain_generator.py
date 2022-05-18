import matplotlib.pyplot as plt
import numpy as np

# generate x-axis array
x = np.linspace(0, 20, 500)

# noisy sinusoid function
def terrain_detail(amplitude, frequency, detail, phase):
    return (amplitude/detail) * np.sin((x * frequency * detail) + (phase))

# add sinusoids together
y = terrain_detail(1, 1, 1, 0)
y += terrain_detail(1, 1, 5, 5)
y += terrain_detail(1, 1, 10, 6)

# threshold zeroing (waterline)
ymin = -0.7
for index, value in enumerate(y):
    if value < ymin:
        y[index] = ymin

# plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth = 1.0, color = 'b', )
plt.show()