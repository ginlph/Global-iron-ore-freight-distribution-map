import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

# your dataset
nValues = np.arange(0, 30)
xValues = np.linspace(0, 10)
dataset = [(xValues-5-0.5*n)**2 for n in nValues]

# setup the normalization and the colormap
normalize = mcolors.Normalize(vmin=nValues.min(), vmax=nValues.max())
colormap = cm.jet

for n in nValues:
    # print(normalize(n))
    # print(colormap(normalize(n)))
    plt.plot(dataset[n], color=colormap(normalize(n)))

# setup the colorbar
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nValues)
plt.colorbar(scalarmappaple)
plt.show()
