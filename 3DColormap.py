import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap,LinearSegmentedColormap

n1 = 100
n2 = 100
x = np.linspace(0, 2.0*np.pi, n1);
y = np.linspace(0, 2.0*np.pi, n2);

X, Y = np.meshgrid(x, y);
#data = ([x, y])
i = 0;
j = 0;

for i in x:
    Z = np.sin(x) * np.cos(y);
    i = i + 1;
    for j in y:
        z = np.sin(x) * np.cos(y);
        j = j + 1;
        #print(z)

breaks1 = np.linspace(-1, 1, 10)
breaks2 = np.linspace(0, 2, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(2*X)*np.cos(2*Y)

plt.figure(figsize=(7,6))
plt.pcolormesh(X, Y, Z)
plt.colorbar()

plt.rcParams['contour.negative_linestyle'] = 'solid'
CS1 = plt.contour(x, y, Z, breaks1, colors = 'k', extend = 'both', vmin = -1.0, vmax = 1.0)
CS2 = plt.contourf(x, y, Z, breaks1, camp = 'seismic', extend = 'both', vmin = -1.0, vmax = 1.0)
plt.colorboard(ticks=breaks1, orientation = 'vertical')
plt.clabel(CS1, inline=1, fontsize=10)
plt.xlabel('angles 1')
plt.ylabel('angles 2')
#plt.grid()
plt.title('Sine- Cosine Wave- Sequential')

--
Samuel Larkin
Pronouns: He/Him/His
Iowa State University | Aerospace Engineering
