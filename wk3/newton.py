# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py
# Name: Paul Vinh Phan

def solve(fvals, x0, debug=False):
	"""
	fvals = a function that returns f(x) and f'(x) for any input x
	x0 = the initial guess
	debug = optional argument, default False
	"""
	maxiter = 20
	i = 0
	x = x0
	f, fp = fvals(x0)
	while (abs(f - fp) < 1e-14) & (i<=maxiter):
		f, fp = fvals(x)
		x = f - f/fp
		i+=1
	return x 

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