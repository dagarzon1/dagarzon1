import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Funcion que establece la funcion de probabilidad de distribucion normal
def normal_dist(x,mean,sigma):
	return (1.0/(np.pi*2.0*sigma**2.0))*np.exp(-((x-mean)**2.0/(2.0*sigma**2.0)))

def get_fit(filename):
	#Variable que obtiene los datos del archivo recibido por parametros
	data=np.loadtxt(filename)
	#Variable que realiza el histograma de lso datos
	hist=np.histogram(data, bins=10, normed=True)
	#Fecuencias
	y=hist[0]
	#Punto medio de la barra que define el histograma
	x=(hist[1][:-1]+hist[1][1:])*0.5
	#parametros de la funcion normal_dist que mejor se acoplan a los datos 	recibidos
	fit=curve_fit(normal_dist,x,y)
	#Imprime los datos solicitados
	print "mean= ",fit[0][0]," sigma= ",fit[0][1]
	#Linspace para graficar ela juste
	x_new=np.linspace(np.min(x),np.max(x),1000)
	#Grafica el histograma y el ajuste proveniente de la funcion normal_dist
	plt.hist(data, bins=10, normed=True)
	plt.plot(x_new,normal_dist(x_new,fit[0][0],fit[0][1]))
	plt.savefig(filename.split('.')[0]+".png")
	plt.clf()
#Arreglo con los N que se requieren
N=np.array([10,100,1000])
#Iteracion que con cada archivo realiza la funcion get_fit
for i in N:
	get_fit("sample_1_%d.txt"%i)
	get_fit("sample_2_%d.txt"%i)

	
