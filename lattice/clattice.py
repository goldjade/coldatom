# Optical Lattice potential (contour plot) 
#
# This program will plot contour plots in x-y and x-z of a 3-d optical lattic potential in the following reference.
# 
# ** P. Verkerk and L. Guidoni, Optical lattice: cold atoms ordered by light, J. Opt. B: Quantum Semiclass. Opt. 1 R23, 1999 **
#
# The form of the optical lattice in interest here is standar tetrahedron. It's figure and potential can be found on the pagre R32
# of the pare above.
#
# Important parts are labeled with Latin numbers, such as I, II, or III. The parameters are to
# be reasonalbe with our experimental conditions where Rubidium atoms and laser beam with the
# wavelength of 780nm are used. 
#
# When running this program, the parameters you might change would be the intensity and the angles of x-y axes.
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

# print("hbar*delta-prime is %e" % eunit)

# (II-a) To define variables (1)

lamda = 780*10**-9
kl = 2*math.pi/lamda
thetaxdegree = 20
thetaydegree = 20
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

fig = plt.figure()

xscale = 2
yscale = 2
step = 4e-2

x, y = np.mgrid[slice(-xscale, xscale + step, step),
								slice(-yscale, yscale + step, step)]
ax = fig.add_subplot(2, 2, 1)

cont1 = ax.pcolor(x, y, up(x, y, 0), cmap='RdBu_r')
fig.colorbar(cont1)
plt.xlabel(r'$X/lambda$')
plt.ylabel(r'$Y/lambda$')
plt.title('XY plot of $U_+$')

# (IV-b) Second subplot (- x-y plot)

bx = fig.add_subplot(2, 2, 2)
cont2 = bx.pcolor(x, y, un(x, y, 0), cmap='RdBu_r')
fig.colorbar(cont2)
plt.xlabel(r'$X/lambda$')
plt.ylabel(r'$Y/lambda$')
plt.title('XY plot of $U_-$')

# (IV-c) Third subplot (+ x-z plot)

cx = fig.add_subplot(2, 2, 3)
cont3 = cx.pcolor(x, y, up(x, 0, y), cmap='RdBu_r')
fig.colorbar(cont3)
plt.xlabel(r'X/lambda')
plt.ylabel(r'Z/lambda')
plt.title('XZ plot of $U_+')

# (IV-d) Fourth subplot (- x-z plot)

dx = fig.add_subplot(2, 2, 4)
cont4 = dx.pcolor(x, y, un(x, 0, y), cmap='RdBu_r')
fig.colorbar(cont4)
plt.xlabel(r'X/lambda')
plt.ylabel(r'Z/lambda')
plt.title('XZ plot of $U_-$')

# main title
fig.suptitle('Optical lattice potential with intensity = %.02f, theta_x = %.02f, and theta_y = %.02f \n \n Energy unit = %e & Lambda = 780nm ' %(intensity, thetaxdegree, thetaydegree, eunit), fontsize=15)

# to print the simulation time
time_f = time.time()
print "Total time consumed for the simulation is " + str(time_f - time_i) + " seconds"

plt.show()
