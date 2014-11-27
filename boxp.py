#grafica

from numpy import loadtxt
from pylab import *
data1=[]
data = loadtxt("datos.txt")
for i in range (len(data)):
    for j in range(len(data[i])):
        data1.append(data[i][j])

figure(1)
boxplot(data1)
title('Grafica de resultados')
show()
