# intersections.py

from newton import solve

def p4(debug_solve=False):
	"""
	Problem 4 from Week 3 HW, find intersects of two functions.
	"""
	from numpy import sqrt
	for x0 in [-2.2, -1.6, .75, 1.4]:
		print " "  # blank line
		# print "for init of the funcial guess %22.15e" % x0
		x,iters = solve(fvals_inter, x0, debug=debug_solve)
		print "solve returns x = %22.15e after %i iterations " % (x,iters)
		fx,fpx = fvals_inter(x)
		print "the value of f(x) is %22.15e" % fx

def fvals_inter(x):
	import math
	pi = math.pi
	f = 0.6*x**2 + x*math.cos(pi*x) - 1
	fp = -pi*x*math.sin(pi*x) + 1.2*x + math.cos(pi*x)

	return f, fp