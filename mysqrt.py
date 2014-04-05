"""
Coursera - UWHPSC - W1-L3.4
mysqrt.py
"""
def sqrt2(x):
	"""
	Docstring of sqrt2 function
	"""
	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		print "Before iteration %s, s = %20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if abs(delta_s/x) < tol:
			break
	print "After %s iterations, s = %20.15f" % (k,s)