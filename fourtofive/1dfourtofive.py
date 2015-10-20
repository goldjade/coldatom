import numpy as np
from numpy import linalg as la

#initialize

for x in xrange(0, 99999):

	h = np.zeros((9, 9), complex)

	z = 0.0 + 0.00001*x
	c = np.cos(2*np.pi*z)*np.cos(2*np.pi*z)
	s = np.sin(2*np.pi*z)*np.sin(2*np.pi*z)
	sc = np.cos(2*np.pi*z)*np.sin(2*np.pi*z)

# diagonal components

	h[0][0] = c + (1.0/45)*s
	h[1][1] = (36.0/45)*c + (3.0/45)*s
	h[2][2] = (28.0/45)*c + (6.0/45)*s
	h[3][3] = (21.0/45)*c + (10.0/45)*s
	h[4][4] = (15.0/45)*c + (15.0/45)*s
	h[5][5] = (10.0/45)*c + (21.0/45)*s
	h[6][6] = (6.0/45)*c + (28.0/45)*s
	h[7][7] = (3.0/45)*c + (36.0/45)*s
	h[8][8] = (1.0/45)*c + s

# off-diagonal components

	h[0][2] = -np.sqrt(28.0/45)*np.sqrt(1.0/45)*1.0j*sc
	h[1][3] = -np.sqrt(3.0/45)*np.sqrt(21.0/45)*1.0j*sc
	h[2][4] = -np.sqrt(6.0/45)*np.sqrt(15.0/45)*1.0j*sc
	h[3][5] = -np.sqrt(10.0/45)*np.sqrt(10.0/45)*1.0j*sc
	h[4][6] = -np.sqrt(6.0/45)*np.sqrt(15.0/45)*1.0j*sc
	h[5][7] = -np.sqrt(21.0/45)*np.sqrt(3.0/45)*1.0j*sc
	h[6][8] = -np.sqrt(28.0/45)*np.sqrt(1.0/45)*1.0j*sc

	h[2][0] = np.sqrt(28.0/45)*np.sqrt(1.0/45)*1.0j*sc
	h[3][1] = np.sqrt(3.0/45)*np.sqrt(21.0/45)*1.0j*sc
	h[4][2] = np.sqrt(6.0/45)*np.sqrt(15.0/45)*1.0j*sc
	h[5][3] = np.sqrt(10.0/45)*np.sqrt(10.0/45)*1.0j*sc
	h[6][4] = np.sqrt(6.0/45)*np.sqrt(15.0/45)*1.0j*sc
	h[7][5] = np.sqrt(21.0/45)*np.sqrt(3.0/45)*1.0j*sc
	h[8][6] = np.sqrt(28.0/45)*np.sqrt(1.0/45)*1.0j*sc


# diagonalize the hamiltonian

	w, v = la.eigh(h)
	
	print z, -w[0], -w[1], -w[2], -w[3], -w[4], -w[5], -w[6], -w[7], -w[8]

