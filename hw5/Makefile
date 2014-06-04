
OBJECTS = functions.o quadrature2.o test2.o
FFLAGS = -fopenmp

.PHONY: test2 clean 

test: test2.exe
	./test2.exe

test2.exe: $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test2.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

clean:
	rm -f *.o *.exe *.mod

