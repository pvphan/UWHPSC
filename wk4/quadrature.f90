! $UWHPSC/wk4/quadrature.f90

module quadrature

	! module parameters:
	implicit none

contains

real(kind=8) function trapezoid(f,a,b,n)
	! Estimate the integral using Trapezoid Rule.
	! Input:
	!	f: the function to find integral of
	!	a: the lower bound of integral
	!	b: the upper bound of integral
	!	n: the number of increments to integrate over
	! Returns:
	!	the area of all trapezoid given by the function 'f'

	implicit none
	real(kind=8), external :: f
	real(kind=8), intent(in) :: a, b
	integer, intent(in) :: n

	integer :: i, j
	real(kind=8) :: h, xj, fj, pfj, int_trapezoid

	h = (b-a)/(n-1) ! step size
	int_trapezoid = 0.d0! intialize sum as 0.00
	
	xj = a
	pfj = f(xj)			! initial value of f
	do j=1,n-1
		xj = xj + h 	! iterate xj
		fj = f(xj) 		! calculate next

		! add next piece of integral
		int_trapezoid = int_trapezoid + h*((pfj + fj)/2.d0)

		pfj = fj 		! store previous

	enddo

	trapezoid = int_trapezoid

end function trapezoid

subroutine error_table(f,a,b,nvals,int_true)

	implicit none
	real(kind=8), external :: f
	real(kind=8), intent(in) :: a, b, int_true
	integer, dimension(:), intent(in) :: nvals
	integer :: i, n
	real(kind=8) :: int_trap, last_error, error, ratio

	print *, "    n         trapezoid            error       ratio"

	do i=1,size(nvals)
		n = nvals(i)
		int_trap = trapezoid(f, a, b, n)
		error = abs(int_trap - int_true)
		ratio = last_error / error
		last_error = error
		print 11, n, int_trap, error, ratio
11		format(i8, es22.14, es13.3, es13.3)
	enddo

end subroutine error_table

end module quadrature