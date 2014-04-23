# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py
# Name: Paul Vinh Phan

def solve(fvals, x0, debug=False):
	"""
	fvals = a function that returns f(x) and f'(x) for any input x
	x0 = the initial guess
	debug = optional argument, default False
	"""
	x = x0
	kmax = 20 
	tol = 1.e-14
	for k in range(kmax):
		x0 = x
		if debug:
			print "Before iteration %s, x = %e" % (k,x)
		f, fp = fvals(x)
		x = x0 - f/fp
		delta_x = x - x0
		if abs(delta_x / x) < tol:
			break
	if debug:
		print "solve returns x = %e after %s iterations \
			the value of f(x) is %e" % (x, k+1, f) 
	return x, k 

def fvals_sqrt(x):
	"""
	Return f(x) and f'(x) for applying Newton to find a square root.
	"""
	f = x**2 - 4.
	fp = 2.*x
	# example: return tuple
	return f, fp

def test1(debug_solve=False):
	"""
	Test Newton iteration for the square root with different initial
	conditions.
	"""
	from numpy import sqrt
	for x0 in [1., 2., 100.]:
		print " "  # blank line
		x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
		print "solve returns x = %22.15e after %i iterations " % (x,iters)
		fx,fpx = fvals_sqrt(x)
		print "the value of f(x) is %22.15e" % fx
		assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x