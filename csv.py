import numpy  
#read from csv
my_matrix = numpy.loadtxt(open("c:\\1.csv","rb"),delimiter=",",skiprows=0)  
#save into csv
numpy.savetxt('new.csv', my_matrix, delimiter = ',')  
