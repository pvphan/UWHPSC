! $UWHPSC/wk3/fortran/functions.f90

module functions

contains

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt

real(kind=8) function f(x)
    implicit none
    real(kind=8), intent(in) :: x
    real, parameter :: pi = 3.14159265
    
    f = 0.6d0*x**2 + x*cos(pi*x) - 1.d0

end function f

real(kind=8) function fp(x)
    implicit none
    real(kind=8), intent(in) :: x
    real, parameter :: pi = 3.14159265
    
    fp = -pi*x*sin(pi*x) + 1.2d0*x + cos(pi*x)

end function fp

real(kind=8) function g_2(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    g_2 = 1.d0 - 0.6*x**2

end function g_2 

end module functions
