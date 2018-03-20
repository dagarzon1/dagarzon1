import numpy as np

#Definir datos de sample_1.
def sample_1(N):
	#Variable para definir numeros aleatorios a partir del arreglo y las 	probabilidades dadas.
	var=np.random.choice([-10,-5,3,9],size=N,p=[0.1,0.4,0.2,0.3])
	return var

#Definir datos de sample_2.
def sample_2(N):
	#Variable para definir numeros aleatorios a partir de la distribucion y el Betha dado.
	var=np.random.exponential(scale=0.5,size=N)
	return var

#Funcion para definir M promedios de los N numeros establecidos por la funcion que recibe como parametro.
def getmean(sampling_fun,N,M):
	#Variable de size M de unos que guardara el promedio de cada iteracion.
	res=np.ones(M)
	#Iteracion para obtener M promedios de N numeros establecidos por la funcion que se recibe como parametro.
	for i in range(M):
		#Variable de size N que define los diferentes numeros obtenidos por la funcion recibida como parametro.	
		var=sampling_fun(N)
		res[i]=np.sum(var)/len(var)
	return res

#Arreglo con los N que se requieren
N=np.array([10,100,1000])
#Valor de promedios constante
M=10000
#Iteracion para obtener los diferentes promedios
for i in N:
	#Promedio de datos obtenidos de sample_1
	sample=getmean(sample_1,i,M)
	#Nombre de archivo de los promedios de los datos obtenidos de sample_1
	name="sample_1_%d.txt"%i
	np.savetxt(name,sample)

	#Promedio de datos obtenidos de sample_2
	sample=getmean(sample_2,i,M)
	#Nombre de archivo de los promedios de los datos obtenidos de sample_2
	name="sample_2_%d.txt"%i
	np.savetxt(name,sample)

