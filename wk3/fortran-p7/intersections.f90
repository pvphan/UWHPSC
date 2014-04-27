! $UWHPSC/wk3/fortran/intersections.f90

program intersections

    use newton, only: solve
    use functions, only: f, fp, g_2

    implicit none
    real(kind=8) :: x, x0, fx
    real(kind=8) :: x0vals(4)
    integer :: iters, itest
	logical :: debug         ! set to .true. or .false.

    print *, "Test routine for intersections of g_1 and g_2"
    debug = .true.

    ! values to test as x0:
    x0vals = (/-2.2d0, -1.6d0, -0.75d0, 1.4d0/)

    do itest=1,4
        x0 = x0vals(itest)
		print *, ' '  ! blank line
        call solve(f, fp, x0, x, iters, debug)

        print 11, x, iters
11      format('solver returns x = ', es22.15, ' after', i3, ' iterations')

        fx = g_2(x)
        print 12, fx
12      format('the value of f(x) is ', es22.15)

        enddo

end program intersections
