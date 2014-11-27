# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

def fun1(x):
	return (x*x).sum(axis=1)

def fun2(x):
	return abs(x).sum(axis=1)+abs(x).prod(axis=1)

def fun3(x):
	suma = zeros(len(x))
	for i in range(len(x)):
		aux=0
		for j in range (len(x[i])):
			for k in range (j+1):
				aux += x[i][k]
			suma[i]+=(aux*aux).sum(axis=0)
	return suma


def graficar(gmax,grafica):
	plt.scatter(range(gmax),grafica)
	plt.show()

def ejecute(lS,lI,fun):
	w=0.7
	c1=1.4
	c2=1.4

	gmax=2000

	ndims=30
	nparts=40

	x = random.random((nparts,ndims))
	x = x*(lS-lI)+lI

	flag1=x>=lI
	flag2=x<lS
	flag3=logical_and(flag1,flag2)
	prom=sum(x[flag3])/len(x[flag3])
	x[~flag3]=prom


	fx = fun(x)
	pbest=x.copy()
	fx_pbest=fx.copy()
	index = argmin(fx_pbest)
	gbest=x[index].copy()
	fx_gbest=fx[index].copy()

	v =  zeros((nparts,ndims))
	grafica=[]
	i=0

	while i<gmax:
		cSocial = c1*random.random()*(pbest-x)
		cCognitivo = c2*random.random()*(gbest-x)
		v= w*v + cSocial + cCognitivo
		x = x+v

		flag1=x>=lI
		flag2=x<lS
		flag3=logical_and(flag1,flag2)
		prom=sum(x[flag3])/len(x[flag3])
		x[~flag3]=prom

		fx=fun(x)
		index = fx < fx_pbest
		pbest[index] = x[index]
		fx_pbest[index]=fx[index]
		index = argmin(fx_pbest)

		if  fx_pbest[index] < fx_gbest:
			gbest=x[index]
			fx_gbest=fx[index]

		grafica.append(fx_gbest)
		i+=1

	graficar(gmax,grafica)

def main():
	ejecute(100,-100,fun1)
	ejecute(10,-10,fun2)
	ejecute(100,-100,fun3)

main()
