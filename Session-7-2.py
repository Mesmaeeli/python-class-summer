import matplotlib.pyplot as plt
import numpy as np

xha = np.linspace(0,2*np.pi,50)
yha = np.sin(xha)

"""
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlabel = 'mehvar x ha',ylabel = 'mehvar y ha',title = 'sample matplot')
ax.set_xlabel('mehvar man')
ax.set_ylabel('mehvar dg')
ax.plot(xha,np.sin(xha))
"""
"""
fig, ax = plt.subplots(nrows = 2, ncols = 2)
ax[0,0].plot(xha,np.sin(xha))
ax[0,1].plot(xha,np.cos(xha))
ax[1,0].plot(xha,xha**2)
ax[1,1].plot(xha,xha**0.5)
fig.tight_layout(pad=3.0)
plt.show()
"""
"""
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005


rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(figsize=(8, 8))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)
ax_histx = plt.axes(rect_histx)
ax_histx.tick_params(direction='in', labelbottom=False)
ax_histy = plt.axes(rect_histy)
ax_histy.tick_params(direction='in', labelleft=False)

# the scatter plot:
ax_scatter.scatter(x, y)

# now determine nice limits by hand:
binwidth = 0.25
lim = np.ceil(np.abs([x, y]).max() / binwidth) * binwidth
ax_scatter.set_xlim((-lim, lim))
ax_scatter.set_ylim((-lim, lim))

bins = np.arange(-lim, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')

ax_histx.set_xlim(ax_scatter.get_xlim())
ax_histy.set_ylim(ax_scatter.get_ylim())

plt.show()

"""
"""
theta = np.linspace(0,2*np.pi,500)
l1 = [0.8,1.0,1.2]
list1 = []
for r_0 in l1:
   r = r_0 + np.cos(theta)
   x = r * np.cos(theta)
   y = r * np.sin(theta)
   plt.plot(x,y)
   list1.append('Diagram with r-0 = {}'.format(r_0))
   
plt.title("Limacon Shape")
plt.xlabel("x-axes")
plt.ylabel("y-axes")
plt.legend(list1)
plt.show()
"""
"""
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z)

plt.show()
"""
"""
t = np.arange(0,5,0.2)
plt.plot(t,t,'r-',t,t**2,'g--',t,t**3,'b^')
plt.show()
"""
