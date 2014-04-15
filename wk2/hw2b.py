
"""
Demonstration module for quadratic interpolation.
Update this docstring to describe your code.
Modified by: Paul Vinh Phan, 4/14/2014
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.
    """

    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:
    A = np.vstack([np.ones(3), xi, xi**2]).T
    b = yi

    c = solve(A,b)

    return c

def cubic_interp(xi,yi):
    """
    Cubic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,3.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3.

    """

    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message

    # Set up linear system to interpolate through data points:
    A = np.vstack([np.ones(4), xi, xi**2, xi**3]).T
    b = yi

    c = solve(A,b)

    return c

def poly_interp(xi,yi):
    """
    Polynomial interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,...,n-1
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + ... + c[n-1]*x**n-1
    """

    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have the same length"
    assert len(xi)== len(yi), error_message

    # Set up linear system to interpolate through data points:
    for i in range(0,len(xi)-1):
        A = np.concatenate([A,np.vstack([xi**i])

    A = A.T
    b = yi

    c = solve(A,b)

    return c

def plot_quad(xi,yi,fig_num):

    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    c = quad_interp(xi,yi)
    y = c[0] + c[1]*x + c[2]*x**2

    plt.figure(fig_num)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(int(yi.min()) - 1, int(yi.max()) + 1)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

def plot_cubic(xi,yi,fig_num):

    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    c = cubic_interp(xi,yi)
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

    plt.figure(fig_num)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(int(yi.min()) - 1, int(yi.max()) + 1)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

def plot_poly(xi,yi,fig_num):

    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    c = poly_interp(xi,yi)
    y = c[0]
    
    # use Horners rule?
    # y = c[n-1]
    #   for j in range(n-1, 0, -1):
    #       y = y*x + c[j-1]

    for i in range(1,len(xi)-1):
        y += c[i]*x**i

    plt.figure(fig_num)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(int(yi.min()) - 1, int(yi.max()) + 1)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1., 0., 2.])

    print "c =      ", c
    print "c_true =      ", c_true

    plot_quad(xi,yi,1)
    plt.savefig('hw2a.png')   # save figure as .png file

    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)
        
def test_quad2():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1., 1., 2.])
    yi = np.array([0., 4., 3.])
    c = quad_interp(xi,yi)
    c_true = np.array([3., 2., -1.])

    print "c =      ", c
    print "c_true =      ", c_true

    plot_quad(xi,yi,2)
    plt.savefig('hw2b.png')   # save figure as .png file

    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_cubic1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1., 1., 2., 5.])
    yi = np.array([0., 4., 3., -1.])
    c = cubic_interp(xi,yi)

    print "c =      ", c

    plot_cubic(xi,yi,3)
    plt.savefig('cubic.png')   # save figure as .png file

    # test that all elements have small error:

def test_poly():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1., 1., 2., 5., -3.])
    yi = np.array([0., 4., 3., -1., 8.])
    c = poly_interp(xi,yi)

    print "c =      ", c

    plot_poly(xi,yi,3)
    plt.savefig('poly.png')   # save figure as .png file

if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    print "Results of test_quad1()"
    test_quad1()
    print "Results of test_quad2()"
    test_quad2()
    print "Results of test_cubic1()"
    test_cubic1()
    # print "Results of test_poly()"
    # test_poly()
