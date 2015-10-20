# Optical Lattice potential 
#
# This program will plot cross sectional plots in x-y and x-z of a 3-d optical lattic potential in the following reference.
# 
# ** P. Verkerk and L. Guidoni, Optical lattice: cold atoms ordered by light, J. Opt. B: Quantum Semiclass. Opt. 1 R23, 1999 **
#
# The form of the optical lattice in interest here is standar tetrahedron. It's figure and potential can be found on the pagre R32
# of the pare above.
#
# Important parts are labeled with Latin numbers, such as I, II, or III. The parameters are to
# be reasonalbe with our experimental conditions where Rubidium atoms and laser beam with the
# wavelength of 780nm. 
#
# When running this program, the parameters you might change would be intensity and angles of x-y axes.
# You can find intensity parameter, "intensity" in (I), and angles, "thetaxdegree" and "thetaydegree" in (II-a).
# Whenever you run the program, these parameters will be shown in the title of the program.
#
# Notice that the scale of x, y, and z are in the unit of wavelength. And the scale of energy is
# presented in the program's title.
#
# Once ever the parameters are changes, the scales of the plot might have to be changed. There are 3 parameters for doing that.
# xscale, yscale, and step. Those can be found in (IV-a).
# 
# Made by Hoseong Asher Lee, and updated on June 23rd 2015 last.
# Email: hoseong.a.lee@gmail.com

# To track the libraries

import numpy as np
import matplotlib. pyplot as plt
import time
import scipy.constants as scon
import math as math
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# To measure the time consumed
time_i = time.time()

# (I) To define constants

h = scon.hbar
intensity = 3
s0 = float(intensity)/1064
Gamma = float(2)*math.pi*6*10 ** 6
delta = 11*Gamma
deltap = delta*s0/2
eunit = h*deltap

# print("energy unit (hbar*delta-prime) is %e" % eunit)

# (II-a) To define variables (1)

lamda = 780*10**-9
kl = 2*math.pi/lamda
thetaxdegree = 54.7 
thetaydegree = 54.7
thetax = (math.pi/180)*thetaxdegree
thetay = (math.pi/180)*thetaydegree

# (II-b) To define variables (2)

kx = kl*np.sin(thetax)
ky = kl*np.sin(thetay)
kp = kl*(np.cos(thetax)+np.sin(thetay))/2
kn = kl*(np.cos(thetax)-np.sin(thetay))/2

# (III) To define the optical lattice potential

def up(x, y, z):
	return -(8/3)*(np.cos(kx*lamda*x)*np.cos(kx*lamda*x) + np.cos(ky*lamda*y)*np.cos(ky*lamda*y) - np.cos(kx*lamda*x)*np.cos(ky*lamda*y)*np.cos(2*kp*lamda*z))

def un(x, y, z):
	return -(8/3)*(np.cos(kx*lamda*x)*np.cos(kx*lamda*x) + np.cos(ky*lamda*y)*np.cos(ky*lamda*y) + np.cos(kx*lamda*x)*np.cos(ky*lamda*y)*np.cos(2*kp*lamda*z))


# (IV-a) First subplot (+ x-y plot)

fig = plt.figure(figsize=plt.figaspect(1))

xscale = 2
yscale = 2
step = 7e-2

ax = fig.add_subplot(2, 2, 1, projection='3d')
X = np.arange(-xscale, xscale, step)
Y = np.arange(-yscale, yscale, step)
ax.set_zlim(-10,10)
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, up(X, Y, 0), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel(r'$X/lambda$')
ax.set_ylabel(r'$Y/lambda$')
ax.set_title("XY plot of $U_+$")

# (IV-b) Second subplot (- x-y plot)

bx = fig.add_subplot(2, 2, 2, projection='3d')
bx.set_zlim(-10,10)

surf2 = bx.plot_surface(X, Y, un(X, Y, 0), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

bx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
fig.colorbar(surf2, shrink=0.5, aspect=5)
bx.set_xlabel(r'$X/lambda$')
bx.set_ylabel(r'$Y/lambda$')
bx.set_title("XY plot of $U_-$")

# (IV-c) Third subplot (+ x-z plot)

cx = fig.add_subplot(2, 2, 3, projection='3d')
cx.set_zlim(-10, 10)

surf3 = cx.plot_surface(X, Y, up(X, 0, Y), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

cx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
fig.colorbar(surf3, shrink=0.5, aspect=5)
cx.set_xlabel(r'$X/lamda$')
cx.set_ylabel(r'$Z/lamda$')
cx.set_title('XZ plot of $U_+$')

# (IV-d) Fourth subplot (- x-z plot)

dx = fig.add_subplot(2, 2, 4, projection='3d')
dx.set_zlim(-10,10)

surf4 = dx.plot_surface(X, Y, un(X, 0, Y), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

dx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
fig.colorbar(surf4, shrink=0.5, aspect=5)
dx.set_xlabel(r'$X/lamda$')
dx.set_ylabel(r'$Z/lamda$')
dx.set_title('XZ plot of $U_-$')



# main title
fig.suptitle('Optical lattice potential with intensity = %.02f, theta_x = %.02f, and theta_y = %.02f \n \n Energy unit = %e & Lambda = 780nm ' %(intensity, thetaxdegree, thetaydegree, eunit), fontsize=15)

# to print the simulation time
time_f = time.time()
print "Total time consumed for the simulation is " + str(time_f - time_i) + " seconds"

plt.show()


