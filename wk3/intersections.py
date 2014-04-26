# intersections.py

from newton import solve
import numpy as np
import matplotlib.pyplot as plt

def p4(debug_solve=False):
	"""
	Problem 4 from Week 3 HW, find intersects of two functions.
	"""
	from numpy import sqrt

	a_x = []
	a_fx = []

	for x0 in [-2.2, -1.6, -.75, 1.4]:
		print " "  # blank line
		# print "for init of the funcial guess %22.15e" % x0
		x,iters = solve(fvals_inter, x0, debug=debug_solve)
		print "solve returns x = %22.15e after %i iterations " % (x,iters)
		fx = f1(x)
		print "the value of f(x) is %22.15e" % fx

		# store values to plot
		a_x = np.append(a_x,x)
		a_fx = np.append(a_fx,fx)

	x_lin = np.linspace(-5,5,1001)
	pi = math.pi
	g1 = x_lin*np.cos(pi*x_lin)
	g2 = 1 - 0.6*x_lin**2
	plt.clf(); plt.plot(x_lin,g1,'r-'); plt.plot(x_lin,g2)
	plt.plot(a_x, a_fx,'ko')

	if debug_solve:
		for i in range(0,len(a_x)):
			print a_x[i], a_fx[i]

def f1(x):
	f = x*np.cos(np.pi*x)
	return f

def fvals_inter(x):
	pi = math.pi
	f = 0.6*x**2 + x*math.cos(pi*x) - 1
	fp = -pi*x*math.sin(pi*x) + 1.2*x + math.cos(pi*x)

	return f, fp