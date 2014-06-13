
OBJECTS2 = functions.o quadrature2.o test2.o
OBJECTS3 = functions.o quadrature3.o test3.o
FFLAGS = -fopenmp

.PHONY: test2 clean 

test2: test2.exe
	./test2.exe

test2.exe: $(OBJECTS2)
	gfortran $(FFLAGS) $(OBJECTS2) -o test2.exe

test3: test3.exe
	./test3.exe

test3.exe: $(OBJECTS3)
	gfortran $(FFLAGS) $(OBJECTS3) -o test3.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

clean:
	rm -f *.o *.exe *.mod

