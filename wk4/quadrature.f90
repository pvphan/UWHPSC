! $UWHPSC/wk4/quadrature.f90

module quadrature

	! module parameters:
	implicit none
	integer, dimension(:), intent(in) :: nvals

contains

subroutine trapezoid(f,a,b,nvals)
	! Estimate the integral using Trapezoid Rule.
	! Input:
	!	f: the function to find integral of
	!	a: the lower bound of integral
	!	b: the upper bound of integral
	!	n: the number of increments to integrate over
	! Returns:
	!	the area of all trapezoid given by the function 'f'

	implicit none
	real(kind=8), intent(in) :: a, b
	real(kind=8), external :: f
	integer :: i
	real(kind=8) :: h, xj, fj, pfj, int_trapezoid

	h = (b-a)/(nvals-1) ! step size
	xj = a 				! left bound start
	fj = f(xj)			! initial value of f
	int_trapezoid = 0.d0! intialize sum as 0.00

	do i=1,nvals
		pfj = fj 		! store previous
		fj = f(xj) 		! calculate next

		! add next piece of integral
		int_trapezoid = int_trapezoid + h*((pfj + fj)/2.d0)

		xj = xj + h 	! iterate xj
	enddo

	print 11, int_trapezoid
11	format('Vinhs Trapezoid Rule gives int_trapezoid =', es22.15)
	print *, " "

end subroutine trapezoid

! subroutine error_table(f,a,b,nvals,int_true)

! end subroutine error_table

end module quadrature