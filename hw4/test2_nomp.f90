! $UWHPSC/wk4/test2_omp.f90
! $ gfortran -fopenmp quadrature_omp.f90 test2_omp.f90

program test2

    use quadrature, only: trapezoid, error_table

    implicit none
    real(kind=8) :: a, b, int_true
    integer :: nvals(12), i
    real(kind=8) :: t1, t2, elapsed_cpu_time

    call cpu_time(t1)

    a = 0.d0
    b = 2.d0
    int_true = (b-a) + (b**4 - a**4) / 4.d0 - ((cos(1000.d0*b)/1000.d0) - (cos(1000.d0*a)/1000.d0))

    print 10, int_true
 10 format("true integral: ", es22.14)
    print *, " "  ! blank line

    ! values of n to test:
    do i=1,size(nvals)
        nvals(i) = 5.d0 * 2.d0**i
    enddo

    call error_table(f, a, b, nvals, int_true)

    call cpu_time(t2)
    elapsed_cpu_time = t2 - t1
    print *, "Elapsed CPU time", elapsed_cpu_time

contains

    real(kind=8) function f(x)
        implicit none
        real(kind=8), intent(in) :: x 
        real(kind=8) :: k

        k = 1000.d0
        
        f = 1.d0 + x**3 + sin(k*x)

    end function f

end program test2
