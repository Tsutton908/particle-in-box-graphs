import matplotlib.pyplot as plot
import numpy

x = numpy.linspace(0,1,100)
L = 1

#normalized wave function
def nwf(n,L,x):
	#wave function for standard particle with n value
	wave_func = numpy.sqrt(1/L)*numpy.sin(n*numpy.pi*x/L)
	return wave_func

def prob_den(n,L,x):
	den = numpy.square(nwf(n,L,x))
	return den

plot.figure(figsize=(10,10))
plot.suptitle("Wave Functions for different n")

m=int(input("Please input the desired value for n: \n"))
for n in range (1,m+1):
	nwf_list = []
	prob_den_list = []
	for i in x:
		nwf_list.append(nwf(n,L,i))
		prob_den_list.append(prob_den(n,L,i))
	#plot of the wave functions for each n value from 1 to input n
	plot.subplot(m,2,2*n-1)
	plot.plot(x,nwf_list)
	plot.xlabel("L", fontsize=14)
	plot.ylabel("Ψ", fontsize=14)
	plot.xticks(numpy.arange(0, 1, step=0.1))
	plot.title("Wave Function for n="+str(n), fontsize=16)
	#plot of the probability density for each n value from 1 to input n
	plot.subplot(m,2,2*n)
	plot.plot(x,prob_den_list)
	plot.xlabel("L", fontsize=13)
	plot.ylabel("Probability", fontsize=13)
	plot.xticks(numpy.arange(0, 1, step=0.1))
	plot.title("Probability Density for n="+str(n),fontsize=16)

#reassures layout so elements don't overlap
plot.tight_layout(rect=[0, 0.03, 1, 0.95])
plot.show()
